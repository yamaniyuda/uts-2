from data import data  
from tabulate import tabulate

def display_menu():
    print("Urutan Data Mahasiswa")
    print("1. NIM ")
    print("2. Nama")
    print()


def main() -> str:
    display_menu()
    user_input = input("Pilih opsi urutan [1-2]: ")

    if user_input == "1":
        nim = input("Masukkan NIM: ")
        result = data.search_data(data.Column.NIM, nim)  
    elif user_input == "2":
        name = input("Masukkan Nama: ")
        result = data.search_data(data.Column.NAME, name)
    else:
        raise ValueError("Inputan tidak valid")

    if not result:
        print("Data tidak ditemukan.")
        return main()

    table = tabulate(result, headers="keys", tablefmt="heavy_outline")
    print(table)
    input("Tekan Enter untuk melanjutkan...")
    return ""

