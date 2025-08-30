import os
import yt_dlp

# Define download directories
VIDEO_DOWNLOAD_DIR = "downloads/videos"
AUDIO_DOWNLOAD_DIR = "downloads/audio"

def create_download_directories():
    """Creates the directories for storing downloaded videos and audio."""
    os.makedirs(VIDEO_DOWNLOAD_DIR, exist_ok=True)
    os.makedirs(AUDIO_DOWNLOAD_DIR, exist_ok=True)

def download_media(url, download_type='video', is_playlist=False, logger=None):
    """
    Downloads a YouTube video or playlist.
    A custom logger can be passed to capture yt-dlp's output.
    """
    # Use a custom logger hook if provided
    if logger:
        ydl_hooks = [logger]
    else:
        ydl_hooks = []

    output_template = os.path.join(VIDEO_DOWNLOAD_DIR, '%(title)s.%(ext)s')
    ydl_opts = {
        'outtmpl': output_template,
        'ignoreerrors': is_playlist,
        'nocheckcertificate': True,
        'progress_hooks': ydl_hooks,
    }

    if download_type == 'audio':
        output_template = os.path.join(AUDIO_DOWNLOAD_DIR, '%(title)s.%(ext)s')
        ydl_opts.update({
            'outtmpl': output_template,
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        })

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # No need to print here, the logger hook will handle it
            ydl.download([url])
    except Exception as e:
        # If a logger is present, it might handle exceptions too
        # For now, we can re-raise or print
        print(f"Error during download: {e}")
        # Or if logger has an error method: logger.error(f"Error during download: {e}")
