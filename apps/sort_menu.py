import data.data
import tabulate


def main() -> str:
  print(tabulate.tabulate(data.data.sortData(data.data.Column.YEAR), headers="keys", tablefmt="grid"))

  input()
  return ""