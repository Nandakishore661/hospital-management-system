
class Patient:
    def __init__(self, pid, name, age, gender, phone):
        self.pid = pid
        self.name = name
        self.age = age
        self.gender = gender
        self.phone = phone

    def display_details(self):
        print("\nPatient ID   :", self.pid)
        print("Patient Name :", self.name)
        print("Age          :", self.age)
        print("Gender       :", self.gender)
        print("Phone Number :", self.phone)


class Doctor:
    def __init__(self, did, name, specialization, phone):
        self.did = did
        self.name = name
        self.specialization = specialization
        self.phone = phone

    def display_details(self):
        print("\nDoctor ID      :", self.did)
        print("Doctor Name    :", self.name)
        print("Specialization :", self.specialization)
        print("Phone Number   :", self.phone)


class Appointment:
    def __init__(self, aid, pid, did, date, time):
        self.aid = aid
        self.pid = pid
        self.did = did
        self.date = date
        self.time = time

    def display_details(self):
        print("\nAppointment ID :", self.aid)
        print("Patient ID     :", self.pid)
        print("Doctor ID      :", self.did)
        print("Date           :", self.date)
        print("Time           :", self.time)


class MedicalRecord:
    def __init__(self, rid, pid, did, diagnosis, treatment):
        self.rid = rid
        self.pid = pid
        self.did = did
        self.diagnosis = diagnosis
        self.treatment = treatment

    def display_details(self):
        print("\nRecord ID  :", self.rid)
        print("Patient ID :", self.pid)
        print("Doctor ID  :", self.did)
        print("Diagnosis  :", self.diagnosis)
        print("Treatment  :", self.treatment)


