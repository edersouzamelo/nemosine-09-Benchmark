import csv
from pathlib import Path
from datetime import datetime

CSV_PATH = Path("runs.csv")


def log_run(summary: dict) -> None:
    file_exists = CSV_PATH.exists()

    with open(CSV_PATH, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "timestamp",
                "runs",
                "mean",
                "stdev",
                "min",
                "max",
                "failure_rate",
            ],
        )

        if not file_exists:
            writer.writeheader()

        writer.writerow(
            {
                "timestamp": datetime.utcnow().isoformat(),
                "runs": summary["n"],
                "mean": summary["mean"],
                "stdev": summary["stdev"],
                "min": summary["min"],
                "max": summary["max"],
                "failure_rate": summary["failure_rate"],
            }
        )


