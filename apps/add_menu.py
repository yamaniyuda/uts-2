import data.data
from helpers.check_data_not_null import check_data_not_null


def add_feture_handle() -> None:
  nim = input("{:<30}:".format("Nim") + " ")
  name = input("{:<30}:".format("Nama") + " ")
  place_birth = input("{:<30}:".format("Tempat lahir") + " ")
  date_birth = input("{:<30}:".format("Tanggal lahir (dd/mm/yyyy)") + " ")
  major = input("{:<30}:".format("Program Study") + " ")
  year = input("{:<30}:".format("Tahun Masuk") + " ")

  validate = check_data_not_null(nim, name, place_birth, date_birth, major, year)

  if not validate:
    raise ValueError("Semua field inputan wajib diisi")

  data.data.add_data({
    "nim": nim.lower(),
    "name": name.lower(),
    "date_birth": date_birth.lower(),
    "place_birth": place_birth.lower(),
    "major": major.lower(),
    "year": year.lower()
  })

  
  return None
  


def main() -> str:
  print("="*60)
  print("Tambah Data Mahasiswa")
  print("="*60)

  return add_feture_handle()