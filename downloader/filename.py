# Filename helper (simple & clean)

def build_filename(info: dict, custom: str = "") -> str:
    title = info.get("title", "video").replace("/", "_")

    if custom:
        safe = custom.replace(" ", "_").replace("/", "_")
        return f"{safe}_{title}"

    return title
