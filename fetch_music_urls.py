import json
import sys
import subprocess
from pathlib import Path

def build_query(track: dict):
    name = track.get("name", "")
    artists = track.get("artists", [])
    if isinstance(artists, list):
        artist_str = ", ".join(artists)
    else:
        artist_str = artists
    return f"{name} {artist_str}".strip()

def search_and_download_ytdl(query: str):
    try:
        print(f"[YT-DLP] Searching and downloading: {query}")
        subprocess.run([
            "yt-dlp",
            "-x", "--audio-format", "mp3",
            "--embed-thumbnail",
            "--embed-metadata",
            f"ytsearch1:{query}"
        ], check=True)
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] yt-dlp failed for query: {query}")

def process_spotdl_file(file_path: str):
    file = Path(file_path)
    if not file.exists():
        print(f"[ERROR] File does not exist: {file_path}")
        return

    try:
        with open(file, "r", encoding="utf-8-sig") as f:
            tracks = json.load(f)
    except Exception as e:
        print(f"[ERROR] Could not parse metadata file: {e}")
        return

    if not isinstance(tracks, list):
        print(f"[ERROR] Metadata is not a list of tracks.")
        return

    for i, track in enumerate(tracks, start=1):
        query = build_query(track)
        if query:
            print(f"\n[{i}/{len(tracks)}] Processing: {query}")
            search_and_download_ytdl(query)
        else:
            print(f"[SKIP] Could not build query for track #{i}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python yt_fetch_from_spotdl_list.py <spotdl_json_file>")
        sys.exit(1)

    process_spotdl_file(sys.argv[1])
