def main() -> str:
  '''
  This function usage for first display
  ret
  '''
  
  print(data.data.getListData()[0])
  print(tabulate.tabulate(data.data.getListData(), headers="keys", tablefmt="grid"))

  return ""