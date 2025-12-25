# 📥 Universal Downloader

A simple, clean, and practical **IDM alternative** built with Python, Streamlit, and yt-dlp.

This tool is designed for **daily use** — paste a URL, preview the content, and download it cleanly without ads, trials, or unnecessary complexity.

---

## ✨ Why this project exists

Most download managers:
- Are paid or time-limited (like IDM)
- Show ads or unnecessary popups
- Feel heavy for simple daily tasks

**Universal Downloader** focuses on one thing only:

> **Download public online videos & audio — simply and reliably.**

---

## 🚀 Features

- 🌐 Supports multiple platforms (YouTube, Facebook, Instagram, Twitter/X, more via yt-dlp)
- 🖼️ Thumbnail preview before download
- ⏱️ Shows duration and approximate file size
- 🎥 Video or 🎧 Audio-only download
- 📊 Quality selection (Best, 1080p, 720p, etc.)
- ✏️ Optional custom name for organizing downloads
- 📂 Automatic folder organization by platform
- 🎛️ One-click download presets (YouTube 1080p, Audio only, Fast & Safe)
- 📈 Real-time progress, speed, and ETA
- ❌ Human-friendly error messages (no scary yt-dlp logs)
- 🕘 Session-based download history

---

## 🧭 What this tool is **not**

To keep things simple and honest:

- ❌ No background/async queue (Streamlit limitation)
- ❌ No DRM-protected sites (Netflix, Spotify, Prime, etc.)
- ❌ No account system or cloud upload
- ❌ No analytics or tracking

This is a **local, personal downloader**, just like IDM.

---

## 🛠️ Tech Stack

- **Python 3.11**
- **Streamlit** – UI
- **yt-dlp** – Download engine
- **ffmpeg** – Media processing (required for best quality & audio)

---

## 📁 Project Structure

```bash
universal_downloader/
│
├── app.py # Streamlit UI
├── downloader/
│ ├── engine.py # yt-dlp execution logic
│ ├── progress.py # progress hook logic
│ ├── validator.py # URL validation logic
│ ├── metadata.py # metadata extractor
│ ├── platform.py # platform detection
│ ├── filename.py # filename helper
│ ├── errors.py # friendly error mapping
│ └── summary.py # download summary helper
│
├── downloads/ # auto-created download folders
├── requirements.txt
├── template.py
└── README.md
```

## ⚙️ Installation & Run

### 1️⃣ Create environment
```bash
conda create -n universaldwn python=3.11 -y
```
```bash
conda activate universaldwn
```

2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

3️⃣ Run the app
```bash
streamlit run app.py
```


Browser will open automatically.

### 📦 ffmpeg requirement

For best video+audio merging and audio extraction, make sure ffmpeg is installed and available in your system PATH.

### 🔐 Legal & Ethical Note

This tool only works with publicly accessible content supported by yt-dlp.

You are responsible for:

- Respecting platform terms

- Avoiding copyright misuse

- Using downloads for personal/educational purposes

### 🧠 Design Philosophy

- Keep it simple

- Avoid fake “advanced” features

- Prefer reliability over complexity

- Solve a real daily problem

### 📌 Status

#### Stable – Daily Use Ready

Future improvements (optional):

- Open download folder button

- Safe mode toggle

- Retry-on-failure

- Windows EXE build

### 🙌 Final Note

This project was built to be used, not just showcased.

If you use IDM daily and want a clean, no-trial alternative —
this tool does the job.

### 👨‍💻 Author
**InHuman**

### 📜 License
Open-source.  
Free for learning and academic use.