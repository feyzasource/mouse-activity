import papermill as pm
from pathlib import Path

base_path = Path("C:/store/git/km-stat-activity/data/real/")
notebook_path = Path("C:/store/git/km-stat-activity/analysis/scripts/feature-engineering/real_feature_extraction.ipynb")
output_dir = Path("C:/store/git/km-stat-activity/data/real/processed")

output_dir.mkdir(exist_ok=True)

for day in range(20250421, 20250426):
    input_file = base_path / f"km_stat_nature_{day}.csv"
    output_file = base_path / f"km_stat_nature_{day}_features.csv"
    log_file = output_dir / f"run_{day}.ipynb"

    if input_file.exists():
        print(f"📘 Executing notebook for: {day}")
        pm.execute_notebook(
            input_path=str(notebook_path),
            output_path=str(log_file),
            parameters=dict(
                input_path=str(input_file),
                output_path=str(output_file)
            )
        )
    else:
        print(f"❌ Missing file: {input_file}")
