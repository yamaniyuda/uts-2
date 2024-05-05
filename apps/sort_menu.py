from data.data import sortData, Column
from tabulate import tabulate

def display_menu():
    print("Aplikasi Data Mahasiswa")
    print("1. NIM ")
    print("2. Nama")
    print("3. Program Studi")
    print("4. Tahun Masuk")
    print("5. Keluar")
    print()

def main() -> str:
    display_menu()
    user_input = input(" Jenis pengurutan (Masukkan angka) [1-5] : ")
    if user_input in ("1", "2", "3", "4", "5"):
        # Melakukan pengurutan data berdasarkan pilihan pengguna
        if user_input == "1":
            sorted_data = sortData(Column.NIM)
        elif user_input == "2":
            sorted_data = sortData(Column.NAME)
        elif user_input == "3":
            sorted_data = sortData(Column.MAJOR)
        elif user_input == "4":
            sorted_data = sortData(Column.YEAR)
        else:
            print("Keluar")
            return user_input

        # Cetak data yang sudah diurutkan
        print(tabulate(sorted_data, headers="keys", tablefmt="heavy_outline"))
        input()
    else:
        print("Input tidak valid. Harap masukkan angka 1-5.")
        return main()
