import os
import argparse
import yt_dlp

# Define download directories
VIDEO_DOWNLOAD_DIR = "downloads/videos"
AUDIO_DOWNLOAD_DIR = "downloads/audio"

def create_download_directories():
    """Creates the directories for storing downloaded videos and audio."""
    os.makedirs(VIDEO_DOWNLOAD_DIR, exist_ok=True)
    os.makedirs(AUDIO_DOWNLOAD_DIR, exist_ok=True)

def download_media(url, download_type='video', is_playlist=False):
    """Downloads a YouTube video or playlist."""
    output_template = os.path.join(VIDEO_DOWNLOAD_DIR, '%(title)s.%(ext)s')
    ydl_opts = {
        'outtmpl': output_template,
        'ignoreerrors': is_playlist, # Continue on error if it's a playlist
        'nocheckcertificate': True,
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
            print(f"Starting download for: {url}")
            ydl.download([url])
            print(f"Successfully downloaded from {url}")
    except Exception as e:
        print(f"Error downloading {url}: {e}")


if __name__ == '__main__':
    create_download_directories()

    parser = argparse.ArgumentParser(description="Download YouTube videos, playlists, or search for media.")
    parser.add_argument("query", help="The URL or search term for the YouTube media.")
    parser.add_argument("-t", "--type", choices=['video', 'audio'], default='video',
                        help="The download type (video or audio). Defaults to video.")
    parser.add_argument("-p", "--playlist", action="store_true",
                        help="Flag to indicate that the URL is a playlist.")


    args = parser.parse_args()

    # If the query doesn't look like a URL, treat it as a search term.
    query = args.query
    if not query.lower().startswith('http'):
        query = f"ytsearch:{query}"

    download_media(query, args.type, args.playlist)
