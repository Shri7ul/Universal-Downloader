def progress_hook(d, progress_bar, status_text):
    if d["status"] == "downloading":
        percent = d.get("_percent_str", "0%").strip()
        speed = d.get("_speed_str", "N/A")
        eta = d.get("_eta_str", "N/A")

        try:
            p = int(percent.replace("%", ""))
            progress_bar.progress(p)
        except:
            pass

        status_text.markdown(
            f"⬇️ **Downloading**  \n"
            f"📊 {percent} | ⚡ {speed} | ⏳ {eta}"
        )

    elif d["status"] == "finished":
        progress_bar.progress(100)
        status_text.success("✅ Download completed")
