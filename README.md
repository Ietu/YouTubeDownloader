# YouTubeDownloader
Simple command-line tool to download YouTube a single video or full playlists as mp3 or mp4. I used this to create a local spotify playlist from a YouTube playlist.

> [!NOTE]
> Playlist needs to at least Unlisted or Public, Private playlists can't be downloaded.
> 
> Uses ```pytube``` and ```moviepy``` libraries, install them first with:
> 
> ```pip install -r requirements.txt```

## Example usage:
```python yt_downloader.py -U --url {playlist or video URL} -F --folder {path for downloads} -T --type {mp3 or mp4}```

Example playlist as mp3.
```python yt_downloader.py -U https://www.youtube.com/playlist?list=YOUR_PLAYLIST_ID -F C:\SpotifySongs -T mp3```

Example single video as mp4.
```python yt_downloader.py -U https://www.youtube.com/watch?v=VIDEO_ID C:\Downloads -T mp4```
