# Hospital Patient Management System
# OOP + Exception Handling


class Patient:

    def __init__(self, patient_id, name, age, disease):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.disease = disease

    def display_patient(self):
        print("\n===== PATIENT DETAILS =====")
        print("Patient ID:", self.patient_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Disease:", self.disease)


class Hospital:

    def __init__(self):
        self.patients = []

    def add_patient(self):
        try:
            patient_id = int(input("Enter patient ID: "))

            name = input("Enter patient name: ").strip()

            if name == "":
                raise ValueError("Patient name cannot be empty.")

            age = int(input("Enter patient age: "))

            if age <= 0 or age > 120:
                raise ValueError("Please enter a valid age.")

            disease = input("Enter disease: ").strip()

            if disease == "":
                raise ValueError("Disease cannot be empty.")

            patient = Patient(patient_id, name, age, disease)

            self.patients.append(patient)

        except ValueError as error:
            print("Error:", error)

        else:
            print("Patient added successfully.")

        finally:
            print("Add patient operation completed.")

    def view_patients(self):

        try:
            if len(self.patients) == 0:
                raise Exception("No patients available.")

            print("\n===== ALL PATIENTS =====")

            for patient in self.patients:
                print(
                    "ID:", patient.patient_id,
                    "| Name:", patient.name,
                    "| Age:", patient.age,
                    "| Disease:", patient.disease
                )

        except Exception as error:
            print("Error:", error)

        finally:
            print("View patient operation completed.")

    def search_patient(self):

        try:
            patient_id = int(input("Enter patient ID to search: "))

            found = False

            for patient in self.patients:

                if patient.patient_id == patient_id:
                    patient.display_patient()
                    found = True
                    break

            if not found:
                raise Exception("Patient not found.")

        except ValueError:
            print("Please enter a valid patient ID.")

        except Exception as error:
            print("Error:", error)

        finally:
            print("Search operation completed.")

    def delete_patient(self):

        try:
            patient_id = int(input("Enter patient ID to delete: "))

            for patient in self.patients:

                if patient.patient_id == patient_id:
                    self.patients.remove(patient)
                    print("Patient deleted successfully.")
                    break

            else:
                raise Exception("Patient not found.")

        except ValueError:
            print("Please enter a valid patient ID.")

        except Exception as error:
            print("Error:", error)

        finally:
            print("Delete operation completed.")


def main():

    hospital = Hospital()

    while True:

        print("\n===== HOSPITAL PATIENT MANAGEMENT SYSTEM =====")
        print("1. Add Patient")
        print("2. View Patients")
        print("3. Search Patient")
        print("4. Delete Patient")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))

        except ValueError:
            print("Please enter a number between 1 and 5.")
            continue

        if choice == 1:
            hospital.add_patient()

        elif choice == 2:
            hospital.view_patients()

        elif choice == 3:
            hospital.search_patient()

        elif choice == 4:
            hospital.delete_patient()

        elif choice == 5:
            print("Thank you for using the Hospital Patient Management System.")
            break

        else:
            print("Invalid choice. Please select 1 to 5.")


main()