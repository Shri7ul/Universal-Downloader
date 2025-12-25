import streamlit as st

from downloader.engine import download_media
from downloader.metadata import extract_metadata
from downloader.validator import is_valid_url
from downloader.progress import progress_hook
from downloader.platform import detect_platform
from downloader.filename import build_filename
from downloader.errors import map_error
from downloader.summary import build_summary

st.set_page_config("Universal Downloader", "📥")

# ---------------- SESSION STATE ----------------
if "history" not in st.session_state:
    st.session_state.history = []

# ---------------- UI ----------------
st.title("📥 Universal Downloader")

urls = st.text_area(
    "Paste URL(s) — one per line",
    height=120
)

preset = st.selectbox(
    "🎛️ Download Preset",
    [
        "Custom",
        "YouTube 1080p",
        "Instagram Reel",
        "Audio Only (Podcast)",
        "Fast & Safe"
    ]
)

download_type = st.radio("Type", ["Video", "Audio"])
quality = st.selectbox("Quality", ["Best", "1080p", "720p", "480p"])

custom_name = st.text_input(
    "✏️ Custom Name (optional)",
    placeholder="e.g. DSA_Lecture, ProjectX, Podcast"
)

start = st.button("⬇️ Start Download")

# ---------------- PRESET LOGIC ----------------
def apply_preset(preset_name):
    if preset_name == "YouTube 1080p":
        return {"type": "video", "format": "bestvideo[height<=1080]+bestaudio/best"}
    if preset_name == "Instagram Reel":
        return {"type": "video", "format": "best"}
    if preset_name == "Audio Only (Podcast)":
        return {"type": "audio", "format": "bestaudio"}
    if preset_name == "Fast & Safe":
        return {"type": "video", "format": "best"}
    return None

# ---------------- START ----------------
if start:
    url_list = [u.strip() for u in urls.splitlines() if u.strip()]

    if not url_list:
        st.error("Please paste at least one valid URL.")
        st.stop()

    st.subheader("📊 Preview")

    valid_items = []

    for url in url_list:
        if not is_valid_url(url):
            st.warning(f"Invalid URL skipped: {url}")
            continue

        info = extract_metadata(url)
        platform = detect_platform(url)

        col1, col2 = st.columns([1, 3])

        with col1:
            if info.get("thumbnail"):
                st.image(info["thumbnail"], use_container_width=True)

        with col2:
            st.markdown(f"**🎬 {info.get('title', 'Unknown')}**")
            st.markdown(f"🌐 Platform: `{platform}`")

            duration = info.get("duration")
            if duration:
                dur_text = f"{int(duration // 60)}m {int(duration % 60)}s"
            else:
                dur_text = "Unknown"

            filesize = info.get("filesize_approx") or info.get("filesize")
            if filesize:
                size_text = f"{round(filesize / 1024 / 1024, 2)} MB"
            else:
                size_text = "Unknown"

            st.markdown(f"⏱ {dur_text} | 📦 {size_text}")

        st.divider()

        valid_items.append({
            "url": url,
            "info": info,
            "platform": platform
        })

    # ---------------- DOWNLOAD ----------------
    st.subheader("⬇️ Download Progress")

    for item in valid_items:
        with st.container(border=True):
            st.markdown(f"**⬇️ {item['info'].get('title', 'Unknown')}**")
            status_box = st.empty()
            progress_bar = st.progress(0)

        status_box.info("Starting download...")

        preset_conf = apply_preset(preset)

        filename = build_filename(
            item["info"],
            custom_name
        )

        opts = {
            "platform": item["platform"],
            "type": download_type.lower(),
            "format": "best" if quality == "Best"
            else f"bestvideo[height<={quality[:-1]}]+bestaudio/best",
            "filename": filename,
        }

        if preset_conf:
            opts.update(preset_conf)

        def hook(d):
            progress_hook(d, progress_bar, status_box)

        try:
            download_media(item["url"], opts, hook)
            status_box.success("✅ Download completed")

            st.session_state.history.append({
                "title": item["info"].get("title"),
                "platform": item["platform"]
            })

        except Exception as e:
            friendly = map_error(str(e))
            status_box.error(friendly)

    st.success("🎉 All downloads finished")

# ---------------- SUMMARY ----------------
if st.session_state.history:
    st.divider()
    st.subheader("📊 Download Summary")

    summary = build_summary(st.session_state.history)

    st.markdown(f"**Total Downloads:** {summary['total']}")
    st.markdown(f"**Successful:** {summary['success']}")

    st.markdown("**By Platform:**")
    for p, c in summary["platforms"].items():
        st.markdown(f"- {p}: {c}")

    st.divider()
    st.subheader("🕘 Download History")

    for h in st.session_state.history[-10:][::-1]:
        st.markdown(f"- **{h['title']}** (`{h['platform']}`)")
