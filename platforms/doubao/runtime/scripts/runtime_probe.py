#!/usr/bin/env python3
import json, shutil, sys, importlib.util, platform

def status(cmd):
    return "VERIFIED" if shutil.which(cmd) else "UNKNOWN"

out = {
    "python": {"status": "VERIFIED", "version": sys.version.split()[0]},
    "platform": platform.platform(),
    "ffmpeg": {"status": status("ffmpeg")},
    "magick": {"status": status("magick")},
    "convert": {"status": status("convert")},
    "pillow": {"status": "VERIFIED" if importlib.util.find_spec("PIL") else "UNKNOWN"},
    "pyyaml": {"status": "VERIFIED" if importlib.util.find_spec("yaml") else "UNKNOWN"},
}
print(json.dumps(out, ensure_ascii=False, indent=2))
