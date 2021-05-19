import json
import argparse


def get_preds_from_json_file(preds_json_file: str, output_preds_txt_file: str) -> None:
    with open(preds_json_file) as inpf, open(output_preds_txt_file, 'w') as outf:
        preds = json.load(inpf)
        for pred in preds:
            query = pred["inferred_code"]
            outf.write(f"{query}\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--preds-json-file", required=True)
    parser.add_argument("--output-preds-txt-file", required=True)
    args = parser.parse_args()

    get_preds_from_json_file(preds_json_file=args.preds_json_file,
                             output_preds_txt_file=args.output_preds_txt_file)
