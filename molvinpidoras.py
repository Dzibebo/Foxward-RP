import os
import re
from pathlib import Path

def decode_unicode_escapes(text: str) -> str:
    return re.sub(
        r"\\u([0-9a-fA-F]{4})",
        lambda m: chr(int(m.group(1), 16)),
        text
    )

def process_properties_file(file_path: Path) -> None:
    content = file_path.read_text(encoding='utf-8')
    decoded = decode_unicode_escapes(content)
    file_path.write_text(decoded, encoding='utf-8')
    print(f"Processed: {file_path}")

def process_directory(root_dir: Path) -> None:
    for path in root_dir.rglob('*.properties'):
        process_properties_file(path)

if __name__ == '__main__':
    base_dir = Path(r"...")
    if not base_dir.exists():
        print(f"ne nashol: {base_dir}")
    else:
        process_directory(base_dir)
        print("Done")
