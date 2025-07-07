#!/usr/bin/env python3
# partition_to_parquet.py

import dask.dataframe as dd
from pathlib import Path
import logging

def main():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    log = logging.getLogger()

    # ----------------------------------------------------------------
    # Proje kök dizini (km-stat-activity)
    # script: analysis/scripts/partitioning/partition_to_parquet.py
    # parents[0] = .../partition_to_parquet.py
    # parents[1] = .../partitioning
    # parents[2] = .../scripts
    # parents[3] = .../analysis
    # parents[4] = .../km-stat-activity  <-- istediğimiz
    PROJECT_ROOT = Path(__file__).resolve().parents[4]

    # CSV dosyalarının bulunduğu desen
    CSV_GLOB = PROJECT_ROOT /"km-stat-activity" / "data" / "fake" / "*-f" / "fake_data_*.csv"

    # Parquet’in yazılacağı dizin
    OUT_DIR = PROJECT_ROOT /"km-stat-activity" / "parquet_dataset"
    
 
    OUT_DIR.mkdir(exist_ok=True)

    log.info(f"Reading CSVs from {CSV_GLOB}")
    # Dask DataFrame ile CSV’leri oku
    ddf = dd.read_csv(
        str(CSV_GLOB),
        assume_missing=True,
        dtype={"profile_guid": "object", "date": "object"}
    )

    log.info(f"Writing partitioned Parquet dataset to {OUT_DIR} …")
    ddf.to_parquet(
        str(OUT_DIR),
        engine="pyarrow",
        partition_on=["date", "profile_guid"],
        write_index=False
    )

    log.info("Done.")

if __name__ == "__main__":
    main()
