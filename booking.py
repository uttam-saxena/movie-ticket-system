from booking import view_movies, book_ticket


def main():
    while True:
        print("\n" + "=" * 30)
        print(" WELCOME TO UTTAM CINEMAS")
        print("=" * 30)
        print("1. View Available Movies")
        print("2. Book a Ticket & Snacks")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1/2/3): ")
        
        if choice == '1':
            view_movies()

        elif choice == '2':
            book_ticket()

        elif choice == '3':
            print("\nThank you for visiting! Enjoy your movie. ")
            break

        else:
            print("\n Invalid input. Please type 1, 2, or 3.")


if __name__ == "__main__":
    main()