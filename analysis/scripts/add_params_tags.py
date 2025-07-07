#!/usr/bin/env python3
import nbformat
from pathlib import Path

# 1) Notebook’ların bulunduğu kök klasör
NOTEBOOK_ROOT = Path("C:/store/git/km-stat-activity/analysis/scripts")

# 2) Alt klasörler ve notebook dosya adları
NOTEBOOK_DIRS = {
    "directional_change":        "calculate_direction.ipynb",
    "bounding_box":              "bounding_box.ipynb",
    "speed":                     "compute_avg_speed_math.ipynb",
    "acceleration":              "compute_avg_acceleration.ipynb",
    "idle_entropy":              "compute_idle_entropy_fixed2.ipynb",
    "linearity":                 "compute_linearity_manual.ipynb",
}

# 3) Tüm notebook dosyalarını güncelle
for subdir, nb_name in NOTEBOOK_DIRS.items():
    nb_path = NOTEBOOK_ROOT / subdir / nb_name
    if not nb_path.exists():
        print(f"⚠ Notebook bulunamadı: {nb_path}")
        continue

    nb = nbformat.read(str(nb_path), as_version=4)
    if not nb.cells:
        continue

    cell = nb.cells[0]
    lines = cell.source.splitlines()

    # a) Eğer direktif yoksa ekle
    if not any(l.strip().startswith("# papermill: parameters") for l in lines):
        new_lines = []
        for l in lines:
            new_lines.append(l)
            if l.strip().startswith("# Parameters"):
                new_lines.append("# papermill: parameters")
        cell.source = "\n".join(new_lines)

    # b) Metadata tags içine 'parameters' ekle
    tags = cell.metadata.get("tags", [])
    if "parameters" not in tags:
        tags.append("parameters")
        cell.metadata["tags"] = tags

    # 4) Notebook’u tekrar yaz
    nbformat.write(nb, str(nb_path))
    print(f"✅ Etiket eklendi: {nb_path}")
