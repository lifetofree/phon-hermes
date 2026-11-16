#!/bin/bash
# Transcribe one video -> wav -> whisper.cpp JSON(full) -> markdown
# Usage: transcribe.sh <video.mp4>
set -e
VID="$1"
BASE="$(basename "$VID" .mp4)"
DIR="$(dirname "$VID")"           # .../opb-notes/videos
ROOT="$(dirname "$DIR")"          # .../opb-notes
AUD="$ROOT/audio"; OUT="$ROOT/transcripts"; TMP="$ROOT/json"
mkdir -p "$AUD" "$OUT" "$TMP"
WAV="$AUD/$BASE.wav"
echo "=== [$BASE] probing duration ==="
DUR=$(ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 "$VID")
echo "duration: $DUR s"
echo "=== [$BASE] extracting 16kHz mono audio ==="
[ -f "$WAV" ] || ffmpeg -y -loglevel error -i "$VID" -ar 16000 -ac 1 -c:a pcm_s16le "$WAV"
echo "=== [$BASE] whisper large-v3-turbo (CUDA) ==="
~/whisper.cpp/build/bin/whisper-cli -m ~/whisper.cpp/models/ggml-large-v3-turbo.bin \
  -f "$WAV" -l th -oj -ojf -of "$TMP/$BASE" -np 2>&1 | grep -vE "^\s*$" | tail -3
echo "=== [$BASE] building markdown ==="
python3 "$ROOT/scripts/md_from_json.py" "$TMP/$BASE.json" "$OUT/$BASE.md" "$BASE" "$BASE.mp4"
echo "=== [$BASE] DONE ==="
