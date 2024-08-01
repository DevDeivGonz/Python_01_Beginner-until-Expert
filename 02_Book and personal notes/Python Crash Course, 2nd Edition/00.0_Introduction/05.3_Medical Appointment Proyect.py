def clear_console():
    print("\n" * 5)


def display_hospital_menu():
    hospitals = {
        1: "Fundación Santa Fe                 | La Esmeralda #24-9, Teusaquillo, Bogotá",
        2: "Fundación Cardio Infantil          | Cl. 163a #13B-60, Bogotá",
        3: "Fundación Clínica Shaio            | Dg. 115a #70c - 75, Bogotá",
        4: "Hospital Universitario San Ignacio | Kra 7° #40-62, Bogotá",
        5: "Clínica Del Country                | Cra. 16 #82-95, Chapinero, Bogotá, Cundinamarca"
    }

    while True:
        print("\nMenu of Hospitals Available:")
        for key, value in hospitals.items():
            print(f"{key}: {value}")

        choice_hospital = int(input("Enter your hospital choice by number (1-5) or 0 to exit: "))

        if choice_hospital in hospitals:
            return hospitals[choice_hospital]
        elif choice_hospital == 0:
            return None
        else:
            print("Invalid choice. Please choose a valid option.")


def add_medical_appointment():
    medical_appointments = {}

    while True:
        requested = input("""
        Hello, welcome!
        Do you want to make a medical appointment?
        If you would like to proceed please ENTER "yes", otherwise ENTER "finish"
        """)
        if requested.lower() == "finish":
            print("Thanks for choosing us, have a nice day.")
            break

        id_identification = int(input("Enter your ID identification:\n"))
        first_name_and_last_name = input("Enter your first name and last name:\n")
        date_of_medical_appointment = input("Enter the date you would like to assign for your medical appointment, (YYYY-MM-DD):\n")

        hospital_chosen = display_hospital_menu()
        if hospital_chosen:
            medical_appointments[id_identification] = {
                "first_name_and_last_name": first_name_and_last_name,
                "date_of_medical_appointment": date_of_medical_appointment,
                "hospital_available": hospital_chosen
            }
            print(f"\n\n\nAppointment successfully added for {first_name_and_last_name.upper()} at {hospital_chosen.upper()} on {date_of_medical_appointment}.")
            print(f"\nThanks for choose us {first_name_and_last_name.upper()}, have a nice day\n")
        else:
            print("No hospital chosen. Returning to main menu.")

    return medical_appointments


# Collecting user data
appointments = add_medical_appointment()

# Printing the appointments
for key, value in appointments.items():
    print(f"ID {key}")
    for sub_key, sub_value in value.items():
        print(f"  {sub_key}: {sub_value}")

clear_console()
