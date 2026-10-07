"""
Monta o dataset mínimo da Fase 6 a partir do Open Images V7.

Objetivo:
- 40 imagens contendo Pessoa (Person) e sem Car
- 40 imagens contendo Car e sem Person
- splits 32/4/4 por classe
- rótulos em formato YOLO: pessoa=0, carro=1

Depois do download, revise visualmente TODAS as caixas e as licenças/origens
antes da entrega. O script não inventa resultados de treinamento.
"""

from pathlib import Path
import argparse
import csv
import random
import shutil

import fiftyone as fo
import fiftyone.zoo as foz

TARGETS = {"Person": 0, "Car": 1}
PT_NAMES = {"Person": "pessoa", "Car": "carro"}
SPLITS = [("train", 32), ("val", 4), ("test", 4)]


def safe_image_id(sample):
    for field in ("open_images_id", "image_id"):
        if sample.has_field(field):
            value = sample.get_field(field)
            if value:
                return str(value)
    return Path(sample.filepath).stem


def only_one_target(sample):
    detections = sample.detections.detections if sample.detections else []
    present = {d.label for d in detections if d.label in TARGETS}
    if present == {"Person"}:
        return "Person"
    if present == {"Car"}:
        return "Car"
    return None


def yolo_lines(sample, target):
    rows = []
    for det in sample.detections.detections:
        if det.label != target:
            continue
        x, y, w, h = det.bounding_box
        cx = x + w / 2
        cy = y + h / 2
        rows.append(f"{TARGETS[target]} {cx:.6f} {cy:.6f} {w:.6f} {h:.6f}")
    return rows


def ensure_dirs(base):
    for split, _ in SPLITS:
        (base / "images" / split).mkdir(parents=True, exist_ok=True)
        (base / "labels" / split).mkdir(parents=True, exist_ok=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--saida", default="FarmTech_Fase6/dataset")
    parser.add_argument("--candidatas", type=int, default=600)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    out = Path(args.saida).resolve()
    ensure_dirs(out)

    print("Baixando candidatas do Open Images V7...")
    dataset = foz.load_zoo_dataset(
        "open-images-v7",
        split="train",
        label_types=["detections"],
        classes=["Person", "Car"],
        max_samples=args.candidatas,
        shuffle=True,
        seed=args.seed,
    )

    pools = {"Person": [], "Car": []}
    for sample in dataset:
        target = only_one_target(sample)
        if target is None:
            continue
        labels = yolo_lines(sample, target)
        if not labels:
            continue
        pools[target].append((sample, labels))

    for target in pools:
        if len(pools[target]) < 40:
            raise RuntimeError(
                f"Foram encontradas apenas {len(pools[target])} imagens válidas de {target}. "
                "Rode novamente aumentando --candidatas, por exemplo para 1200."
            )

    rng = random.Random(args.seed)
    for target in pools:
        rng.shuffle(pools[target])
        pools[target] = pools[target][:40]

    manifest = []
    for target in ("Person", "Car"):
        cursor = 0
        seq = 1
        for split, amount in SPLITS:
            for sample, labels in pools[target][cursor:cursor + amount]:
                ext = Path(sample.filepath).suffix.lower() or ".jpg"
                name = f"{PT_NAMES[target]}_{seq:03d}{ext}"
                img_dst = out / "images" / split / name
                lbl_dst = out / "labels" / split / f"{Path(name).stem}.txt"

                shutil.copy2(sample.filepath, img_dst)
                lbl_dst.write_text("\n".join(labels) + "\n", encoding="utf-8")

                manifest.append({
                    "arquivo": name,
                    "classe": PT_NAMES[target],
                    "split": split,
                    "origem_url_ou_autoria": f"Open Images V7 image_id={safe_image_id(sample)}",
                    "licenca_ou_permissao": "VERIFICAR metadados/licenca da imagem antes da entrega",
                    "cena_id": safe_image_id(sample),
                })
                seq += 1
            cursor += amount

    fontes = out.parent / "fontes_openimages.csv"
    with fontes.open("w", newline="", encoding="utf-8") as fp:
        writer = csv.DictWriter(
            fp,
            fieldnames=[
                "arquivo", "classe", "split", "origem_url_ou_autoria",
                "licenca_ou_permissao", "cena_id"
            ],
        )
        writer.writeheader()
        writer.writerows(manifest)

    print(f"Dataset criado em: {out}")
    print("Esperado: 64 treino, 8 validacao, 8 teste.")
    print(f"Fontes preliminares: {fontes}")
    print("IMPORTANTE: revisar caixas, cenas e licencas antes de executar o notebook.")


if __name__ == "__main__":
    main()
