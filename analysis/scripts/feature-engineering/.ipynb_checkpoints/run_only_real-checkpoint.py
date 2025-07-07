#!/usr/bin/env python3
import papermill as pm
from pathlib import Path
import logging

def main():
    # Logger kurulumu
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")
    log = logging.getLogger()

    # Kök dizin ve klasör ayarları
    BASE_DIR     = Path(__file__).resolve().parents[3]
    NOTEBOOK_DIR = BASE_DIR / "analysis" / "scripts"
    THIS_DIR     = NOTEBOOK_DIR / "feature-engineering"
    REAL_DIR     = BASE_DIR / "data" / "real"
    RUNS_DIR     = THIS_DIR / "runs"
    RUNS_DIR.mkdir(exist_ok=True)

    # Sadece işlem yapılacak 5 gün
    REAL_DATES = ["20250421", "20250422", "20250423", "20250424", "20250425"]

    # Kullanılacak notebooklar (sıralı olarak)
    NOTEBOOKS = [
        "directional_change/calculate_direction_with_full_df_real.ipynb",
        "bounding_box/bounding_box_fixed_loading_and_saving_real.ipynb",
        "speed/compute_avg_speed_math_with_full_df_real.ipynb",
        "acceleration/compute_avg_acceleration_with_full_df_real.ipynb",
        "idle_entropy/compute_idle_entropy_fixed2_with_full_df_real.ipynb",
        "linearity/compute_linearity_manual_with_full_df_real.ipynb",
    ]

    # Her gün için işlem yap
    for date in REAL_DATES:
        input_filename  = f"km_stat_nature_{date}_le120s_fixed_brackets.csv"
        output_filename = f"km_stat_nature_{date}_le120s_fixed_brackets_processed.csv"

        csv_path    = REAL_DIR / input_filename
        output_path = REAL_DIR / output_filename

        log.info(f"[REAL-NATURE] {date}: input={csv_path} → output={output_path}")

        for nb in NOTEBOOKS:
            full_nb = NOTEBOOK_DIR / nb
            run_nb  = RUNS_DIR / f"real_nature_{date}_{Path(nb).stem}.ipynb"
            log.info(f"    → Executing {full_nb.name} → {run_nb.name}")

            pm.execute_notebook(
                input_path   = str(full_nb),
                output_path  = str(run_nb),
                parameters   = {
                    "mode": "real",
                    "input_path": str(csv_path),
                    "output_path": str(output_path),
                },
                log_output=True
            )

        log.info(f"[REAL-NATURE] {date} tamamlandı.\n")

if __name__ == "__main__":
    main()
