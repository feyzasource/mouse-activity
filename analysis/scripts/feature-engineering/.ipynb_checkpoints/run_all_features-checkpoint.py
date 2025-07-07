 #!/usr/bin/env python3
import papermill as pm
from pathlib import Path
import logging
from urllib.parse import quote

def main():
    # ── Logger kurulumu ─────────────────────────────────────────────────────────
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")
    log = logging.getLogger()

    # ── Proje kök dizini (km-stat-activity) ──────────────────────────────────────
    BASE_DIR = Path(__file__).resolve().parents[3]

    # ── Notebook klasörü ─────────────────────────────────────────────────────────
    THIS_DIR     = BASE_DIR / "analysis" / "scripts" / "feature-engineering"
    NOTEBOOK_DIR = BASE_DIR / "analysis" / "scripts"

    # ── Çalıştırılacak notebook’lar ───────────────────────────────────────────────
    NOTEBOOKS = [
        "directional_change/calculate_direction_with_full_df.ipynb",
        "bounding_box/bounding_box_fixed_loading_and_saving.ipynb",
        "speed/compute_avg_speed_math_with_full_df.ipynb",
        "acceleration/compute_avg_acceleration_with_full_df.ipynb",
        "idle_entropy/compute_idle_entropy_fixed2_with_full_df.ipynb",
        "linearity/compute_linearity_manual_with_full_df.ipynb",
    ]


    # ── FAKE pipeline ayarları ───────────────────────────────────────────────────
    FAKE_DATES   = ["2025-04-21","2025-04-22","2025-04-23","2025-04-24","2025-04-25"]
    PARQUET_ROOT = BASE_DIR / "parquet_dataset"
    OUT_FAKE     = BASE_DIR / "processed" / "fake"
    OUT_FAKE.mkdir(parents=True, exist_ok=True)

    # ── REAL pipeline ayarları ───────────────────────────────────────────────────
    REAL_DIR        = BASE_DIR / "data" / "real"
    OUT_REAL_ACER   = BASE_DIR / "processed" / "real" / "acer"
    OUT_REAL_NATURE = BASE_DIR / "processed" / "real" / "nature"
    OUT_REAL_ACER.mkdir(parents=True, exist_ok=True)
    OUT_REAL_NATURE.mkdir(parents=True, exist_ok=True)

    # ── Runs klasörü ────────────────────────────────────────────────────────────
    RUNS_DIR = THIS_DIR / "runs"
    RUNS_DIR.mkdir(exist_ok=True)

    # ── FAKE pipeline ────────────────────────────────────────────────────────────


    for date in FAKE_DATES:
        date_dir = PARQUET_ROOT / f"date={date}"
        
        for profile_dir in date_dir.glob("profile_guid=*"):
            guid = profile_dir.name.split("=")[-1]  # profile_guid=ABC123 → ABC123
            files = [str(p) for p in profile_dir.glob("*.parquet")]
            
            if not files:
                log.warning(f"[FAKE] {date} {guid}: No parquet files found.")
                continue
            
            # Çıktı yolu: processed/fake/profile_guid=ABC123/2025-04-21-processed.csv
            output_profile_dir = OUT_FAKE / f"profile_guid={quote(guid)}"
            output_profile_dir.mkdir(parents=True, exist_ok=True)
            out_csv = str(output_profile_dir / f"{date}-processed.csv")
    
            log.info(f"[FAKE] {date} - {guid}: {len(files)} parquet files → {out_csv}")
            
            for nb in NOTEBOOKS:
                full_nb = NOTEBOOK_DIR / nb
                run_nb = RUNS_DIR / f"fake_{guid}_{date}_{Path(nb).stem}.ipynb"
                log.info(f"    → Executing {full_nb.name} → {run_nb.name}")
                pm.execute_notebook(
                    input_path=str(full_nb),
                    output_path=str(run_nb),
                    parameters={
                        "mode": "fake",
                        "input_path": files,        # liste halinde .parquet yolları
                        "output_path": out_csv      # her profil için ayrı çıktı
                    },
                    log_output=True
                )
    
            log.info(f"[FAKE] {date} - {guid} tamamlandı.\n")


    # ── REAL pipeline ────────────────────────────────────────────────────────────
    for csv_path in sorted(REAL_DIR.glob("km_stat_*.csv")):
        parts  = csv_path.stem.split("_")    # ["km","stat","acer","YYYYMMDD"]
        prefix = parts[2]                    # "acer" veya "nature"
        date   = parts[3]
        out    = str((OUT_REAL_ACER if prefix=="acer" else OUT_REAL_NATURE)
                     / f"{date}-processed.csv")

        log.info(f"[REAL-{prefix.upper()}] {date}: input={csv_path} → output={out}")
        for nb in NOTEBOOKS:
            full_nb = NOTEBOOK_DIR / nb
            run_nb  = RUNS_DIR / f"real_{prefix}_{date}_{Path(nb).stem}.ipynb"
            log.info(f"    → Executing {full_nb.name} → {run_nb.name}")
            pm.execute_notebook(
                input_path   = str(full_nb),
                output_path  = str(run_nb),
                parameters   = {
                    "mode":        "real",
                    "input_path":  str(csv_path),
                    "output_path": out
                },
                log_output=True
            )
        log.info(f"[REAL-{prefix.upper()}] {date} tamamlandı.\n")


if __name__ == "__main__":
    main()
