"""Database Management Banking"""
import mysql.connector as sql

mydb = sql.connect(
    host="localhost",
    user="root",
    passwd='pass',
    database="blood_bank",
    auth_plugin='mysql_native_password'
)

cursor = mydb.cursor()


def db_query(query, status=True):
    cursor.execute(query)
    if status:
        return cursor.fetchall()


def create_tables():
    donor_table = """CREATE TABLE IF NOT EXISTS donor (
        donor_id INT AUTO_INCREMENT PRIMARY KEY,
        donor_name VARCHAR(30),
        donor_age INT,
        donor_blood_type VARCHAR(5) 
    )"""

    inventory_table = """CREATE TABLE IF NOT EXISTS inventory (
            blood_id INT AUTO_INCREMENT PRIMARY KEY,
            blood_type VARCHAR(5),
            quantity INT DEFAULT 1
        )"""

    inventory_table_rows = """INSERT INTO inventory (blood_type) VALUES
            ('A+'), ('A-'), ('B+'), ('B-'), ('AB+'), ('AB-'), ('O+'), ('O-');"""

    request_table = """CREATE TABLE IF NOT EXISTS request (
            request_id INT AUTO_INCREMENT PRIMARY KEY,
            hospital_name VARCHAR(30),
            patient_name VARCHAR(30),
            patient_age INT,
            patient_blood_type VARCHAR(5) ,
            donor_name VARCHAR(30),
            donor_age INT,
            donor_blood_type VARCHAR(5) 
        )"""

    cursor.execute(donor_table)
    cursor.execute(inventory_table)
    cursor.execute(inventory_table_rows)
    cursor.execute(request_table)
    mydb.commit()


if __name__ == "__main__":
    create_tables()
