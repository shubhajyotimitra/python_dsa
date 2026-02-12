import sqlite3
from datetime import datetime

# ---------------- DATABASE MANAGER ----------------
class DatabaseManager:
    def __init__(self, db_name="hospital.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS patients(
            patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            gender TEXT,
            contact TEXT,
            disease TEXT
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS doctors(
            doctor_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            specialization TEXT,
            contact TEXT
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS appointments(
            appointment_id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_id INTEGER,
            doctor_id INTEGER,
            date TEXT,
            FOREIGN KEY(patient_id) REFERENCES patients(patient_id),
            FOREIGN KEY(doctor_id) REFERENCES doctors(doctor_id)
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS bills(
            bill_id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_id INTEGER,
            amount REAL,
            date TEXT,
            FOREIGN KEY(patient_id) REFERENCES patients(patient_id)
        )
        """)
        self.conn.commit()

db = DatabaseManager()

# ---------------- PATIENT ----------------
class Patient:
    @staticmethod
    def add():
        try:
            name = input("Name: ")
            age = int(input("Age: "))
            gender = input("Gender: ")
            contact = input("Contact: ")
            disease = input("Disease: ")

            db.cursor.execute(
    """
    INSERT INTO patients (name, age, gender, contact, disease)
    VALUES (?, ?, ?, ?, ?)
    """,
    (name, age, gender, contact, disease)
)

            db.conn.commit()
            print("✅ Patient added successfully")

        except ValueError:
            print("❌ Invalid input! Age must be a number.")

    @staticmethod
    def view():
        db.cursor.execute("SELECT * FROM patients")
        records = db.cursor.fetchall()

        if not records:
            print("No patient records found.")
        for row in records:
            print(row)

# ---------------- DOCTOR ----------------
class Doctor:
    @staticmethod
    def add():
        name = input("Doctor Name: ")
        specialization = input("Specialization: ")
        contact = input("Contact: ")

        db.cursor.execute(
            "INSERT INTO doctors VALUES (NULL,?,?,?)",
            (name, specialization, contact)
        )
        db.conn.commit()
        print("✅ Doctor added successfully")

    @staticmethod
    def view():
        db.cursor.execute("SELECT * FROM doctors")
        for row in db.cursor.fetchall():
            print(row)

# ---------------- APPOINTMENT ----------------
class Appointment:
    @staticmethod
    def book():
        try:
            patient_id = int(input("Patient ID: "))
            doctor_id = int(input("Doctor ID: "))
            date = input("Date (YYYY-MM-DD): ")

            db.cursor.execute(
                "INSERT INTO appointments VALUES (NULL,?,?,?)",
                (patient_id, doctor_id, date)
            )
            db.conn.commit()
            print("✅ Appointment booked")

        except ValueError:
            print("❌ Invalid input!")

    @staticmethod
    def view():
        db.cursor.execute("""
        SELECT appointment_id, patients.name, doctors.name, date
        FROM appointments
        JOIN patients ON appointments.patient_id = patients.patient_id
        JOIN doctors ON appointments.doctor_id = doctors.doctor_id
        """)
        for row in db.cursor.fetchall():
            print(row)

# ---------------- BILLING ----------------
class Billing:
    @staticmethod
    def generate():
        try:
            patient_id = int(input("Patient ID: "))
            amount = float(input("Amount: "))
            date = datetime.now().strftime("%Y-%m-%d")

            db.cursor.execute(
                "INSERT INTO bills VALUES (NULL,?,?,?)",
                (patient_id, amount, date)
            )
            db.conn.commit()
            print("✅ Bill generated")

        except ValueError:
            print("❌ Invalid amount!")

    @staticmethod
    def view():
        db.cursor.execute("""
        SELECT bills.bill_id, patients.name, bills.amount, bills.date
        FROM bills
        JOIN patients ON bills.patient_id = patients.patient_id
        """)
        for row in db.cursor.fetchall():
            print(row)

# ---------------- MAIN MENU ----------------
def main():
    while True:
        print("\n--- HOSPITAL MANAGEMENT SYSTEM ---")
        print("1. Add Patient")
        print("2. View Patients")
        print("3. Add Doctor")
        print("4. View Doctors")
        print("5. Book Appointment")
        print("6. View Appointments")
        print("7. Generate Bill")
        print("8. View Bills")
        print("9. Exit")

        choice = input("Enter choice: ")

        match choice:
            case "1": Patient.add()
            case "2": Patient.view()
            case "3": Doctor.add()
            case "4": Doctor.view()
            case "5": Appointment.book()
            case "6": Appointment.view()
            case "7": Billing.generate()
            case "8": Billing.view()
            case "9":
                print("Exiting...")
                break
            case _:
                print("❌ Invalid choice")

if __name__ == "__main__":
    main()
    

