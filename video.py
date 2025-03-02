import yt_dlp

# Configure YoutubeDL options
ydl_opts = {
    'format': 'bestvideo[height>=720]+bestaudio/best[height>=720]',  # Ensure 720p or higher video with best audio
    'outtmpl': '%(title)s.%(ext)s',  # Save file with title as filename
    'merge_output_format': 'mp4',  # Merge into an MP4 file
    'postprocessors': [{  # Ensure ffmpeg is used for merging
        'key': 'FFmpegVideoConvertor',
        'preferedformat': 'mp4',  # Convert output to MP4 if needed
    }],
}

# Download the video
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([''])  # Download the video
