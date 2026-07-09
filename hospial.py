patients = []

def add_patient():
    patient_id = input("Enter Patient ID: ")
    name = input("Enter Patient Name: ")
    age = input("Enter Patient Age: ")
    disease = input("Enter Disease: ")

    patient = {
        "ID": patient_id,
        "Name": name,
        "Age": age,
        "Disease": disease
    }

    patients.append(patient)
    print("\n✅ Patient Added Successfully!\n")


def view_patients():
    if len(patients) == 0:
        print("\nNo Patients Found!\n")
    else:
        print("\n------ Patient List ------")
        for patient in patients:
            print(f"ID       : {patient['ID']}")
            print(f"Name     : {patient['Name']}")
            print(f"Age      : {patient['Age']}")
            print(f"Disease  : {patient['Disease']}")
            print("--------------------------")


def search_patient():
    search_id = input("Enter Patient ID to Search: ")

    for patient in patients:
        if patient["ID"] == search_id:
            print("\nPatient Found")
            print(f"ID       : {patient['ID']}")
            print(f"Name     : {patient['Name']}")
            print(f"Age      : {patient['Age']}")
            print(f"Disease  : {patient['Disease']}")
            return

    print("\n❌ Patient Not Found!\n")


def delete_patient():
    delete_id = input("Enter Patient ID to Delete: ")

    for patient in patients:
        if patient["ID"] == delete_id:
            patients.remove(patient)
            print("\n✅ Patient Deleted Successfully!\n")
            return

    print("\n❌ Patient Not Found!\n")


while True:
    print("\n========== Hospital Management System ==========")
    print("1. Add Patient")
    print("2. View Patients")
    print("3. Search Patient")
    print("4. Delete Patient")
    print("5. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_patient()

    elif choice == "2":
        view_patients()

    elif choice == "3":
        search_patient()

    elif choice == "4":
        delete_patient()

    elif choice == "5":
        print("\nThank You! Visit Again.")
        break

    else:
        print("\n❌ Invalid Choice! Try Again.\n")