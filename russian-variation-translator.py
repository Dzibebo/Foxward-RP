import json
import os

file_path = r"location_to_file.json"

def toggle_first_char(s: str) -> str:
    if not s:
        return s
    first, rest = s[0], s[1:]
    if first.islower():
        return first.upper() + rest
    else:
        return first.lower() + rest

if not os.path.isfile(file_path):
    raise FileNotFoundError(f"Файл не найден: {file_path}")

with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

special = data.get('parameters', {}).get('specialNames')
if special is None:
    raise KeyError("В файле отсутствует ключ 'parameters.specialNames'")

new_special = {}
for key, value in special.items():
    new_key = toggle_first_char(key)
    new_special[new_key] = value

data['parameters']['specialNames'] = new_special

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Обновлено {len(new_special)} записей в 'specialNames' файла {file_path}")