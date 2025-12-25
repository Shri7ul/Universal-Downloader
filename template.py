import os

STRUCTURE = {
    "app.py": "",
    "requirements.txt": "",
    "README.md": "",
    "downloads": {},
    "downloader": {
        "__init__.py": "",
        "engine.py": "# yt-dlp execution logic\n",
        "progress.py": "# progress hook logic\n",
        "validator.py": "# URL validation logic\n",
        "metadata.py": "#Metadata extractor\n",
        "constants.py": "#status constants helper\n",
        "platform.py": "#Platform detect\n",
        "summary.py" : "# Download summary helper\n",
        "filename.py": "# Filename template helper\n",
        "errors.py" : "# Simple error message mapper\n",


    },
}

def create_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)

        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        else:
            if not os.path.exists(path):  # already thakle overwrite করবে না
                with open(path, "w", encoding="utf-8") as f:
                    f.write(content)

if __name__ == "__main__":
    base_path = "."  # current directory
    create_structure(base_path, STRUCTURE)
    print("✅ Missing files/folders created (existing files untouched)")
