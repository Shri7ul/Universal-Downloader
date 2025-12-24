# Filename template helper

def build_filename(template: str, info: dict, platform: str, quality: str, custom: str = "") -> str:
    title = info.get("title", "video").replace("/", "_")
    q = quality.lower()

    name = template
    name = name.replace("{title}", title)
    name = name.replace("{platform}", platform)
    name = name.replace("{quality}", q)

    if custom:
        safe_custom = custom.replace(" ", "_").replace("/", "_")
        name = f"{safe_custom}_{name}"

    return name
