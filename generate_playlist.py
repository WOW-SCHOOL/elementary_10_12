from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parent
TRACKS_DIR = ROOT / "tracks"
PLAYLIST_FILE = ROOT / "playlist.json"
AUDIO_EXTENSIONS = {".mp3", ".ogg", ".wav", ".m4a"}

def natural_key(path: Path):
    return [int(part) if part.isdigit() else part.lower()
            for part in re.split(r"(\d+)", path.name)]

tracks = []
for file in sorted(TRACKS_DIR.iterdir(), key=natural_key):
    if file.is_file() and file.suffix.lower() in AUDIO_EXTENSIONS:
        tracks.append({
            "file": f"tracks/{file.name}",
            "title": file.stem.replace("_", " ")
        })

playlist = {
    "title": "English File — Elementary 2",
    "tracks": tracks
}

PLAYLIST_FILE.write_text(
    json.dumps(playlist, ensure_ascii=False, indent=2),
    encoding="utf-8"
)

print(f"Готово: добавлено треков — {len(tracks)}")
