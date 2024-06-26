import stream_viewer
import streamer_manager


def main_menu():
    while True:
        print("\n1. View Who Is Live")
        print("2. Edit Streamer List")
        print("3. Watch Stream")
        option = input("Choose an option (1-3)\nenter: ")
        if option == '1':
            stream_viewer.view_who_is_live()
        elif option == '2':
            streamer_manager.edit_streamers()
        elif option == '3':
            streamer_name = input("Enter the streamer name to watch\nenter: ")
            stream_viewer.watch_stream(streamer_name)
        else:
            print("Invalid option, please choose again!\nenter: ")
            main_menu()

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\nExitng the application")