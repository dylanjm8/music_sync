# music_sync
A project to label and sync metadata to mp3 files and a workaround for spotdl/yt-dlp download error.

## Generate Playlist Metadata
```sh
  spotdl save PLAYLIST_URL --save-file example.spotdl
```
## Download All YT mp3 files from spotify metadata file
```sh
  fetch_music_urls "C:\Path to spotdl json file containing song metadata" 
```
(downloads mp3 files in current path)
