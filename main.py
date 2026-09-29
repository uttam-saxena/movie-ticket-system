
movies = [
    ("The Matrix", "10:00 AM", 150),
    ("Inception", "01:00 PM", 200),
    ("Interstellar", "06:00 PM", 250)
]


snacks = [
    ("Popcorn (Regular)", 80),
    ("Popcorn (Large)", 120),
    ("Cold Drink", 60),
    ("Coffee", 90)
]

seats = [
    ['O', 'O', 'O', 'O', 'O'],  
    ['O', 'O', 'O', 'O', 'O'],  
    ['O', 'O', 'O', 'O', 'O']   
]


while True:
    print("\n" + "="*30)
    print(" WELCOME TO UTTAM CINEMAS")
    print("="*30)
    print("1. View Available Movies")
    print("2. Book a Ticket & Snacks")
    print("3. Exit")
    
    choice = input("\nEnter your choice (1/2/3): ")
    
    if choice == '1':
        print("\n--- Now Showing ---")
        for index in range(len(movies)):
            print(f"{index + 1}. {movies[index][0]} | Time: {movies[index][1]} | Ticket: ₹{movies[index][2]}")

    elif choice == '2':
        print("\n--- Book Your Seat ---")
        for index in range(len(movies)):
            print(f"{index + 1}. {movies[index][0]}")
            
        movie_choice = int(input("\nSelect a movie (1-3): ")) - 1
        
        if 0 <= movie_choice < len(movies):
            print(f"\nSeat Map for {movies[movie_choice][0]}:")
            print(f"Seats: {seats[movie_choice]}")
            
            seat_choice = int(input("Select a seat number (1-5): ")) - 1
            
            if 0 <= seat_choice < len(seats[movie_choice]):
                if seats[movie_choice][seat_choice] == 'O':
                    
                    seats[movie_choice][seat_choice] = 'X' 
                    print("\n SEAT BOOKED SUCCESSFULLY!")
                    
                    
                    total_bill = movies[movie_choice][2] 
                    ordered_snacks = [] 
                    
                    
                    while True:
                        add_snack = input("\nWould you like to add popcorn or a beverage? (y/n): ").lower()
                        if add_snack == 'y':
                            print("\n--- Snacks Menu ---")
                            for index in range(len(snacks)):
                                print(f"{index + 1}. {snacks[index][0]} - ₹{snacks[index][1]}")
                                
                            snack_choice = int(input("\nSelect an item (1-4): ")) - 1
                            
                            if 0 <= snack_choice < len(snacks):
                                qty = int(input("Enter quantity: "))
                                if qty > 0:
                                    
                                    snack_cost = snacks[snack_choice][1] * qty
                                    total_bill += snack_cost
                                    
                                    ordered_snacks.append((snacks[snack_choice][0], qty, snack_cost))
                                    print(f" Added {qty}x {snacks[snack_choice][0]} to your order.")
                                else:
                                    print(" Quantity must be at least 1.")
                            else:
                                print(" Invalid snack choice.")
                        else:
                            break 
                    
                   
                    print("\n" + "*"*30)
                    print("️ FINAL BOOKING RECEIPT")
                    print("*"*30)
                    print(f"Movie: {movies[movie_choice][0]}")
                    print(f"Seat Number: {seat_choice + 1}")
                    print(f"Ticket Price: ₹{movies[movie_choice][2]}")
                    
                    
                    if len(ordered_snacks) > 0:
                        print("\nFood & Beverage:")
                        for item in ordered_snacks:
                             print(f"  - {item[1]}x {item[0]} (₹{item[2]})")

                    
                            
                    print("-" * 30)
                    print(f"TOTAL AMOUNT DUE: ₹{total_bill}")
                    print("*"*30)

                else:
                    print("\n Sorry, that seat is already booked.")
            else:
                print("\n Invalid seat number.")
        else:
            print("\n Invalid movie choice.")

    elif choice == '3':
        print("\nThank you for visiting! Enjoy your movie. ")
        break

    else:
        print("\n Invalid input. Please type 1, 2, or 3.")
