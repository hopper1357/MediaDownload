import argparse
from downloader_core import create_download_directories, download_media

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

    print(f"Preparing to download: {query}")
    download_media(query, args.type, args.playlist)
    print("CLI operation finished.")
