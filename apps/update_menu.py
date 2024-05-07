from data import data
from tabulate import tabulate
from helpers import directory
from helpers.default_value import default_value


def update_data_feature(data_source):
  print("Note: Kosongkan Jika Tidak Ingin Diubah")

  name = input("{:<30}:".format("Nama") + " ")
  place_birth = input("{:<30}:".format("Tempat lahir") + " ")
  date_birth = input("{:<30}:".format("Tanggal lahir (dd/mm/yyyy)") + " ")
  major = input("{:<30}:".format("Program Study") + " ")
  year = input("{:<30}:".format("Tahun Masuk") + " ")

  prev_data = data_source[1][0]

  data_update = {
    "nim": prev_data["nim"],
    "name": default_value(prev_data["name"], name, lambda n: n.lower()),
    "date_birth": default_value(prev_data["date_birth"], date_birth, lambda n: n.lower()),
    "place_birth": default_value(prev_data["place_birth"], place_birth, lambda n: n.lower()),
    "major": default_value(prev_data["major"], major, lambda n: n.lower()),
    "year": default_value(prev_data["year"], year, lambda n: n.lower()),
  }

  data.update_data(data_source[0][0], data_update)



def main() -> str:
  nim = input("NIM mahasiswa yang akan diubah: ")

  find_data = data.search_data(data.Column.NIM, nim, data.SearchBy.INDEX_VALUE)
  keys = ["NIM", "Nama", "Tempat Lahir", "Tanggal Lahir", "Program Studi", "Tahun Masuk"]
  rebuild_data = directory.directory_key_values_list(find_data[1][0], keys)

  table = tabulate(rebuild_data, headers=["Field", "Detail"], tablefmt="heavy_outline")
  print(table)
  input()

  update_data_feature(find_data)

  return ""