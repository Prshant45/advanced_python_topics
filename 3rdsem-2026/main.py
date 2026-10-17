from mysql_database.database import Database


db = Database(host='localhost', port=3306,
              user='root', password='Admin@123',
              database='employee')

result = db.execute_query("SELECT * FROM employee")
for row in result:
    print(row)

result = db.insert("INSERT INTO employee (employee_name, email, salary, hire_date, department_id) VALUES (%s, %s, %s, %s, %s)",
                   ("John Doe", "john.doe@example.com", 50000, "2023-01-01", 2))
print(f"Inserted row ID: {result}")