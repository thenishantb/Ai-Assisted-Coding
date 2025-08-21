

"""Task Description #1:
• Start a Python class named Student with attributes name, roll_number, and marks. Prompt
GitHub Copilot to complete methods for displaying details and checking if marks are above
average"""
class Student:
	def __init__(self, name, roll_number, marks):
		self.name = name
		self.roll_number = roll_number
		self.marks = marks

	def display_details(self):
		print(f"Name: {self.name}")
		print(f"Roll Number: {self.roll_number}")
		print(f"Marks: {self.marks}")

	def is_above_average(self, average=50):
		return self.marks > average

# Example usage
if __name__ == "__main__":
	student = Student("Alice", "101", 78)
	student.display_details()
	print("Above average?", student.is_above_average())


"""
Task 2:
Write the first two lines of a for loop to iterate through a list of numbers. Use a comment
prompt to let Copilot suggest how to calculate and print the square of even numbers only
"""
# Iterate through a list of numbers
numbers = [1, 2, 3, 4, 5, 6]
for num in numbers:
	if num % 2 == 0:
		print(f"Square of {num}: {num ** 2}")


"""
Task 3:
Create a class called BankAccount with attributes account_holder and balance. Use Copilot to
complete methods for deposit(), withdraw(), and check for insufficient balance
"""
# BankAccount class with Copilot prompts for methods
class BankAccount:
	def __init__(self, account_holder, balance=0):
		self.account_holder = account_holder
		self.balance = balance


	def deposit(self, amount):
		if amount > 0:
			self.balance += amount
			print(f"Deposited {amount}. New balance: {self.balance}")
		else:
			print("Deposit amount must be positive.")


	def withdraw(self, amount):
		if amount <= 0:
			print("Withdrawal amount must be positive.")
		elif amount > self.balance:
			print("Insufficient balance.")
		else:
			self.balance -= amount
			print(f"Withdrew {amount}. New balance: {self.balance}")
# Example usage of BankAccount class

# Create an account for John with an initial balance of 500
account1 = BankAccount("John Doe", 500)

# Deposit money
account1.deposit(200)   # Should add 200, balance becomes 700
account1.deposit(-50)   # Invalid deposit

# Withdraw money
account1.withdraw(100)  # Should subtract 100, balance becomes 600
account1.withdraw(1000) # Insufficient balance
account1.withdraw(-20)  # Invalid withdrawal

# Another account
account2 = BankAccount("Alice", 1000)
account2.deposit(500)
account2.withdraw(300)


"""
Define a list of student dictionaries with keys name and score. write a while
loop to print the names of students who scored more than 75.
"""
# List of student dictionaries
students = [
	{"name": "Alice", "score": 80},
	{"name": "Bob", "score": 70},
	{"name": "Charlie", "score": 90},
	{"name": "David", "score": 60}
]

# While loop to print names of students who scored more than 75
i = 0
while i < len(students):
	if students[i]["score"] > 75:
		print(students[i]["name"])
	i += 1


"""Begin writing a class ShoppingCart with an empty items list. Prompt Copilot to generate
methods to add_item, remove_item, and use a loop to calculate the total bill using conditional
discounts"""

# ShoppingCart class
class ShoppingCart:
	def __init__(self):
		self.items = []


	def add_item(self, item):
		self.items.append(item)
		print(f"Added {item} to cart.")


	def remove_item(self, item):
		if item in self.items:
			self.items.remove(item)
			print(f"Removed {item} from cart.")
		else:
			print(f"Item {item} not found in cart.")


	def calculate_total(self):
		total = 0
		# Assume each item is a dict with 'name' and 'price' keys
		for item in self.items:
			total += item.get('price', 0)
		# Apply a 10% discount if total exceeds 100
		if total > 100:
			discount = total * 0.10
			total -= discount
			print(f"Discount applied: {discount}")
		print(f"Total bill: {total}")
		return total
#Example Usage:
# Create a shopping cart
cart = ShoppingCart()

# Add items
cart.add_item({'name': 'Laptop', 'price': 750})
cart.add_item({'name': 'Headphones', 'price': 50})
cart.add_item({'name': 'Mouse', 'price': 20})

# Remove an item
cart.remove_item({'name': 'Mouse', 'price': 20})

# Calculate total
cart.calculate_total()
