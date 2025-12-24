#Platform detect
def detect_platform(url: str) -> str:
    url = url.lower()

    if "youtube.com" in url or "youtu.be" in url:
        return "youtube"
    if "facebook.com" in url or "fb.watch" in url:
        return "facebook"
    if "instagram.com" in url:
        return "instagram"
    if "twitter.com" in url or "x.com" in url:
        return "twitter"

    return "other"
