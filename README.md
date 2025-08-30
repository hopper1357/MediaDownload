# YouTube Downloader

A simple but powerful command-line tool to download videos and audio from YouTube. You can download individual media, entire playlists, or even search for media directly from the command line.

## Features

-   Download single videos or entire playlists.
-   Search for media by name (downloads the top result).
-   Choose between downloading the full video or extracting the audio as an MP3.
-   Organizes downloads into `downloads/videos` and `downloads/audio` folders.

## Requirements

To use this script, you will need to have Python 3 installed, along with the following libraries:

-   `yt-dlp`: The core library used for interacting with YouTube.
-   `ffmpeg`: Required for extracting audio and converting it to MP3.

You can install `yt-dlp` using pip:
```bash
pip install yt-dlp
```

You will need to install `ffmpeg` through your system's package manager (e.g., `sudo apt-get install ffmpeg` on Debian/Ubuntu, `brew install ffmpeg` on macOS).

## Usage

The script is run from the command line and accepts a URL or a search term as its main argument.

### Command Syntax

```bash
python youtube_downloader.py [query] [options]
```

### Arguments and Options

-   `query`: (Required) The YouTube URL or the search term for the media you want to download. If your search term has spaces, enclose it in quotes.
-   `-t {video,audio}`, `--type {video,audio}`: (Optional) The type of media to download. Defaults to `video`. Use `audio` to download as an MP3.
-   `-p`, `--playlist`: (Optional) A flag to indicate that the provided URL is a playlist.

### Examples

**1. Download a single video:**
```bash
python youtube_downloader.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```

**2. Search for a song and download the audio:**
```bash
python youtube_downloader.py "Rick Astley - Never Gonna Give You Up" -t audio
```

**3. Download an entire playlist as videos:**
```bash
python youtube_downloader.py "https://www.youtube.com/playlist?list=PL-wA2v_2csb-TICOtTzI--uY2P_ve_t2v" -p
```

**4. Download an entire playlist as audio MP3s:**
```bash
python youtube_downloader.py "https://www.youtube.com/playlist?list=PL-wA2v_2csb-TICOtTzI--uY2P_ve_t2v" -p -t audio
```
