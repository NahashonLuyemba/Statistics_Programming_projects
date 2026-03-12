
import sqlite3
import re

# ---------- User Class ----------
class User:
    def __init__(self, user_id, name, email, contact, city, password):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.contact = contact
        self.city = city
        self._password = password

    def get_email(self):
        return self.email

    def check_password(self, password):
        return self._password == password 

    def display_role(self):
        return "Regular User"   


# ---------------Admin class inherits from user ------------
class Admin(User):
    def __init__(self, user_id, name, email, contact, city, password):
        super().__init__(user_id, name, email, contact, city, password)

    def display_role(self):
        return "Admin User"
  
# ---------- Hotel Class ----------
class Hotel:
    def __init__(self):
        self.users = []         # Store registered users
        self.orders_history = []  # Store all orders placed
        self.user_count = 1     # Auto-increment user IDs
        self.setup_database()
        self.cursor.execute("SELECT id, name, email, city FROM users")
        rows = self.cursor.fetchall()
        for row in rows:
            user = User(row[0], row[1], row[2], "N/A", row[3], "N/A")
            self.users.append(user)



    def setup_database(self):
        self.conn = sqlite3.connect("restaurant.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute(
"CREATE TABLE IF NOT EXISTS users (id INTEGER, name TEXT, email TEXT, city TEXT)"
)
        self.conn.commit()    

        # Menu
        self.menu = {
            "Veg": {
                1: ("Kales", 180),
                2: ("Veg Biryani", 150),
                3: ("Managu", 250),
                4: ("Cow Piece", 200),
                5: ("Spider Plant (Sagaa)", 300),
            },
            "Non-Veg": {
                6: ("Chicken Curry", 380),
                7: ("Mutton Biryani", 390),
                8: ("Fish Fry", 350),
                9: ("Egg Curry", 150),
                10: ("Chicken Kebab", 400),
                11:("Ugali", 150),
                12:("Chapati", 30),
                13:("Beans", 50),
            }
        }

    # ---------- Registration ----------
    def register(self):
        print("\n--- Registration Form ---")
        name = input("Enter Name: ").capitalize()
        while True:
            email = input("Enter Email: ").lower()
    # Simple email regex pattern
            if re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
                break
            else:
                print("Invalid email format. Please enter a valid email.")

        contact = input("Enter Contact: ")
        city = input("Enter City: ").capitalize()
        password = input("Enter Password: ")

        user = User(self.user_count, name, email, contact, city, password)
        self.users.append(user)
        self.cursor.execute(
    "INSERT INTO users VALUES (?, ?, ?, ?)",
    (user.user_id, user.name, user.email, user.city)
)
        self.conn.commit()

        self.user_count += 1

        print(f"\nRegistration Successful! Welcome, {name}!\n")

    # ---------- User Login ----------
    def login(self):
        print("\n--- Login ---")
        email = input("Enter Email: ").lower()
        password = input("Enter Password: ")

        for user in self.users:
            if user.get_email() == email and user.check_password(password):
                print(f"\nLogin Successful! Welcome back, {user.name}!\n")
                self.show_menu(user)
                return
        print("\nInvalid Email or Password!\n")

    # ---------- Show Menu ----------
    def show_menu(self, user):
        print("------ MENU ------")
        print("\nVEG ITEMS:")
        for key, item in self.menu["Veg"].items():
            print(f"{key}. {item[0]} - Ksh{item[1]}")

        print("\nNON-VEG ITEMS:")
        for key, item in self.menu["Non-Veg"].items():
            print(f"{key}. {item[0]} - Ksh{item[1]}")

        self.take_order(user)

    # ---------- Take Order ----------
    def take_order(self, user):
        orders = []  # Store this user's orders
        while True:
            choice = input("\nEnter item number to order (or 'done' to finish): ")

            if choice.lower() == "done":
                break

            try:
                choice = int(choice)
                for category in self.menu.values():
                    if choice in category:
                        orders.append(category[choice])
                        print(f"{category[choice][0]} added to your order.")
                        break
                else:
                    print("Invalid choice, please try again.")
            except ValueError:
                print("Please enter a valid number.")

        if orders:
            self.orders_history.append((user.name, orders))
        self.generate_bill(orders)

    # ---------- Generate Bill ----------
    def generate_bill(self, orders):
        print("\n------ BILL ------")
        total = 0
        for item in orders:
            print(f"{item[0]} - Ksh{item[1]}")
            total += item[1]
        print("------------------")
        print(f"Total Amount: Ksh{total}")
        print("------------------\n")

    # ---------- Admin Login ----------
    def admin_login(self):
        print("\n--- Admin Login ---")
        username = input("Enter Admin Username: ")
        password = input("Enter Admin Password: ")

        if username == "admin" and password == "admin123":
            print("\nAdmin Login Successful!\n")
            self.admin_menu()
        else:
            print("\nInvalid Admin Credentials!\n")

    # ---------- Admin Menu ----------
    def admin_menu(self):
        while True:
            print("------ ADMIN MENU ------")
            print("1. View Registered Users")
            print("2. View All Orders")
            print("3. Logout")

            choice = input("Enter choice: ")

            if choice == "1":
                self.view_users()
            elif choice == "2":
                self.view_orders()
            elif choice == "3":
                print("\nAdmin Logged Out.\n")
                break
            else:
                print("Invalid choice!")

    # ---------- View Users ----------
    def view_users(self):
        if not self.users:
            print("\nNo users registered yet!\n")
        else:
            print("\n--- Registered Users ---")
            for user in self.users:
                print(f"ID: {user.user_id}, Name: {user.name}, Email: {user.email}, City: {user.city}")
            print()

    # ---------- View Orders ----------
    def view_orders(self):
        if not self.orders_history:
            print("\nNo orders placed yet!\n")
        else:
            print("\n--- Orders History ---")

            for name, orders in self.orders_history:
                print(f"\n{name}'s Order:")
                for item in orders:
                    print(f"   {item[0]} - Ksh{item[1]}")
            print()

    # ---------- Main Menu ----------
    def main(self):
        while True:
            print("------ WELCOME TO SHON'S RESTAURANT ------")
            print("1. Register")
            print("2. Login")
            print("3. Admin Login")
            print("4. Exit")

            choice = input("Enter choice: ")

            if choice == "1":
                self.register()
            elif choice == "2":
                self.login()
            elif choice == "3":
                self.admin_login()
            elif choice == "4":
                print("\nThank you for visiting SHON'S Restaurant. Goodbye!")
                break
            else:
                print("Invalid choice, please try again.\n")


# ---------- Run the Program ----------
hotel = Hotel()
hotel.main()