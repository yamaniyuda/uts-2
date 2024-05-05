import data.data

from helpers.check_data_null import check_data_null


def add_feture_handle() -> None:
  nim = input("{:<30}:".format("Nim") + " ")
  name = input("{:<30}:".format("Nama") + " ")
  place_birth = input("{:<30}:".format("Tempat lahir") + " ")
  date_birth = input("{:<30}:".format("Tanggal lahir (dd/mm/yyyy)") + " ")
  major = input("{:<30}:".format("Program Study") + " ")
  year = input("{:<30}:".format("Tahun Masuk") + " ")

  check_data_null(nim, name, place_birth, date_birth, major, year)
  

def main() -> str:
  '''
  This function usage for first display
  ret
  '''
  
  print("="*60)
  print("Tambah Data Mahasiswa")
  print("="*60)

  add_feture_handle()
  return ""