# music_sync
A project to label and sync metadata to mp3 files and a workaround for spotdl/yt-dlp download error.
Add spotdl and fetchmusic scripts to PATH to execute commands in powershell/cmd
## Generate Playlist Metadata
```sh
  spotdl save PLAYLIST_URL --save-file example.spotdl
```
Use the following flags to connect to Spotify app dev environment, bypassing download and rate limits: 

```sh
spotdl --client-id YOUR_CLIENT_ID --client-secret YOUR_CLIENT_SECRET [QUERY] 
```

You can also set client ID and Secret to be env variables in powershell using the following:
```sh
setx SPOTIPY_CLIENT_ID "your-client-id"
setx SPOTIPY_CLIENT_SECRET "your-client-secret"
```
## Download All YT mp3 files from spotify metadata file
```sh
  fetch_music_urls "C:\Path to spotdl json file containing song metadata" 
```
(downloads mp3 files in current path)
