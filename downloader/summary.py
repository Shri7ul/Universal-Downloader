# Download summary helper

def build_summary(history: list) -> dict:
    total = len(history)
    platforms = {}
    success = 0

    for item in history:
        success += 1
        p = item.get("platform", "other")
        platforms[p] = platforms.get(p, 0) + 1

    return {
        "total": total,
        "success": success,
        "platforms": platforms
    }
