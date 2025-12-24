# URL validation logic
import re

def is_valid_url(url):
    regex = re.compile(
        r'^(https?:\/\/)?([\w\-]+\.)+[\w\-]+'
    )
    return re.match(regex, url)
