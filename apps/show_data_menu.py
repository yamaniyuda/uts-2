from data.data import get_list_data
from tabulate import tabulate

def main() -> None:
  table = tabulate(get_list_data(), headers="keys", tablefmt="heavy_outline")
  print(table)
  input()
  return None