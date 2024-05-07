from data.data import sort_data, Column
from helpers import quict_sort, directory
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
    except_column = [Column.PLACE_BIRTH, Column.DATE_BIRTH]

    match user_input:
        case "1": sorted_data = sort_data(Column.NIM, quict_sort.Sort.ASC, except_column)
        case "2": sorted_data = sort_data(Column.NAME, quict_sort.Sort.ASC, except_column)
        case "3": sorted_data = sort_data(Column.MAJOR, quict_sort.Sort.ASC, except_column)
        case "4": sorted_data = sort_data(Column.YEAR, quict_sort.Sort.ASC, except_column)
        case "5": return None
        
    if sorted_data == None:
        raise ValueError("Inputan tidak valid")

    headers = ["NIM", "Nama", "Program Studi", "Tahun Masuk"]
    sorted_data = directory.directory_list_to_list(sorted_data)
    print(tabulate(sorted_data, headers=headers, tablefmt="heavy_outline"))
    input()

