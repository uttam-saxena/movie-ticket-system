from data import snacks


def order_snacks():
    ordered_snacks = []
    total_snack_cost = 0

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
                    total_snack_cost += snack_cost
                    
                    ordered_snacks.append((snacks[snack_choice][0], qty, snack_cost))
                    print(f" Added {qty}x {snacks[snack_choice][0]} to your order.")
                else:
                    print(" Quantity must be at least 1.")
            else:
                print(" Invalid snack choice.")
        else:
            break

    return ordered_snacks, total_snack_cost