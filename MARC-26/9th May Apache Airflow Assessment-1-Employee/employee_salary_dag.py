from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def create_employee_file():
    with open("/tmp/employees.txt", "w") as f:
        f.write("Rahul,45000\n")
        f.write("Sneha,52000\n")
        f.write("Amit,61000\n")
        f.write("Priya,47000\n")
        f.write("Kiran,39000\n")

def read_employee_data():
    with open("/tmp/employees.txt", "r") as f:
        for line in f:
            print(line.strip())

def calculate_salary_expense():
    total = 0

    with open("/tmp/employees.txt", "r") as f:
        for line in f:
            salary = int(line.strip().split(",")[1])
            total += salary

    print(f"Total Salary Expense = {total}")
    return total

def find_highest_salary():
    highest_salary = 0
    highest_employee = ""

    with open("/tmp/employees.txt", "r") as f:
        for line in f:
            name, salary = line.strip().split(",")
            salary = int(salary)

            if salary > highest_salary:
                highest_salary = salary
                highest_employee = name

    print(f"Highest Salary = {highest_salary}")
    print(f"Employee = {highest_employee}")

def generate_salary_report():
    total_salary = 0
    employee_count = 0

    with open("/tmp/employees.txt", "r") as f:
        for line in f:
            employee_count += 1
            total_salary += int(line.strip().split(",")[1])

    with open("/tmp/salary_report.txt", "w") as report:
        report.write("Employee Salary Report\n")
        report.write(f"Total Employees = {employee_count}\n")
        report.write(f"Total Salary Expense = {total_salary}\n")
        report.write("Status = Processed Successfully\n")

with DAG(
    dag_id="employee_salary_dag",
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    catchup=False
) as dag:

    t1 = PythonOperator(
        task_id="create_employee_file",
        python_callable=create_employee_file
    )

    t2 = PythonOperator(
        task_id="read_employee_data",
        python_callable=read_employee_data
    )

    t3 = PythonOperator(
        task_id="calculate_salary_expense",
        python_callable=calculate_salary_expense
    )

    t4 = PythonOperator(
        task_id="find_highest_salary",
        python_callable=find_highest_salary
    )

    t5 = PythonOperator(
        task_id="generate_salary_report",
        python_callable=generate_salary_report
    )

    t1 >> t2 >> t3 >> t4 >> t5