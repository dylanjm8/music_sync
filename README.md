# music_sync
A project to label and sync metadata to mp3 files

## Generate Playlist Metadata
```sh
  spotdl save PLAYLIST_URL --save-file example.spotdl
```
## Download All YT mp3 files from spotify metadata file
```sh
  fetch_music_urls "C:\Path to spotdl json file containing song metadata" 
```
