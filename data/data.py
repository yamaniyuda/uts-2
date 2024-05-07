import json
import os
from helpers import binary_search, quict_sort, default_value
from enum import Enum


class Column(Enum):
    NIM = "nim"
    NAME = "name"
    PLACE_DATE_BIRTH = "place_date_birth"
    MAJOR = "major"
    YEAR = "year"


class SearchBy(Enum):
    INDEX = "index"
    VALUE = "value"
    INDEX_VALUE = "index_value"


def get_list_data() -> set:
    script_dir = os.path.dirname(__file__)
    rel_path = "data.json"

    f = open(os.path.join(script_dir, rel_path))
    data = json.load(f)["colleger"]

    f.close()
    return data


def add_data(new_data) -> None:
    script_dir = os.path.dirname(__file__)
    rel_path = "data.json"

    with open(os.path.join(script_dir, rel_path)) as file:
        data = json.load(file)

    if len(search_data(Column.NIM, new_data["nim"])) > 0:
        raise ValueError("Data NIM telah ada, gunakan NIM yang lain")

    data["colleger"].append(new_data)

    with open(os.path.join(script_dir, rel_path), "r+") as file:
        file.seek(0)
        json.dump(data, file, indent=4)

    with open(os.path.join(script_dir, rel_path)) as file:
        data = json.load(file)

    data["colleger"] = sort_data(Column.YEAR, quict_sort.Sort.DSC)

    with open(os.path.join(script_dir, rel_path), "r+") as file:
        file.truncate(0)
        file.seek(0)
        json.dump(data, file, indent=4)


def update_data(index, value):
    script_dir = os.path.dirname(__file__)
    rel_path = "data.json"

    data = sort_data(Column.NIM)
    data[index] = value

    with open(os.path.join(script_dir, rel_path)) as file:
        data_source = json.load(file)

    data_source["colleger"] = data

    with open(os.path.join(script_dir, rel_path), "r+") as file:
        file.truncate(0)
        file.seek(0)
        json.dump(data_source, file, indent=4)


def sort_data(column: Column, sort: quict_sort.Sort = quict_sort.Sort.ASC) -> list:
    return quict_sort.quicksort(get_list_data(), column.value, sort)


def search_data(column: Column, value: str, search_by: SearchBy = SearchBy.VALUE):
    sort = sort_data(column)
    result = binary_search.binary_search(sort, value, column.value)

    match search_by:
        case SearchBy.VALUE:
            return result[1]
        case SearchBy.INDEX:
            return result[0]
        case SearchBy.INDEX_VALUE:
            return result
