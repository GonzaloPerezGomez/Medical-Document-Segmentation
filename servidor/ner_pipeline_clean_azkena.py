#!/usr/bin/env python3
import argparse
import logging
import re
from pathlib import Path

import pandas as pd
import yaml
from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline

# Patrón para líneas de entidad:
ENTITY_RE = re.compile(r'^(T\d+)\t(\S+\s+\d+\s+\d+)\t?(.*)$')


def get_column_names_from_excel(excel_path: Path):
    """Lee la primera hoja de excel con header=1 y devuelve lista de nombres de columnas."""
    df = pd.read_excel(excel_path, header=2)
    # Limpiar espacios y devolver nombres de columnas reales
    return [str(col).strip() for col in df.columns]



def load_config(path):
    with open(path, "r") as f:
        cfg = yaml.safe_load(f)
    models = cfg.get("models")
    defaults = cfg.get("defaults", {})
    sep = defaults.get("text_separator", "\n")
    skip_empty = defaults.get("skip_empty", True)
    return models, sep, skip_empty


def load_pipelines(models: list):
    logging.info("Cargando modelos y tokenizadores NER...")
    pipes = {}
    for idx, model in enumerate(models):
        model_path: str = model["model_name_or_path"]
        task = model.get("task", "ner")
        logging.info(f"  - Modelo {idx}: {model_path} ({task})")
        tokenizer = AutoTokenizer.from_pretrained(model_path, use_fast=True)
        model = AutoModelForTokenClassification.from_pretrained(model_path)
        pipes[idx] = pipeline(
            task,
            model=model,
            tokenizer=tokenizer,
            grouped_entities=True,
            aggregation_strategy="simple",
        )
    return pipes


def process_file(path_txt: Path, pipelines, models, sep, skip_empty, out_dir: Path):
    # Leer datos con encabezado en la segunda fila para inferencia NER
    with open(path_txt, "r") as txt:
        name = txt.name.split("/")[-1].split(".txt")[0]
        base = txt.read()
        print("Base: ", base)
        print("Name: ", name)
    #df.columns = df.columns.str.strip()
    #base = path_txt.stem
    ann_path = out_dir / f"{name}.ann"
    # Obtener nombres reales de columnas
    #excel_cols = get_column_names_from_excel(path_txt)

    ent_counter = 1
    with open(ann_path, 'w', encoding='utf-8') as ann_f:
        for idx, params in enumerate(models):
            #if idx >= len(excel_cols):
            #    logging.warning(f"{base}: la columna {idx} no existe, se salta.")
            #    continue

            #col_name = excel_cols[idx]
            # Saltar columnas vacías o sin nombre
            #if not col_name or col_name.lower().startswith('unnamed'):
            #    logging.info(f"{base}: columna {idx} sin nombre real ('{col_name}') → saltada")
            #    continue

            #series = df.iloc[:, idx].dropna().astype(str).str.strip()
            #texts = [t for t in series if t]
            
            #if skip_empty and not texts:
            #   logging.info(f"{base}: columna {idx} ('{col_name}') vacía → saltada")
            #    continue

            #full_text = sep.join(texts)
            #ann_f.write(f"# Column {idx}: {col_name}\n")
            chuncks = base.split(sep)
            for sec in chuncks:
                entities = pipelines[idx](sec)
                for ent in entities:
                    start, end = ent['start'], ent['end']
                    label = ent.get('entity_group', ent.get('entity'))
                    text = ent['word']
                    ann_f.write(f"T{ent_counter}\t{label} {start} {end}\t{text}\n")
                    ent_counter += 1

    logging.info(f"→ generado {ann_path}")


def clean_ann_file(input_path: Path, output_path: Path, excel_cols):
    lines = input_path.read_text(encoding='utf-8').splitlines()
    cleaned = []
    i = 0
    while i < len(lines):
        line = lines[i].rstrip('\n')
        if not line.strip():
            i += 1
            continue
        if line.startswith('#'):
            mcol = re.match(r'# Column (\d+):', line)
            if mcol:
                idx = int(mcol.group(1))
                # Obtener nombre real
                name = excel_cols[idx] if idx < len(excel_cols) else str(idx)
                if not name or name.lower().startswith('unnamed'):
                    i += 1
                    continue
                cleaned.append(f"# Column {idx}: {name}")
            else:
                cleaned.append(line)
            i += 1
            continue
        m = ENTITY_RE.match(line)
        if m:
            tid, span, text = m.groups()
            text = text.strip()
            if not text and i + 1 < len(lines):
                next_line = lines[i+1].strip()
                if not next_line.startswith('T') and not next_line.startswith('#'):
                    text = next_line
                    i += 1
            if not text:
                i += 1
                continue
            cleaned.append(f"{tid}\t{span}\t{text}")
        i += 1
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(cleaned) + "\n", encoding='utf-8')
    print(f"[+] {input_path.name} → {output_path.name}: {len(cleaned)} líneas escritas")


def main():
    parser = argparse.ArgumentParser(description="NER pipeline y limpieza .ann con columnas desde txt")
    parser.add_argument("--input-dir", "-i", required=True, help="Carpeta con .txt y .ann originales")
    parser.add_argument("--config", "-c", required=True, help="Fichero YAML de configuración")
    parser.add_argument("--output-dir", "-o", required=True, help="Carpeta donde se guardarán los .ann finales")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    input_dir = Path(args.input_dir).resolve()
    config_path = Path(args.config).resolve()
    output_dir = Path(args.output_dir).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)


    models, sep, skip_empty = load_config(config_path)
    pipelines = load_pipelines(models)

    # Procesar Excels y generar .ann inicial
    for txt in sorted(input_dir.glob("*.txt")):
        logging.info(f"Procesando {txt.name} …")
        process_file(txt, pipelines, models, sep, skip_empty, output_dir)

    # Limpiar y renombrar .ann
    """for ann_path in sorted(output_dir.glob("*.ann")):
        stem = ann_path.stem
        excel_path = input_dir / f"{stem}.txt"
        if not excel_path.exists():
            logging.warning(f"No se encontró Excel para {stem}, saltando limpieza")
            continue
        excel_cols = get_column_names_from_excel(excel_path)
        clean_name = f"{stem}_clean.ann"
        clean_path = output_dir / clean_name
        clean_ann_file(ann_path, clean_path, excel_cols)"""

if __name__ == "__main__":
    main()




