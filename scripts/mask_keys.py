# scripts/mask_keys.py
import re
from pathlib import Path

# Mask secrets in .env files
env_file = Path('.env')
if env_file.exists():
    content = env_file.read_text()
    # Mask anything that looks like a key (split for PEP8)
    content = re.sub(
        r'(=)[^\s]+',
        r'\1******',
        content
    )
    env_file.write_text(content)
