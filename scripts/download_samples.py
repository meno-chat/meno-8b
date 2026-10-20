"""Download the 30 public TutorBench samples (format reference only, never for training)."""
from datasets import load_dataset

ds = load_dataset("tutorbench/tutorbench")
print(ds)
for split in ds:
    ds[split].to_json(f"data/tutorbench_public_{split}.jsonl")
    print(f"saved {split}: {len(ds[split])} rows")
