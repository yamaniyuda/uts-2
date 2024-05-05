from data.data import getListData
from tabulate import tabulate

def main() -> None:
  table = tabulate(getListData(), headers="keys", tablefmt="heavy_outline")
  print(table)
  input()
  return None