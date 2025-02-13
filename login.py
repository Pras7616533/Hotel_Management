import panel as p

# Function for Admin Login
def admin_login(data):
    admin_id = input("Enter Admin ID: ")
    password = input("Enter Password: ")

    if admin_id in data["admins"] and data["admins"][admin_id] == password:
        print("\n✅ Admin Login Successful!")
        p.admin_panel(data)
    else:
        print("\n❌ Invalid Admin Credentials!")


# VIP Login
def vip_login(data):
    vip_id = input("Enter VIP ID: ")
    password = input("Enter Password: ")

    if vip_id in data["vip_customers"] and data["vip_customers"][vip_id] == password:
        print("\n✅ VIP Login Successful!")
        p.vip_panel(data, vip_id)
    else:
        print("\n❌ Invalid VIP Credentials!")
