import apps.add_menu
import apps.main_menu
import apps.search_menu
import apps.show_data_menu
import apps.sort_menu
import apps.update_menu
import helpers.colors
import os


def initial() -> None:
    root_menu: str = None
    while True:
        try:
            match root_menu:
                case '1': root_menu = apps.add_menu.main()
                case '2': root_menu = apps.show_data_menu.main()
                case '3': root_menu = apps.update_menu.main()
                case '4': root_menu = apps.sort_menu.main()
                case '5': root_menu = apps.search_menu.main()
                case '6': break
                case  _ : root_menu = apps.main_menu.main()

        except ValueError as error:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{helpers.colors.colors.WARNING} Terjadi Kesalahan: {helpers.colors.colors.ENDC} {error}")
            input()

        finally:
            os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    initial()
