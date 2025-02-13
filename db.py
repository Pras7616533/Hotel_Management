import os

DB_FILE = "db.txt"

# Function to load database
def load_database():
    data = {"admins": {}, "vip_customers": {}, "orders": []}

    if not os.path.exists(DB_FILE):
        return data  # Return empty structure if file doesn't exist

    with open(DB_FILE, "r") as file:
        for line in file:
            parts = line.strip().split(",")
            if parts[0] == "ADMIN":
                data["admins"][parts[1]] = parts[2]  # Admin ID: Password
            elif parts[0] == "VIP":
                data["vip_customers"][parts[1]] = parts[2]  # VIP ID: Password
            elif parts[0] == "ORDER":
                order = {
                    "order_id": parts[1],
                    "customer_type": parts[2],
                    "customer_name": parts[3],
                    "items": parts[4],
                    "total_price": float(parts[5])
                }
                data["orders"].append(order)

    return data

# Function to save database
def save_database(data):
    with open(DB_FILE, "w") as file:
        for admin, password in data["admins"].items():
            file.write(f"ADMIN,{admin},{password}\n")
        for vip, password in data["vip_customers"].items():
            file.write(f"VIP,{vip},{password}\n")
        for order in data["orders"]:
            file.write(f"ORDER,{order['order_id']},{order['customer_type']},{order['customer_name']},{order['items']},{order['total_price']:.2f}\n")

