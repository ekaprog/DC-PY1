import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(file) -> list[dict]:
    delimiter = ','
    with open(file, 'r') as f:
        csv_data = f.readlines()
    headers = csv_data[0].rstrip().split(sep=delimiter)
    rows = [row.rstrip().split(sep=delimiter) for row in csv_data[1:]]
    list_ = []
    for row in rows:
        dict_ = {headers[i]: row[i] for i in range(len(headers))}
        list_.append(dict_)

    return list_


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
