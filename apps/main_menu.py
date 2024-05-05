def display_menu():
    print("Aplikasi Data Mahasiswa")
    print("1. Tambah Data Mahasiswa")
    print("2. Tampilkan Data Mahasiswa")
    print("3. Ubah Data Mahasiswa")
    print("4. Urutkan Data Mahasiswa")
    print("5. Cari Data Mahasiswa")
    print("6. Keluar")
    print()

def main() ->str:
    while True:
        display_menu()
        user_input = input("Masukkan pilihan menu [1-6]: ")
        if user_input == "1":
            print("Tambah Data Mahasiswa")
        elif user_input == "2":
            print("Tampilkan Data Mahasiswa")
        elif user_input == "3":
            print("Ubah Data Mahasiswa")
        elif user_input == "4":
            print("Urutkan Data Mahasiswa")
        elif user_input == "5":
            print("Cari Data Mahasiswa")
        elif user_input == "6":
            print("Keluar")
            break
        else:
            print("Input tidak valid. Harap masukkan angka 1-6.")
        print()

if __name__ == "__main__":
    main()


  