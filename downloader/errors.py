# Simple error message mapper

def map_error(error_text: str) -> str:
    text = error_text.lower()

    if "private video" in text:
        return "🔒 This video is private."
    if "sign in" in text or "login" in text:
        return "🔑 Login required to download this video."
    if "copyright" in text:
        return "⚠️ Copyright-protected content."
    if "429" in text or "too many requests" in text:
        return "⏳ Too many requests. Please try again later."
    if "403" in text or "forbidden" in text:
        return "🚫 Access forbidden for this video."
    if "404" in text or "not found" in text:
        return "❌ Video not found."
    if "network" in text:
        return "🌐 Network error. Check your internet connection."

    return "❌ Download failed due to an unknown error."