class HospitalManagement:

    def __init__(self):
        self.patients = []
        self.doctors = []
        self.appointments = []
        self.records = []

        self.load_patients()
        self.load_doctors()
        self.load_appointments()
        self.load_records()

    # ================= PATIENT FILE HANDLING =================

    def load_patients(self):
        self.patients = []

        try:
            file = open("patients.txt", "r")

            for line in file:
                if line.strip() != "":
                    data = line.strip().split("|")

                    if len(data) == 5:
                        p = Patient(
                            data[0], data[1], data[2],
                            data[3], data[4]
                        )
                        self.patients.append(p)

            file.close()

        except FileNotFoundError:
            pass

    def save_patients(self):
        file = open("patients.txt", "w")

        for p in self.patients:
            file.write(
                p.pid + "|" + p.name + "|" + p.age + "|" +
                p.gender + "|" + p.phone + "\n"
            )

        file.close()

    # ================= DOCTOR FILE HANDLING =================

    def load_doctors(self):
        self.doctors = []

        try:
            file = open("doctors.txt", "r")

            for line in file:
                if line.strip() != "":
                    data = line.strip().split("|")

                    if len(data) == 4:
                        d = Doctor(
                            data[0], data[1], data[2], data[3]
                        )
                        self.doctors.append(d)

            file.close()

        except FileNotFoundError:
            pass

    def save_doctors(self):
        file = open("doctors.txt", "w")

        for d in self.doctors:
            file.write(
                d.did + "|" + d.name + "|" +
                d.specialization + "|" + d.phone + "\n"
            )

        file.close()

    # ================= APPOINTMENT FILE HANDLING =================

    def load_appointments(self):
        self.appointments = []

        try:
            file = open("appointments.txt", "r")

            for line in file:
                if line.strip() != "":
                    data = line.strip().split("|")

                    if len(data) == 5:
                        a = Appointment(
                            data[0], data[1], data[2],
                            data[3], data[4]
                        )
                        self.appointments.append(a)

            file.close()

        except FileNotFoundError:
            pass

    def save_appointments(self):
        file = open("appointments.txt", "w")

        for a in self.appointments:
            file.write(
                a.aid + "|" + a.pid + "|" + a.did + "|" +
                a.date + "|" + a.time + "\n"
            )

        file.close()

    # ================= MEDICAL RECORD FILE HANDLING =================

    def load_records(self):
        self.records = []

        try:
            file = open("records.txt", "r")

            for line in file:
                if line.strip() != "":
                    data = line.strip().split("|")

                    if len(data) == 5:
                        r = MedicalRecord(
                            data[0], data[1], data[2],
                            data[3], data[4]
                        )
                        self.records.append(r)

            file.close()

        except FileNotFoundError:
            pass

    def save_records(self):
        file = open("records.txt", "w")

        for r in self.records:
            file.write(
                r.rid + "|" + r.pid + "|" + r.did + "|" +
                r.diagnosis + "|" + r.treatment + "\n"
            )

        file.close()

    # ================= ADD PATIENT =================

    def add_patient(self):
        print("\n========== ADD PATIENT ==========")

        pid = input("Enter Patient ID: ")

        for p in self.patients:
            if p.pid == pid:
                print("Patient ID Already Exists!")
                return

        name = input("Enter Patient Name: ")
        age = input("Enter Age: ")
        gender = input("Enter Gender: ")
        phone = input("Enter Phone Number: ")

        p = Patient(pid, name, age, gender, phone)

        self.patients.append(p)
        self.save_patients()

        print("\nPatient Added Successfully!")

    # ================= VIEW PATIENTS =================

    def view_patients(self):
        print("\n========== PATIENT DETAILS ==========")

        if len(self.patients) == 0:
            print("No Patient Records Found!")
        else:
            for p in self.patients:
                p.display_details()
                print("--------------------------------")

    # ================= SEARCH PATIENT =================

    def search_patient(self):
        pid = input("Enter Patient ID to Search: ")

        for p in self.patients:
            if p.pid == pid:
                print("\nPatient Found!")
                p.display_details()
                return

        print("Patient Not Found!")

    # ================= UPDATE PATIENT =================

    def update_patient(self):
        pid = input("Enter Patient ID to Update: ")

        for p in self.patients:
            if p.pid == pid:
                p.name = input("Enter New Name: ")
                p.age = input("Enter New Age: ")
                p.gender = input("Enter New Gender: ")
                p.phone = input("Enter New Phone Number: ")

                self.save_patients()

                print("Patient Updated Successfully!")
                return

        print("Patient Not Found!")

    # ================= DELETE PATIENT =================

    def delete_patient(self):
        pid = input("Enter Patient ID to Delete: ")

        for p in self.patients:
            if p.pid == pid:
                self.patients.remove(p)
                self.save_patients()

                print("Patient Deleted Successfully!")
                return

        print("Patient Not Found!")

    # ================= ADD DOCTOR =================

    def add_doctor(self):
        print("\n========== ADD DOCTOR ==========")

        did = input("Enter Doctor ID: ")

        for d in self.doctors:
            if d.did == did:
                print("Doctor ID Already Exists!")
                return

        name = input("Enter Doctor Name: ")
        specialization = input("Enter Specialization: ")
        phone = input("Enter Phone Number: ")

        d = Doctor(did, name, specialization, phone)

        self.doctors.append(d)
        self.save_doctors()

        print("Doctor Added Successfully!")

    # ================= VIEW DOCTORS =================

    def view_doctors(self):
        print("\n========== DOCTOR DETAILS ==========")

        if len(self.doctors) == 0:
            print("No Doctor Records Found!")
        else:
            for d in self.doctors:
                d.display_details()
                print("--------------------------------")

    # ================= BOOK APPOINTMENT =================

    def book_appointment(self):
        print("\n========== BOOK APPOINTMENT ==========")

        aid = input("Enter Appointment ID: ")

        for a in self.appointments:
            if a.aid == aid:
                print("Appointment ID Already Exists!")
                return

        pid = input("Enter Patient ID: ")
        patient_found = False

        for p in self.patients:
            if p.pid == pid:
                patient_found = True
                break

        if patient_found == False:
            print("Patient Not Found!")
            return

        did = input("Enter Doctor ID: ")
        doctor_found = False

        for d in self.doctors:
            if d.did == did:
                doctor_found = True
                break

        if doctor_found == False:
            print("Doctor Not Found!")
            return

        date = input("Enter Appointment Date: ")
        time = input("Enter Appointment Time: ")

        a = Appointment(aid, pid, did, date, time)

        self.appointments.append(a)
        self.save_appointments()

        print("Appointment Booked Successfully!")

    # ================= VIEW APPOINTMENTS =================

    def view_appointments(self):
        print("\n========== APPOINTMENT DETAILS ==========")

        if len(self.appointments) == 0:
            print("No Appointments Found!")
        else:
            for a in self.appointments:
                a.display_details()
                print("--------------------------------")

    # ================= ADD MEDICAL RECORD =================

    def add_record(self):
        print("\n========== ADD MEDICAL RECORD ==========")

        rid = input("Enter Record ID: ")

        for r in self.records:
            if r.rid == rid:
                print("Record ID Already Exists!")
                return

        pid = input("Enter Patient ID: ")
        patient_found = False

        for p in self.patients:
            if p.pid == pid:
                patient_found = True
                break

        if patient_found == False:
            print("Patient Not Found!")
            return

        did = input("Enter Doctor ID: ")
        doctor_found = False

        for d in self.doctors:
            if d.did == did:
                doctor_found = True
                break

        if doctor_found == False:
            print("Doctor Not Found!")
            return

        diagnosis = input("Enter Diagnosis: ")
        treatment = input("Enter Treatment: ")

        r = MedicalRecord(
            rid, pid, did, diagnosis, treatment
        )

        self.records.append(r)
        self.save_records()

        print("Medical Record Added Successfully!")

    # ================= VIEW MEDICAL RECORDS =================

    def view_records(self):
        print("\n========== MEDICAL RECORD DETAILS ==========")

        if len(self.records) == 0:
            print("No Medical Records Found!")
        else:
            for r in self.records:
                r.display_details()
                print("--------------------------------")


# ================= MAIN PROGRAM =================

h = HospitalManagement()

while True:

    print("\n========== HOSPITAL MANAGEMENT SYSTEM ==========")
    print("1. Add Patient")
    print("2. View Patients")
    print("3. Search Patient")
    print("4. Update Patient")
    print("5. Delete Patient")
    print("6. Add Doctor")
    print("7. View Doctors")
    print("8. Book Appointment")
    print("9. View Appointments")
    print("10. Add Medical Record")
    print("11. View Medical Records")
    print("12. Exit")

    try:
        choice = int(input("\nEnter Your Choice: "))

        if choice == 1:
            h.add_patient()

        elif choice == 2:
            h.view_patients()

        elif choice == 3:
            h.search_patient()

        elif choice == 4:
            h.update_patient()

        elif choice == 5:
            h.delete_patient()

        elif choice == 6:
            h.add_doctor()

        elif choice == 7:
            h.view_doctors()

        elif choice == 8:
            h.book_appointment()

        elif choice == 9:
            h.view_appointments()

        elif choice == 10:
            h.add_record()

        elif choice == 11:
            h.view_records()

        elif choice == 12:
            print("\nThank You for Using Hospital Management System!")
            print("Program Exited Successfully.")
            break

        else:
            print("Invalid Choice! Please Try Again.")

    except ValueError:
        print("Please Enter a Valid Number!")
