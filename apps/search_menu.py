from data import data
from tabulate import tabulate


def main() -> str:
  result = data.searchData(data.Column.NAME, 'ahmad')
  table = tabulate(result, headers="keys", tablefmt="heavy_outline")
  
  print(table)
  input()
  return "" 