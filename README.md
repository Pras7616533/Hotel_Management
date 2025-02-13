# Hotel Management System

This Python-based hotel management system provides an interface for admins, VIP customers, and normal customers to manage and view orders efficiently.

## Features

- **Admin Panel**:
  - View all orders.
  - Add new orders.
  - Remove orders.
  - Change VIP customer passwords.
  - Secure login system.

- **VIP Customer Panel**:
  - View their own orders.
  - Secure login system.

- **Normal Customer View**:
  - Search for their order using the order ID.

## How It Works

1. The system loads data from `db.txt`, where admin credentials, VIP credentials, and order records are stored.
2. Users can select from the main menu:
   - Admin login.
   - VIP customer login.
   - Normal customer order lookup.
3. Admins have full control over order management and VIP credentials.
4. VIP customers can view their specific orders.
5. Normal customers can retrieve order details using an order ID.

## File Structure

- **`hotel_management.py`**: Main Python script containing all functionalities.
- **`db.txt`**: Stores admin credentials, VIP credentials, and orders.

## Usage

1. Run the program:
   ```bash
   python hotel_management.py
   ```

2. Select an option from the main menu.
3. Enter the required credentials or order ID to proceed.

## Example

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

### Viewing an Order as a Normal Customer:
```
Enter Order ID: O123
✅ Your Order Details:
Customer: John Doe
Items: Pizza, Soda
Total Price: $25.50
```

## Future Enhancements

- Implement a graphical user interface (GUI) for ease of use.
- Add authentication mechanisms such as hashed passwords.
- Introduce order history tracking.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
