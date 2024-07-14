from datetime import datetime
from collections import namedtuple

SalesData = namedtuple('SalesData', ['product_name', 'value'])

class SalesSystem:
    def __init__(self):
        self.sales = []
        self.expenses = []
        self.net_profit = 0.0
        self.net_sales = -1
        self.time = None
        self.date = None
        self.day = None

    def display_login_screen(self):
        print("Welcome to the Sales System")

    def authenticate_user(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        if username == "admin" and password == "admin":
            return True
        else:
            print("Authentication failed.")
            return False

    def enter_date_time(self):
        self.time = input("Enter time: ")
        self.date = input("Enter date: ")
        self.day = input("Enter day: ")

    def display_main_screen(self):
        print("\nMain Menu")
        print("1. Enter Sales")
        print("2. Statistics")
        print("3. Reviews")
        if len(self.sales) > 0:
            print("4. Enter Expenses")
            if len(self.expenses) > 0:
                print("5. Net Sales")
                print("6. Net Profit")
        print("*. Exit")
        print("Choose an option: ")

    def enter_sales_data(self):
        num_sales = int(input("Enter the number of sales transactions: "))
        if num_sales < 1:
            print("Number of sales transactions must be at least 1.")
            return
        for i in range(num_sales):
            sale = SalesData(input(f"Enter product name for product {i + 1}: "), float(input(f"Enter sales value for product {i + 1}: ")))
            self.sales.append(sale)
        print("Sales data entered successfully.")

    def enter_expense_data(self):
        num_expenses = int(input("Enter the number of expense transactions: "))
        if num_expenses < 1:
            print("Number of expense transactions must be at least 1.")
            return
        for i in range(num_expenses):
            expense = SalesData(input(f"Enter product name for product {i + 1}: "), float(input(f"Enter expense value for product {i + 1}: ")))
            self.expenses.append(expense)
        print("Expense data entered successfully.")

    def display_net_sales_screen(self):
        total_sales = sum(sale.value for sale in self.sales)
        total_expenses = sum(expense.value for expense in self.expenses)
        self.net_sales = total_sales - total_expenses
        print(f"\nNet Sales for {self.date} - {self.time} ({self.day}): {self.net_sales} dinars")

    def display_net_profit_screen(self):
        if not self.sales or not self.expenses:
            print("Please enter sales and expenses first.")
            return
        if self.net_sales == -1:
            print("Please calculate net sales first.")
            return
        total_sales = sum(sale.value for sale in self.sales)
        total_expenses = sum(expense.value for expense in self.expenses)
        net_sales = total_sales - total_expenses
        self.net_profit = net_sales - (0.16 * net_sales)
        print(f"\nNet Profit for {self.date} - {self.time} ({self.day}): {self.net_profit} dinars")

    def display_statistics_screen(self):
        if not self.sales or not self.expenses:
            print("Please enter sales and expenses first.")
            return
        print("\nStatistics Menu")
        print("1. Highest Sales Value")
        print("2. Highest Expense Value")
        print("3. Lowest Sales Value")
        print("4. Lowest Expense Value")
        print("5. Values where Sales match Expenses")
        print("6. Return to Main Menu")
        print("Choose an option: ")
        choice = input()
        if choice == '1':
            max_sale = max(self.sales, key=lambda x: x.value)
            print(f"\nHighest Sales Value: {max_sale.product_name} - {max_sale.value} dinars")
        elif choice == '2':
            max_expense = max(self.expenses, key=lambda x: x.value)
            print(f"\nHighest Expense Value: {max_expense.product_name} - {max_expense.value} dinars")
        elif choice == '3':
            min_sale = min(self.sales, key=lambda x: x.value)
            print(f"\nLowest Sales Value: {min_sale.product_name} - {min_sale.value} dinars")
        elif choice == '4':
            min_expense = min(self.expenses, key=lambda x: x.value)
            print(f"\nLowest Expense Value: {min_expense.product_name} - {min_expense.value} dinars")
        elif choice == '5':
            print("\nMatching Sales and Expenses Values:")
            for sale in self.sales:
                for expense in self.expenses:
                    if sale.value == expense.value:
                        print(f"{sale.product_name} - {sale.value} dinars")
        elif choice == '6':
            return
        else:
            print("Invalid choice. Please try again.")
        while True:
            choice1 = input("1. Return to Statistics\n")
            if choice1 == '1':
                self.display_statistics_screen()
                break
            else:
                print("Invalid choice. Please try again.")

    def display_reviews_screen(self):
        if not self.sales or not self.expenses:
            print("Please enter sales and expenses first.")
            return
        total_sales = sum(sale.value for sale in self.sales)
        total_expenses = sum(expense.value for expense in self.expenses)
        net_sales = total_sales - total_expenses
        print("\nReviews Menu")
        if net_sales < 0:
            print("Warning: There is a problem with income. Management should be informed.")
        elif net_sales > 1000:
            print("Thank you! Financial status is excellent.")
        elif net_sales > 0 and net_sales < 1000:
            print("The situation is within the critical range.")
        print("Return to Main Menu")

    def exit_program(self):
        choice = input("Do you really want to exit the program? (y/n): ")
        if choice == 'y' or choice == 'Y':
            print("Exiting program. Thank you for using the system.")
            exit(0)

if __name__ == "__main__":
    system = SalesSystem()
    system.display_login_screen()
    if not system.authenticate_user():
        print("Authentication failed. Exiting program.")
        exit(1)
    system.enter_date_time()
    while True:
        system.display_main_screen()
        choice = input()
        if choice == '1':
            system.enter_sales_data()
        elif choice == '2':
            system.display_statistics_screen()
        elif choice == '3':
            system.display_reviews_screen()
        elif choice == '4':
            system.enter_expense_data()
        elif choice == '5':
            system.display_net_sales_screen()
        elif choice == '6':
            system.display_net_profit_screen()
        elif choice == '*':
            system.exit_program()
        else:
            print("Invalid choice. Please try again.")

