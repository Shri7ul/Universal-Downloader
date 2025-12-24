# yt-dlp execution logic

import yt_dlp
import os


def download_media(url, options, hook):
    platform = options.get("platform", "other")
    filename = options.get("filename", "%(title)s")

    base_path = os.path.join("downloads", platform)
    os.makedirs(base_path, exist_ok=True)

    ydl_opts = {
        "outtmpl": os.path.join(base_path, f"{filename}.%(ext)s"),
        "quiet": True,
        "no_warnings": True,
        "ignoreerrors": True,
        "sleep_interval": 2,
        "max_sleep_interval": 5,
        "progress_hooks": [hook],
    }

    # Audio only
    if options.get("type") == "audio":
        ydl_opts.update({
            "format": "bestaudio",
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                }
            ],
        })

    # Video
    else:
        ydl_opts["format"] = options.get("format", "best")

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
