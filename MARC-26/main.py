print("EXERCISE 1:")
file = open("logins.txt", "r")
names = file.read().splitlines()
file.close()
print("All Names:", names)
print("Total Records:", len(names))
count = {}
for name in names:
    count[name] = count.get(name, 0) + 1
print("Login Count:", count)
most = max(count, key=count.get)
print("Most Logged In User:", most)
print("Unique Users:", set(names))

print("\nEXERCISE 2:")
file = open("numbers.txt", "r")
nums = file.read().splitlines()
file.close()
numbers = []
for n in nums:
    numbers.append(int(n))
print("All Numbers:", numbers)
print("Sum:", sum(numbers))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
count = 0
for n in numbers:
    if n > 50:
        count += 1
print("Greater than 50:", count)

print("\nEXERCISE 3:")
import json
file = open("students.json", "r")
data = json.load(file)
file.close()
students = data["students"]
print("Student Names:")
for s in students:
    print(s["name"])
print("Python Students:")
for s in students:
    if s["course"] == "Python":
        print(s["name"])
topper = max(students, key=lambda x: x["marks"])
print("Highest Marks:", topper["name"])
total = 0
for s in students:
    total += s["marks"]
print("Average Marks:", total / len(students))
course_count = {}
for s in students:
    course = s["course"]
    course_count[course] = course_count.get(course, 0) + 1
print("Students Per Course:", course_count)

print("\nEXERCISE 4:")
import json
file = open("orders.json", "r")
data = json.load(file)
file.close()
orders = data["orders"]
print("All Orders:")
for o in orders:
    print(o)
revenue = 0
for o in orders:
    revenue += o["amount"]
print("Total Revenue:", revenue)
spending = {}
for o in orders:
    customer = o["customer"]
    spending[customer] = spending.get(customer, 0) + o["amount"]
print("Spending Per Customer:", spending)
highest = max(spending, key=spending.get)
print("Highest Spending Customer:", highest)
count = {}
for o in orders:
    customer = o["customer"]
    count[customer] = count.get(customer, 0) + 1
print("Orders Per Customer:", count)

print("\nEXERCISE 5:")
import csv
file = open("employees.csv", "r")
reader = csv.DictReader(file)
employees = list(reader)
file.close()
print("Employee Names:")
for e in employees:
    print(e["name"])
print("IT Employees:")
for e in employees:
    if e["department"] == "IT":
        print(e["name"])
total = 0
for e in employees:
    total += int(e["salary"])
print("Average Salary:", total / len(employees))
highest = max(employees, key=lambda x: int(x["salary"]))
print("Highest Salary Employee:", highest["name"])
dept = {}
for e in employees:
    d = e["department"]
    dept[d] = dept.get(d, 0) + 1
print("Employees Per Department:", dept)

print("\nEXERCISE 6:")
import csv
file = open("sales.csv", "r")
reader = csv.DictReader(file)
sales = list(reader)
file.close()
total_revenue = 0
qty = {}
revenue = {}
for s in sales:
    product = s["product"]
    quantity = int(s["quantity"])
    price = int(s["price"])
    total_revenue += quantity * price
    qty[product] = qty.get(product, 0) + quantity
    revenue[product] = revenue.get(product, 0) + quantity * price
print("Total Sales Revenue:", total_revenue)
print("Quantity Per Product:", qty)
highest = max(qty, key=qty.get)
print("Highest Sales Product:", highest)
print("Revenue Per Product:", revenue)
print("Products Above 50000:")
for p in revenue:
    if revenue[p] > 50000:
        print(p)

print("\nBONUS CHALLENGE:")
import csv
file = open("sales.csv", "r")
reader = csv.DictReader(file)
summary = {}
for row in reader:
    product = row["product"]
    qty = int(row["quantity"])
    price = int(row["price"])
    if product not in summary:
        summary[product] = {"qty": 0, "revenue": 0}
    summary[product]["qty"] += qty
    summary[product]["revenue"] += qty * price
file.close()
print("Product Sales Summary")
for product in summary:
    print(product, "→ Qty:", summary[product]["qty"], "Revenue:", summary[product]["revenue"])