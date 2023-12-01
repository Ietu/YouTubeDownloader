# YouTubeDownloader
Simple command-line interface tool to download YouTube a single video or full playlists as mp3 or mp4. I used this to create a local spotify playlist from a YouTube playlist.

pip install -r requirements.txt

Example usage:
python yt_downloader.py -U {playlist or video URL} -F {path for downloads} -T {mp3 or mp4}

Example playlist as mp3.
python yt_downloader.py -U https://www.youtube.com/playlist?list=YOUR_PLAYLIST_ID -F C:\SpotifySongs -T mp3
