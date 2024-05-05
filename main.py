import apps.add_menu
import apps.main_menu
import apps.search_menu
import apps.show_data_menu
import apps.sort_menu
import apps.update_menu
import data.data


def initial() -> None:
    root_menu = apps.show_data_menu.main()
    # while True:
    #     root_menu: str = None

    #     match root_menu:
    #         case '1': root_menu = apps.add_menu.main()
    #         case '2': root_menu = apps.show_data_menu.main()
    #         case '3': root_menu = apps.update_menu.main()
    #         case '4': root_menu = apps.sort_menu.main()
    #         case '5': root_menu = apps.search_menu.main()
    #         case '6': break
    #         case  _ : root_menu = apps.main_menu.main()


if __name__ == "__main__":
    initial()
