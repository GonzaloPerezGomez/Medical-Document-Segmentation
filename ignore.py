#!/usr/bin/env python3
import argparse
import logging
import re
from pathlib import Path

import pandas as pd
import yaml
from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline

path = Path("./servidor/columns_mapping3.yaml")

with open(path, "r") as f:
    cfg = yaml.safe_load(f)
cols = {int(k): v for k, v in cfg.get("columns", {}).items()}
defaults = cfg.get("defaults", {})
sep = defaults.get("text_separator", "\n\n")
skip_empty = defaults.get("skip_empty", True)

print(f"Default: {defaults}")

logging.info("Cargando modelos y tokenizadores NER...")
pipes = {}
for idx, params in cols.items():
    print(f"Paramas: {params}")
    exit()
    model_path = params.get("models")[idx]["model_name_or_path"]
    task = params.get("task", "ner")
    logging.info(f"  - Columna {idx}: {model_path} ({task})")
    tokenizer = AutoTokenizer.from_pretrained(model_path, use_fast=True)
    model = AutoModelForTokenClassification.from_pretrained(model_path)
    pipes[idx] = pipeline(
        task,
        model=model,
        tokenizer=tokenizer,
        grouped_entities=True,
        aggregation_strategy="simple",
    )