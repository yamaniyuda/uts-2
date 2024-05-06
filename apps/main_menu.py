def display_menu():
    print ("="*45)
    print("Aplikasi Data Mahasiswa")
    print ("="*45)
    print("1. Tambah Data Mahasiswa")
    print("2. Tampilkan Data Mahasiswa")
    print("3. Ubah Data Mahasiswa")
    print("4. Urutkan Data Mahasiswa")
    print("5. Cari Data Mahasiswa")
    print("6. Keluar")
    print ("="*45)
    print()

def main() -> str:
    display_menu()
    user_input = input("Masukkan pilihan menu [1-6]: ")
    if user_input in ("1", "2", "3", "4", "5", "6"):
        return user_input
    else:
        print("Input tidak valid. Harap masukkan angka 1-6.")
        return main()

if __name__ == "__main__":
    user_choice = main()
    print("Pilihan pengguna:", user_choice)
