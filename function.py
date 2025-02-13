import db

#Admin function
def list_order(data):
    print("\n📋 Order List:")
    for order in data["orders"]:
        print(f"Order ID: {order['order_id']} | {order['customer_type']} | {order['customer_name']} | {order['items']} | ${order['total_price']}")


def add_order(data):
    order_id = input("Enter Order ID: ")
    customer_type = input("Enter Customer Type (Normal/VIP): ")
    customer_name = input("Enter Customer Name: ")
    items = input("Enter Items Ordered: ")
    total_price = input("Enter Total Price: ")

    data["orders"].append({
        "order_id": order_id,
        "customer_type": customer_type,
        "customer_name": customer_name,
        "items": items,
        "total_price": float(total_price)
    })

    db.save_database(data)
    print("\n✅ Order Added Successfully!")

def remove_order(data):
    order_id = input("Enter Order ID to Remove: ")
    data["orders"] = [o for o in data["orders"] if o["order_id"] != order_id]
    db.save_database(data)
    print("\n✅ Order Removed Successfully!")


def vip_change_pass(data):
    vip_id = input("Enter VIP ID: ")
    if vip_id in data["vip_customers"]:
        new_password = input("Enter New VIP Password: ")
        data["vip_customers"][vip_id] = new_password
        db.save_database(data)
        print("\n✅ VIP Password Updated!")
    else:
        print("\n❌ VIP ID Not Found!")


#VIP function
def vip_view_order(data):
    print("\n📋 VIP Orders:")
    found = False
    for order in data["orders"]:
        if order["customer_type"] == "VIP" and vip_id in order["order_id"]:
            print(f"Order ID: {order['order_id']} | {order['customer_name']} | {order['items']} | ${order['total_price']}")
            found = True

    if not found:
        print("❌ No VIP Orders Found!")


# Normal order
def normal_order(data):
    order_id = input("Enter Order ID: ")

    for order in data["orders"]:
        if order["order_id"] == order_id:
            print(f"\n✅ Your Order Details:\nCustomer: {order['customer_name']}\nItems: {order['items']}\nTotal Price: ${order['total_price']}")
            return

    print("\n❌ Order Not Found!")
