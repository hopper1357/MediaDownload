import tkinter as tk
from tkinter import ttk
import threading
import queue
from downloader_core import create_download_directories, download_media

class ProgressHook:
    def __init__(self, queue):
        self.queue = queue

    def __call__(self, d):
        if d['status'] == 'downloading':
            # Extract progress information
            filename = d.get('filename', 'N/A')
            percent_str = d.get('_percent_str', '0.0%')
            speed_str = d.get('_speed_str', 'N/A')
            eta_str = d.get('_eta_str', 'N/A')

            # Format a detailed message
            msg = f"Downloading: {percent_str} | ETA: {eta_str} | Speed: {speed_str}"
            self.queue.put(msg)

        elif d['status'] == 'finished':
            filename = d.get('filename', 'N/A')
            self.queue.put(f"Finished downloading: {filename.split('/')[-1]}")

        elif d['status'] == 'error':
            self.queue.put("Error: An error occurred during download.")

class DownloaderApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("YouTube Downloader")
        self.geometry("600x350")

        self.log_queue = queue.Queue()

        # --- Main Frame ---
        main_frame = ttk.Frame(self, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # --- Input Section ---
        input_frame = ttk.LabelFrame(main_frame, text="Input", padding="10")
        input_frame.pack(fill=tk.X, pady=5)

        ttk.Label(input_frame, text="URL or Search Term:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.query_entry = ttk.Entry(input_frame, width=60)
        self.query_entry.grid(row=0, column=1, padx=5, pady=5, sticky=tk.EW)

        input_frame.columnconfigure(1, weight=1)

        # --- Options Section ---
        options_frame = ttk.LabelFrame(main_frame, text="Options", padding="10")
        options_frame.pack(fill=tk.X, pady=5)

        self.is_playlist = tk.BooleanVar()
        self.playlist_check = ttk.Checkbutton(options_frame, text="This is a playlist", variable=self.is_playlist)
        self.playlist_check.pack(side=tk.LEFT, padx=5)

        self.download_type = tk.StringVar(value="video")
        self.video_radio = ttk.Radiobutton(options_frame, text="Video", variable=self.download_type, value="video")
        self.audio_radio = ttk.Radiobutton(options_frame, text="Audio (MP3)", variable=self.download_type, value="audio")
        self.video_radio.pack(side=tk.LEFT, padx=5)
        self.audio_radio.pack(side=tk.LEFT, padx=5)

        # --- Action Section ---
        action_frame = ttk.Frame(main_frame, padding="10")
        action_frame.pack(fill=tk.X)

        self.download_button = ttk.Button(action_frame, text="Download", command=self.start_download)
        self.download_button.pack(pady=5)

        # --- Status Section ---
        status_frame = ttk.LabelFrame(main_frame, text="Status", padding="10")
        status_frame.pack(fill=tk.BOTH, expand=True, pady=5)

        self.status_label = ttk.Label(status_frame, text="Ready", anchor=tk.W, wraplength=580)
        self.status_label.pack(fill=tk.X)

        self.progress_bar = ttk.Progressbar(status_frame, mode='indeterminate')
        self.progress_bar.pack(fill=tk.X, pady=5)
        self.progress_bar.pack_forget()

        self.process_log_queue()

    def process_log_queue(self):
        try:
            while True:
                message = self.log_queue.get_nowait()
                self.status_label.config(text=message)
        except queue.Empty:
            pass
        self.after(100, self.process_log_queue)

    def start_download(self):
        query = self.query_entry.get()
        if not query:
            self.status_label.config(text="Error: Please enter a URL or search term.")
            return

        self.download_button.config(state=tk.DISABLED)
        self.progress_bar.pack(fill=tk.X, pady=5)
        self.progress_bar.start()
        self.status_label.config(text="Starting download...")

        download_thread = threading.Thread(target=self.download_worker, args=(query,), daemon=True)
        download_thread.start()

    def download_worker(self, query):
        final_status = "Download finished successfully!"
        try:
            create_download_directories()

            is_playlist = self.is_playlist.get()
            download_type = self.download_type.get()
            progress_hook = ProgressHook(self.log_queue)

            if not query.lower().startswith('http'):
                query = f"ytsearch:{query}"

            self.log_queue.put(f"Preparing to download: {query}")
            download_media(query, download_type, is_playlist, logger=progress_hook)

        except Exception as e:
            final_status = f"Error: {e}"
        finally:
            # Pass the final status message to the completion handler
            self.after(0, self.on_download_complete, final_status)

    def on_download_complete(self, final_message):
        """Called when the download is finished. Runs on the main thread."""
        self.status_label.config(text=final_message)
        self.progress_bar.stop()
        self.progress_bar.pack_forget()
        self.download_button.config(state=tk.NORMAL)


if __name__ == "__main__":
    app = DownloaderApp()
    app.mainloop()
