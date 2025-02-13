import db
import panel as p
import login as l

# Main Menu
def main():
    data = db.load_database()

    while True:
        print("\n--- Hotel Management System ---")
        print("1. Admin Login")
        print("2. VIP Customer Login")
        print("3. Normal Customer View Order")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            l.admin_login(data)
        elif choice == "2":
            l.vip_login(data)
        elif choice == "3":
            p.normal_customer_view(data)
        elif choice == "4":
            print("\n🚪 Exiting...")
            break
        else:
            print("\n❌ Invalid Choice! Try Again.")

if __name__ == "__main__":
    main()
