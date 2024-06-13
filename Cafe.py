class MenuItem:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

class OrderItem:
    def __init__(self, menu_item_id, quantity):
        self.menu_item_id = menu_item_id
        self.quantity = quantity
        self.item_cost = 0.0

class Order:
    def __init__(self, id, customer_name):
        self.id = id
        self.customer_name = customer_name
        self.items = []
        self.total_cost = 0.0

    def calculate_total_cost(self):
        self.total_cost = sum(item.item_cost for item in self.items)

menu = [
    MenuItem(1, "Burger", 5.99),
    MenuItem(2, "Pizza", 8.99),
    MenuItem(3, "Salad", 4.99)
]

orders = []
order_count = 0

def display_menu():
    print("\nMenu:")
    for item in menu:
        print(f"{item.id}. {item.name} - ${item.price:.2f}")
    print("\n" + "-" * 40)

def place_order():
    global order_count
    if order_count < 50:
        customer_name = input("\nCustomer Name: ")

        order = Order(order_count + 1, customer_name)
        
        print("\nAdd items to the order (enter 0 to finish):")
        while len(order.items) < 10:
            try:
                item_id = int(input("Item ID: "))
                if item_id == 0:
                    break
                menu_item = next((item for item in menu if item.id == item_id), None)
                if menu_item:
                    quantity = int(input("Quantity: "))
                    order_item = OrderItem(item_id, quantity)
                    order_item.item_cost = menu_item.price * quantity
                    order.items.append(order_item)
                else:
                    print("Invalid menu item ID. Please choose a valid item or enter 0 to finish.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        order.calculate_total_cost()
        orders.append(order)
        order_count += 1
        print("\nOrder placed successfully.\n")
    else:
        print("\nOrder limit reached. Cannot place more orders.\n")

def modify_order():
    try:
        order_id = int(input("\nEnter the Order ID to modify: "))
        if 1 <= order_id <= order_count:
            order = orders[order_id - 1]
            print(f"\nCurrent Order Details for Order {order.id}:")
            print(f"Customer: {order.customer_name}")
            print(f"{'Item':<20} {'Quantity':<10} {'Cost':<10}")
            print("-" * 40)
            for item in order.items:
                menu_item = next((m for m in menu if m.id == item.menu_item_id), None)
                if menu_item:
                    print(f"{menu_item.name:<20} {item.quantity:<10} ${item.item_cost:.2f}")

            print(f"\nTotal Cost: ${order.total_cost:.2f}")
            print("\nModify Options:")
            print("1. Change Quantity")
            print("2. Delete Item")
            print("3. Back to Main Menu")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                try:
                    item_index = int(input(f"Enter the item index to change quantity (1-{len(order.items)}): ")) - 1
                    if 0 <= item_index < len(order.items):
                        new_quantity = int(input("Enter the new quantity: "))
                        order.items[item_index].quantity = new_quantity
                        order.items[item_index].item_cost = menu[order.items[item_index].menu_item_id - 1].price * new_quantity
                        order.calculate_total_cost()
                        print("Quantity updated successfully.\n")
                    else:
                        print("Invalid item index.\n")
                except ValueError:
                    print("Invalid input. Please enter a number.")

            elif choice == 2:
                try:
                    item_index = int(input(f"Enter the item index to delete (1-{len(order.items)}): ")) - 1
                    if 0 <= item_index < len(order.items):
                        order.items.pop(item_index)
                        order.calculate_total_cost()
                        print("Item deleted successfully.\n")
                    else:
                        print("Invalid item index.\n")
                except ValueError:
                    print("Invalid input. Please enter a number.")
            elif choice == 3:
                print("Back to Main Menu.")
            else:
                print("Invalid choice. Please try again.")
        else:
            print("Invalid Order ID. Please enter a valid Order ID.\n")
    except ValueError:
        print("Invalid input. Please enter a number.\n")

def view_order_history():
    print("\nOrder History:")
    if not orders:
        print("No orders placed yet.")
    else:
        for order in orders:
            print(f"Order {order.id} by {order.customer_name} - Total Cost: ${order.total_cost:.2f}")
    print("\n" + "-" * 40)

def main():
    while True:
        print("Cafeteria Management System")
        print("1. Place Order")
        print("2. Display Menu")
        print("3. View Order History")
        print("4. Modify Order")
        print("5. Exit")
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                place_order()
            elif choice == 2:
                display_menu()
            elif choice == 3:
                view_order_history()
            elif choice == 4:
                modify_order()
            elif choice == 5:
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Please try again.\n")
        except ValueError:
            print("Invalid input. Please enter a number.\n")

if __name__ == "__main__":
    main()
