# YouTube Downloader

A simple but powerful tool to download videos and audio from YouTube. It can be run as a command-line tool or as a graphical user interface (GUI).

## Features

-   Download single videos or entire playlists.
-   Search for media by name (downloads the top result).
-   Choose between downloading the full video or extracting the audio as an MP3.
-   Organizes downloads into `downloads/videos` and `downloads/audio` folders.

## Requirements

-   **Python 3:** This script is written in Python 3.
-   **Tkinter (for GUI):** The graphical interface requires Tkinter. Most Python installations include this by default. If yours does not, you may need to install it separately. For example, on Debian/Ubuntu:
    ```bash
    sudo apt-get install python3-tk
    ```
-   **yt-dlp:** The core library used for interacting with YouTube.
-   **ffmpeg:** Required for extracting audio and converting it to MP3.

You can install `yt-dlp` using pip:
```bash
pip install yt-dlp
```

You will need to install `ffmpeg` through your system's package manager (e.g., `sudo apt-get install ffmpeg` on Debian/Ubuntu, `brew install ffmpeg` on macOS).

## Usage

This program can be run in two ways: as a Graphical User Interface (GUI) or as a Command-Line Interface (CLI).

### GUI Mode

To run the graphical interface, execute the `youtube_downloader_gui.py` script:
```bash
python3 youtube_downloader_gui.py
```
A window will appear with fields for the URL/search term and options for the download type.

### Command-Line Mode

### Command Syntax

```bash
python3 downloader_cli.py [query] [options]
```

### Arguments and Options

-   `query`: (Required) The YouTube URL or the search term for the media you want to download. If your search term has spaces, enclose it in quotes.
-   `-t {video,audio}`, `--type {video,audio}`: (Optional) The type of media to download. Defaults to `video`. Use `audio` to download as an MP3.
-   `-p`, `--playlist`: (Optional) A flag to indicate that the provided URL is a playlist.

### Examples

**1. Download a single video:**
```bash
python3 downloader_cli.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```

**2. Search for a song and download the audio:**
```bash
python3 downloader_cli.py "Rick Astley - Never Gonna Give You Up" -t audio
```

**3. Download an entire playlist as videos:**
```bash
python3 downloader_cli.py "https://www.youtube.com/playlist?list=PL-wA2v_2csb-TICOtTzI--uY2P_ve_t2v" -p
```

**4. Download an entire playlist as audio MP3s:**
```bash
python3 downloader_cli.py "https://www.youtube.com/playlist?list=PL-wA2v_2csb-TICOtTzI--uY2P_ve_t2v" -p -t audio
```
