import data.data
import tabulate

def main() -> None:
  print(tabulate.tabulate(data.data.getListData(), headers="keys", tablefmt="grid"))
  input()
  return None