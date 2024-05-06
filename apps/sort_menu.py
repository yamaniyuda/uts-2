from data.data import sort_data, Column
from tabulate import tabulate


def display_menu():
    print(" Data Mahasiswa")
    print("1. NIM ")
    print("2. Nama")
    print("3. Program Studi")
    print("4. Tahun Masuk")
    print("5. Keluar")
    print()


def main() -> str:
    display_menu()
    user_input = input(" Jenis pengurutan (Masukkan angka) [1-5] : ")
    sorted_data = None

    match user_input:
        case "1": sorted_data = sort_data(Column.NIM)
        case "2": sorted_data = sort_data(Column.NAME)
        case "3": sorted_data = sort_data(Column.MAJOR)
        case "4": sorted_data = sort_data(Column.YEAR)
        case "5": return None
        
    if sorted_data == None:
        raise ValueError("Inputan tidak valid")

    # header = ["No", "NIM", "Nama", "Tempat Lahir"]
    print(tabulate(sorted_data, headers="keys", tablefmt="heavy_outline"))
    input()

