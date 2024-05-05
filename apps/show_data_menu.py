import data.data
import tabulate

def main() -> str:
  print(tabulate.tabulate(data.data.getListData(), headers="keys", tablefmt="grid"))
  input()
  return ""