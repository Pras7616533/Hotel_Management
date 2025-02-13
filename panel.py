import function as f

# Admin Panel
def admin_panel(data):
    while True:
        print("\n--- Admin Panel ---")
        print("1. View All Orders")
        print("2. Add New Order")
        print("3. Remove Order")
        print("4. Change VIP Password")
        print("5. Logout")

        choice = input("Enter choice: ")

        if choice == "1":
            f.list_order(data)

        elif choice == "2":
            f.add_order(data)

        elif choice == "3":
            f.remove_order(data)

        elif choice == "4":
            f.vip_change_pass(data)

        elif choice == "5":
            print("\n🔒 Logging Out...")
            break

        else:
            print("\n❌ Invalid Choice!")

# VIP Panel
def vip_panel(data, vip_id):
    while True:
        print("\n--- VIP Panel ---")
        print("1. View VIP Orders")
        print("2. Logout")

        choice = input("Enter choice: ")

        if choice == "1":
            f.vip_view_order(data)

        elif choice == "2":
            print("\n🔒 Logging Out...")
            break

        else:
            print("\n❌ Invalid Choice!")

# Normal Customer View
def normal_customer_view(data):
    f.normal_order(data)
