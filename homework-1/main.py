"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv

with psycopg2.connect(host='localhost', database='north', user='postgres', password="") as conn:
    with conn.cursor() as cur:
        with open('north_data/employees_data.csv', 'r') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                cur.execute(
                    "insert into employees(employee_id,first_name,last_name,title,birth_date,notes) values(%s,%s,%s,"
                    "%s,%s,%s)",
                    row)
        with open('north_data/customers_data.csv', 'r') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                cur.execute(
                    "insert into customers(customer_id,company_name,contact_name) values(%s,%s,%s)",
                    row)

        with open('north_data/orders_data.csv', 'r') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                cur.execute(
                    "insert into orders(order_id,customer_id,employee_id,order_date,ship_city) values(%s,%s,%s,%s,%s)",
                    row)

conn.close()
