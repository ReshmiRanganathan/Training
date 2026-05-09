from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def create_attendance_file():
    with open("/tmp/attendance.txt", "w") as f:
        f.write("Aarav,Present\n")
        f.write("Priya,Present\n")
        f.write("Rahul,Absent\n")
        f.write("Sneha,Present\n")
        f.write("Kiran,Absent\n")
        f.write("Ananya,Present\n")
        f.write("Vikram,Present\n")
        f.write("Meera,Absent\n")
        f.write("Farhan,Present\n")
        f.write("Divya,Present\n")

def read_attendance_file():
    with open("/tmp/attendance.txt", "r") as f:
        for line in f:
            print(line.strip())

def count_total_students():
    count = 0

    with open("/tmp/attendance.txt", "r") as f:
        for line in f:
            count += 1

    print(f"Total Students = {count}")

def count_present_students():
    present = 0

    with open("/tmp/attendance.txt", "r") as f:
        for line in f:
            if "Present" in line:
                present += 1

    print(f"Present Students = {present}")

def count_absent_students():
    absent = 0

    with open("/tmp/attendance.txt", "r") as f:
        for line in f:
            if "Absent" in line:
                absent += 1

    print(f"Absent Students = {absent}")

def calculate_attendance_percentage():
    total = 0
    present = 0

    with open("/tmp/attendance.txt", "r") as f:
        for line in f:
            total += 1

            if "Present" in line:
                present += 1

    percentage = (present / total) * 100

    print(f"Attendance Percentage = {percentage}%")

def list_absent_students():
    print("Absent Students List")

    with open("/tmp/attendance.txt", "r") as f:
        for line in f:
            name, status = line.strip().split(",")

            if status == "Absent":
                print(name)

def generate_attendance_report():
    total = 0
    present = 0
    absent = 0

    with open("/tmp/attendance.txt", "r") as f:
        for line in f:
            total += 1

            if "Present" in line:
                present += 1
            else:
                absent += 1

    percentage = (present / total) * 100

    if percentage >= 75:
        status = "Good"
    else:
        status = "Needs Improvement"

    with open("/tmp/attendance_report.txt", "w") as report:
        report.write("Daily Attendance Report\n")
        report.write(f"Total Students = {total}\n")
        report.write(f"Present Students = {present}\n")
        report.write(f"Absent Students = {absent}\n")
        report.write(f"Attendance Percentage = {percentage}%\n")
        report.write(f"Status = {status}\n")

with DAG(
    dag_id="attendance_processor_dag",
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    catchup=False
) as dag:

    t1 = PythonOperator(
        task_id="create_attendance_file",
        python_callable=create_attendance_file
    )

    t2 = PythonOperator(
        task_id="read_attendance_file",
        python_callable=read_attendance_file
    )

    t3 = PythonOperator(
        task_id="count_total_students",
        python_callable=count_total_students
    )

    t4 = PythonOperator(
        task_id="count_present_students",
        python_callable=count_present_students
    )

    t5 = PythonOperator(
        task_id="count_absent_students",
        python_callable=count_absent_students
    )

    t6 = PythonOperator(
        task_id="calculate_attendance_percentage",
        python_callable=calculate_attendance_percentage
    )

    t7 = PythonOperator(
        task_id="list_absent_students",
        python_callable=list_absent_students
    )

    t8 = PythonOperator(
        task_id="generate_attendance_report",
        python_callable=generate_attendance_report
    )

    t1 >> t2 >> t3 >> t4 >> t5 >> t6 >> t7 >> t8