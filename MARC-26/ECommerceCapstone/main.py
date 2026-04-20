# PYTHON CAPSTONE PROJECT
# E-Commerce Order Analytics System

import json
import csv

# FUNCTIONS

# Task 23
def load_visits():
    with open("website_visits.txt", "r") as file:
        return file.read().splitlines()

# Task 24
def load_products():
    with open("products.json", "r") as file:
        data = json.load(file)
        return data["products"]

# Task 25
def load_orders():
    with open("orders.csv", "r") as file:
        data = csv.DictReader(file)
        return list(data)

# Task 26
def calculate_product_revenue(product_id, quantity, product_dict):
    return product_dict[product_id]["price"] * quantity

# Task 27
def calculate_customer_spending(customer_name, spending_dict):
    return spending_dict.get(customer_name, 0)

# Task 28
def find_top_customer(spending_dict):
    return max(spending_dict, key=spending_dict.get)

# PART 1 WEBSITE VISITS

# Task 1
visits = load_visits()
print("Task 1 - website_visits.txt loaded")

# Task 2
print("Task 2 - All Visitors:")
print(visits)

# Task 3
print("\nTask 3 - Total Visits:")
print(len(visits))

# Task 4
unique_visitors = set(visits)
print("\nTask 4 - Unique Visitors:")
print(unique_visitors)

# Task 5
visit_count = {}
for name in visits:
    visit_count[name] = visit_count.get(name, 0) + 1
print("\nTask 5 - Visit Count:")
print(visit_count)

# Task 6
most_frequent = max(visit_count, key=visit_count.get)
print("\nTask 6 - Most Frequent Visitor:")
print(most_frequent)

# PART 2 PRODUCTS

# Task 7
products = load_products()

# Task 8
print("\nTask 8 - Product Names and Prices:")
for item in products:
    print(item["name"], "-", item["price"])

# Task 9
product_dict = {}
for item in products:
    product_dict[item["product_id"]] = {
        "name": item["name"],
        "price": item["price"]
    }
print("\nTask 9 - Product Dictionary:")
print(product_dict)

# Task 10
most_expensive = max(products, key=lambda x: x["price"])
print("\nTask 10 - Most Expensive Product:")
print(most_expensive["name"], most_expensive["price"])

# Task 11
least_expensive = min(products, key=lambda x: x["price"])
print("\nTask 11 - Least Expensive Product:")
print(least_expensive["name"], least_expensive["price"])

# PART 3 ORDERS

# Task 12
orders = load_orders()

# Task 13
print("\nTask 13 - Each Order:")
for order in orders:
    print(order)

# Task 14
quantity_sold = {}
for order in orders:
    pid = int(order["product_id"])
    qty = int(order["quantity"])
    quantity_sold[pid] = quantity_sold.get(pid, 0) + qty
print("\nTask 14 - Quantity Sold Per Product:")
print(quantity_sold)

# Task 15
orders_per_customer = {}
for order in orders:
    customer = order["customer"]
    orders_per_customer[customer] = orders_per_customer.get(customer, 0) + 1
print("\nTask 15 - Orders Per Customer:")
print(orders_per_customer)

# PART 4 SALES

# Task 16
print("\nTask 16 - Revenue Per Order:")
order_revenues = []
total_revenue = 0
revenue_per_product = {}
for order in orders:
    pid = int(order["product_id"])
    qty = int(order["quantity"])
    customer = order["customer"]
    revenue = calculate_product_revenue(pid, qty, product_dict)
    order_revenues.append(revenue)
    print("Order", order["order_id"], "-", revenue)

# Task 17 + 18 + 20
customer_spending = {}
for order in orders:
    pid = int(order["product_id"])
    qty = int(order["quantity"])
    customer = order["customer"]
    revenue = calculate_product_revenue(pid, qty, product_dict)
    total_revenue += revenue
    pname = product_dict[pid]["name"]
    revenue_per_product[pname] = revenue_per_product.get(pname, 0) + revenue
    customer_spending[customer] = customer_spending.get(customer, 0) + revenue
print("\nTask 17 - Total Revenue:")
print(total_revenue)

# Task 18
print("\nTask 18 - Revenue Per Product:")
print(revenue_per_product)

# Task 19
highest_product = max(revenue_per_product, key=revenue_per_product.get)

print("\nTask 19 - Highest Selling Product:")
print(highest_product)

# PART 5 CUSTOMER ANALYSIS

# Task 20
print("\nTask 20 - Customer Spending:")
print(customer_spending)

# Task 21
top_customer = find_top_customer(customer_spending)
print("\nTask 21 - Highest Spending Customer:")
print(top_customer)

# Task 22
print("\nTask 22 - Customers Spending > 50000")
for customer, amount in customer_spending.items():
    if amount > 50000:
        print(customer)

# PART 7 DATA STRUCTURES

product_revenue_tuples = []

for product, revenue in revenue_per_product.items():
    product_revenue_tuples.append((product, revenue))

print("\nPart 7 - Tuple Data:")
print(product_revenue_tuples)

# PART 8 SALES REPORT

with open("sales_report.txt", "w") as file:
    file.write("E-Commerce Sales Report\n")
    file.write("--------------------------\n")
    file.write("Total Website Visits: " + str(len(visits)) + "\n")
    file.write("Unique Visitors: " + str(len(unique_visitors)) + "\n")
    file.write("Total Revenue: " + str(total_revenue) + "\n\n")
    file.write("Top Customer: " + top_customer + "\n\n")
    file.write("Product Sales\n")
    for product, revenue in revenue_per_product.items():
        file.write(product + " -> " + str(revenue) + "\n")
print("\nSales report created successfully.")

# FINAL CHALLENGE

# Task 29
ordered_customers = set(orders_per_customer.keys())
never_ordered = unique_visitors - ordered_customers
print("\nTask 29 - Visited But Never Ordered:")
print(never_ordered)

# Task 30
print("\nTask 30 - Ordered But Never Visited More Than Once:")
for customer in ordered_customers:
    if visit_count.get(customer, 0) <= 1:
        print(customer)