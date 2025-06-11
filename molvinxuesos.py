import os
import re

def process_line(line):
    if not line.startswith("nbt.display.Name="):
        return line

    m = re.match(r"^(nbt\.display\.Name)=(i(pattern|regex):)(.*)$", line)
    if not m:
        return line + "\n"

    prefix = m.group(1)
    content = m.group(4)

    content = content.strip('*')

    if content.startswith('(') and content.endswith(')'):
        inner = content[1:-1]
        parts = inner.split('|')
        keep = []
        for p in parts:
            if re.match(r"^(?:\\u[0-9A-Fa-f]{4})+.*", p):
                keep.append(p)
            elif not p.isascii() or not p.isalpha():
                keep.append(p)
        if not keep and parts:
            keep = [parts[0]]
        content = keep[0]

    new_line = f"{prefix}={content}\n"
    return new_line


def process_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    modified = False
    new_lines = []
    for line in lines:
        new = process_line(line)
        if new != line:
            modified = True
        new_lines.append(new)

    if modified:
        with open(path, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
        print(f"Updated: {path}")


def run(folder):
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.lower().endswith('.properties'):
                process_file(os.path.join(root, file))


if __name__ == '__main__':
    target_folder = r"C:\Users\dzibebo\Desktop\Foxward-RP\assets\minecraft\optifine\cit"
    run(target_folder)
