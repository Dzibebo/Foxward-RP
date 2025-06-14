import os
import json
import glob

def parse_properties_file(path):
    name = None
    model = None
    texture = None
    with open(path, encoding='utf-8') as f:
        for raw in f:
            line = raw.strip()
            if not line or line.startswith('#') or '=' not in line:
                continue
            key, val = line.split('=', 1)
            key = key.strip()
            val = val.strip()
            if key == 'nbt.display.Name':
                name = val
            elif key == 'model':
                model = val
            elif key == 'texture':
                texture = val
    model_name = model if model is not None else texture
    return name, model_name

def build_special_names(dir_path):
    special = {}
    pattern = os.path.join(dir_path, '*.properties')
    for filepath in glob.glob(pattern):
        name, model = parse_properties_file(filepath)
        if name and model:
            model_name = os.path.basename(model)
            special[name] = model_name
        else:
            print(f'В {filepath} не найдены key=value')
    return special

def main():
    src_dir = r'location_dir'
    out_file = os.path.join(os.path.dirname(src_dir), 'json_name.json')

    data = {
        "type": "custom_name",
        "items": ["minecraft:id", "minecraft:id"],
        "modelPrefix": "item/dir/",
        "modelParent": "minecraft:item/generated",
        "parameters": {
            "nbtPath": ".display.Name",
            "specialNames": build_special_names(src_dir)
        }
    }

    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f'Успешно создан файл: {out_file}')

if __name__ == '__main__':
    main()