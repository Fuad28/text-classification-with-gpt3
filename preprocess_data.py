import json
import pandas as pd

data = pd.read_csv("spam.csv")


def create_jsonl(dataset: pd.DataFrame, file_name: str) -> None:
    with open(f'{file_name}.jsonl', 'w') as file:
        for row in dataset.itertuples():
            file.write(json.dumps({"prompt": row.Message, 'completion': row.Category})+'\n')
    file.close()


create_jsonl(data, "training.jsonl")