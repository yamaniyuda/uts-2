from data import data  
from tabulate import tabulate
from helpers import directory

def display_menu():
    print("Urutan Data Mahasiswa")
    print("1. NIM ")
    print("2. Nama")
    print()


def main() -> str:
    display_menu()
    user_input = input("Pilih opsi urutan [1-2]: ")

    match user_input:
        case "1":
            nim = input("Masukkan NIM: ")
            result = data.search_data(data.Column.NIM, nim)
        case "2":
            name = input("Masukkan Nama: ")
            result = data.search_data(data.Column.NAME, name)
        case _ :
            raise ValueError("Inputan tidak valid")

    if not result:
        print("Data tidak ditemukan.")
        return main()

    result = directory.directory_list_to_list(result, True)
    headers = ["No", "NIM", "Nama", "Tempat Lahir", "Tanggal Lahir", "Program Studi", "Tahun Masuk"]
    table = tabulate(result, headers=headers, tablefmt="heavy_outline")
    print(table)
    input("Tekan Enter untuk melanjutkan...")
    return ""

