import json
import os
from helpers.quict_sort import quicksort
from enum import Enum


class Column(Enum):
    NIM = 'nim'
    NAME = 'name'
    PLACE_DATE_BIRTH = 'place_date_birth'
    MAJOR = 'major'
    YEAR = 'year'


def getListData() -> set:
    script_dir = os.path.dirname(__file__)
    rel_path = 'data.json'

    f = open(os.path.join(script_dir, rel_path))
    data = json.load(f)["colleger"]

    f.close()
    return data


def addData(new_data) -> None:
    script_dir = os.path.dirname(__file__)
    rel_path = 'data.json'

    with open(os.path.join(script_dir, rel_path)) as file:
        data = json.load(file)

    data["colleger"].append(new_data)
    print(data)

    with open(os.path.join(script_dir, rel_path), 'r+') as file:
        file.seek(0)
        json.dump(data, file, indent=4)


def sortData(column: Column) -> list:
    return quicksort(getListData(), column.value)
