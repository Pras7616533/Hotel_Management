# Hotel Management System

This Python-based hotel management system provides an interface for admins, VIP customers, and normal customers to manage and view orders efficiently. The system is designed to streamline order management, ensure security, and enhance user experience.

## Features

- **Admin Panel**:
  - View all orders placed in the system.
  - Add new orders with customer details and items.
  - Remove existing orders from the database.
  - Change VIP customer passwords for enhanced security.
  - Secure authentication for admin access.

- **VIP Customer Panel**:
  - Log in securely with VIP credentials.
  - View and track their specific orders.

- **Normal Customer View**:
  - Search for their order status using the order ID.

## How It Works

1. The system initializes by loading data from `db.txt`, where:
   - Admin credentials are stored.
   - VIP customer credentials are saved.
   - Order records, including customer details and items, are maintained.

2. Users interact with the system through a main menu, allowing them to:
   - Log in as an Admin for full system control.
   - Log in as a VIP Customer to view exclusive orders.
   - Look up an order as a Normal Customer using an order ID.

3. **Admins** can:
   - View all placed orders.
   - Add new orders with customer details.
   - Remove orders as needed.
   - Modify VIP customer passwords.

4. **VIP Customers** can:
   - Securely log in.
   - Access their own order details.

5. **Normal Customers** can:
   - Enter an order ID to retrieve their order details.

## File Structure

- **`hotel_management.py`**: The main Python script containing all functionalities, including authentication, order management, and data storage.
- **`db.txt`**: The text-based database file storing admins, VIP customers, and order records.

## Usage

1. Run the program using the following command:
   ```bash
   python hotel_management.py
   ```

2. Select an option from the displayed main menu.
3. Enter the required credentials (Admin/VIP) or an order ID to proceed.

## Example Scenarios

### Admin Login:
```
Enter Admin ID: admin1
Enter Password: password123
✅ Admin Login Successful!
```

### Adding an Order:
```
Enter Order ID: O123
Enter Customer Type (Normal/VIP): VIP
Enter Customer Name: John Doe
Enter Items Ordered: Pizza, Soda
Enter Total Price: 25.50
✅ Order Added Successfully!
```

### Removing an Order:
```
Enter Order ID to Remove: O123
✅ Order Removed Successfully!
```

### Viewing an Order as a Normal Customer:
```
Enter Order ID: O123
✅ Your Order Details:
Customer: John Doe
Items: Pizza, Soda
Total Price: $25.50
```

## Future Enhancements

- Implement a graphical user interface (GUI) for a more user-friendly experience.
- Introduce secure authentication with hashed passwords instead of plaintext storage.
- Allow multiple admin users with different levels of access.
- Add an order history tracking feature for VIP customers.
- Enable automatic order confirmation emails for customers.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
