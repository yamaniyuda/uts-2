from data.data import get_list_data, Column
from tabulate import tabulate
from helpers import directory

def main() -> None:
  data_source = get_list_data([Column.PLACE_BIRTH, Column.DATE_BIRTH])
  data_source = directory.directory_list_to_list(data_source)
  headers = ["NIM", "Nama", "Program Studi", "Tahun Masuk"]
  
  table = tabulate(data_source, headers=headers, tablefmt="heavy_outline")
  print(table)
  input()
  return None