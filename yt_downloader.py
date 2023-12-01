import os
import sys
import argparse

try:
    from pytube import YouTube, Playlist
    from moviepy.editor import *
except ImportError as e:
    sys.exit(f"Required module missing: {e.name}. Please install it with 'pip install {e.name}'.")

def download_video(url: str, folder_path: str, format_type: str):
    try:
        video = YouTube(url)
        filename = f"{video.title}.{format_type}"

        if format_type == 'mp3':
            stream = video.streams.filter(only_audio=True).first()
            if stream is None:
                raise Exception("No audio stream found")
            temp_filename = f"{video.title}_temp.mp4"
            temp_file_path = stream.download(output_path=folder_path, filename=temp_filename)
            final_file_path = os.path.join(folder_path, filename)
            convert_to_mp3(temp_file_path, final_file_path)
        elif format_type == 'mp4':
            stream = video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
            if stream is None:
                raise Exception("No video stream found")
            stream.download(output_path=folder_path, filename=filename)

        return True, None
    except Exception as e:
        return False, (video.title, url)


def download_playlist(playlist_url: str, folder_path: str, format_type: str) -> None:
    playlist = Playlist(playlist_url)
    failed_videos = []

    for url in playlist.video_urls:
        success, result = download_video(url, folder_path, format_type)
        if not success:
            failed_videos.append(result)

    total_videos = len(playlist.video_urls)
    downloaded_count = total_videos - len(failed_videos)

    print(f"\nDownloaded {downloaded_count}/{total_videos} videos.")
    if failed_videos:
        print("Videos that were not downloaded:")
        for title, url in failed_videos:
            print(f"{title} - {url}")

def convert_to_mp3(temp_file_path: str, final_file_path: str) -> None:
    video_clip = AudioFileClip(temp_file_path)
    video_clip.write_audiofile(final_file_path)
    video_clip.close()
    os.remove(temp_file_path)

def main():
    parser = argparse.ArgumentParser(description="Download YouTube Videos or Playlists as MP3 or MP4")
    parser.add_argument("-U", "--url", help="YouTube video or playlist URL", required=True)
    parser.add_argument("-F", "--folder", help="Folder to save files in", required=True)
    parser.add_argument("-T", "--type", help="Format type to download (mp3 or mp4)", choices=['mp3', 'mp4'], default='mp3')
    args = parser.parse_args()

    if "playlist?list=" in args.url:
        download_playlist(args.url, args.folder, args.type)
    else:
        success, result = download_video(args.url, args.folder, args.type)
        if not success:
            print("Could not download the video:")
            title, url = result
            print(f"{title} - {url}")
        else:
            print(f"Downloaded the video successfully as {args.type.upper()}.")

if __name__ == "__main__":
    main()
