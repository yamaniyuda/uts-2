def check_data_not_null(*data) -> bool:
  for dt in data:
    if not dt.strip(): return False
  return True
  