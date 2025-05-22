#!/usr/bin/env python3

import clinic
from objects import Client, Pet, Appointment, Staff, MedicalHistory, Billing

def display_title():
    print()
    print("\t\t\t\t\t\t\tWelcome to Pawsitive Care Veterinary Clinic!")
    print()
    print("\t\t\t\tWe are dedicated to providing compassionate, expert care to ensure the health and happiness of your pets.\n\t\t\t\t\tWith our pawsitive approach, we prioritize their well-being every step of the way.")
    print("---------------------------------------------------------------------------------------------------------------------------------------------------------")

def display_menu():
    print()
    print("======================")
    print("\tMENU")
    print("======================")
    print("1 - View Personal & Pet Info")
    print("2 - Edit Personal Info")
    print("3 - Register New Personal & Pet Info")
    print("4 - View Pet Medical History")
    print("5 - Schedule Appointment")
    print("6 - Exit Program")
    print()

def view_personal_pet_info(client_list, pet_list):
    print("Enter your first and last name to find your information: ")
    first_name = input("Enter first name: ").strip().title()
    last_name = input("Enter last name: ").strip().title()

    find_client = [client for client in client_list if client.first_name == first_name and client.last_name == last_name] 
    
    
    if not find_client:
        print("Client not found.")
        return

    client = find_client[0]
    print()
    print("===Client Personal Information===")
    print(f"Name: {client.first_name} {client.last_name}\nPhone: {client.phone}\nEmail: {client.email}\nAddress: {client.address}")
    print()
    print(f"===Pet Information===")

    client_pet = [pet for pet in pet_list if pet.client_id == client.client_id]
        
    if client_pet:
        for pet in client_pet:
            print(f"Pet ID: {pet.pet_id}\nName: {pet.name}\nBreed: {pet.breed}\nSpecies: {pet.species}\nAge: {pet.age}\nGender: {pet.gender}\nClientID: {pet.client_id}")
    else:
        print("No pet found.")
def edit_personal_info(client_list):
    print("Enter your first and last name to edit your information: ")
    first_name = input("Enter first name: ").strip().title()
    last_name = input("Enter last name: ").strip().title()

    find_client = [client for client in client_list if client.first_name == first_name and client.last_name == last_name] 
    
    
    if not find_client:
        print("Client not found.")
        return

    client = find_client[0]
    print()
    print("===Client Personal Information===")
    print(f"Name: {client.first_name} {client.last_name}\nPhone: {client.phone}\nEmail: {client.email}\nAddress: {client.address}")
    print()
    change = input("If you would like to make a change to your information, please enter one of the following commands: phone, email, or address.\n")

    if change == "phone":
        old_phone = client.phone
        new_phone = input("Enter new phone number: ")
        client.phone = new_phone
        print(f"Your phone number has been update to {new_phone}.")
 
    elif change == "email":
        old_email = client.email
        new_email = input("Enter new email: ")
        client.email = new_email
        print(f"Your email has been update to {new_email}.")
    elif change == "address":
        old_address = client.address
        new_address = input("Enter new address: ")
        client.address = new_address
        print(f"Your address has been update to {new_address}.")
    print()
    print("For changes regarding your name or pet information, please contact our office.")

def register_new():
    print()
    print("We are excited for you to join Pawsitive Care Veterinary Clinic! To begin, please enter your information below.")
    first_name = input("Enter your first name: ").strip().title()
    last_name = input("Enter your last name: ").strip().title()
    phone = input("Enter your phone number: ").strip()
    email = input("Enter your email address: ").strip()
    address = input("Enter your home address: ").strip()


    
    print("Now, please enter your pet's information. ")
    name = input("Enter your pet's name: ").strip().title()
    breed = input("Enter your pet's breed: ").strip().title()
    species = input("Enter your pet's species: ").strip().title()
    age = int(input("Enter your pet's age: "))
    gender = input("Enter your pet's gender: ").strip().title()

    client = Client(None, first_name, last_name, phone, email, address)
    client_id = clinic.add_client(client)

    client_list = clinic.get_clients()

    pet = Pet(None, name, breed, species, age, gender, client_id)
    clinic.add_pet(pet)

    pet_list = clinic.get_pets()
    print("Thank you! Your profile is created! You can view it by entering menu option 1")

def view_pet_history(pet_list):
    print()
    pet_id = input("Enter your pet's ID to find their medical history. This can be found in Personal/Pet Info.\n")
  
    try:
        pet_id = int(pet_id)
    except ValueError:
        print("Invalid pet ID. Please try again.")
        return

    pet = None
    for p in pet_list:
        if p.pet_id == pet_id:
            pet = p
            break

    if not pet:
        print("Pet not found.")
        return

    history_list = clinic.get_pet_history()
    app_list = clinic.get_app()

    pet_history = [record for record in history_list if record.pet_id == pet.pet_id]
    pet_app = [appointment for appointment in app_list if appointment.pet_id == pet.pet_id]
    print(f"==={pet.name}'s Medical History===")

    if not pet_history:
        print("No medical history available.")
        
    
    for record in pet_history:
        print(f"Pet ID: {record.pet_id}\nDate: {record.date}\nDiagnosis: {record.diagnosis}\nTreatment: {record.treatment}\nMedication: {record.medication}\nNotes: {record.notes}")
    print()
    print(f"==={pet.name}'s Appointments===")

    if not pet_app:
        print("No appointments found.")
    else:
        for appointment in pet_app:
            print(f"Date: {appointment.date}\nTime: {appointment.time}\nPet ID: {appointment.pet_id}\nClient ID: {appointment.client_id}\nReason: {appointment.reason}\nNotes: {appointment.notes}")


def schedule_app(client_list):
    print()
    print("To schedule an appointment with us, fill in the information below.")

    try:
        client_id = int(input("Enter your ID number to schedule: "))
    except ValueError:
        print("Invalid ID. Must be a number.")
        return

    client = (c for c in client_list if c.client_id == client_id)
    for c in client_list:
        if c.client_id == client_id:
            client = c
            break
    if not client:
        print("Client ID was not found. You must be registered with our clinic. To register, please enter menu option 3")
        return

    available_apps = [
        {"date": "05/26/2025", "time":"8:00 AM"},
        {"date": "05/27/2025", "time":"9:00 AM"},
        {"date": "05/28/2025", "time":"10:00 AM"},
        {"date": "05/29/2025", "time":"11:00 AM"},
        {"date": "05/30/2025", "time":"1:00 PM"},
    ]

    for i, appointment in enumerate(available_apps, start=1):
        print(f"{i}. {appointment['date']} at {appointment['time']}")
    try:
        selected = int(input("Enter the number of date and time you'd like to choose: "))
        if selected < 1 or selected > len(available_apps):
            print("Invalid selection. Please try again.")
            return
        selected_choice = available_apps[selected-1]
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    pet_id = int(input("Enter your pet's ID: "))
    reason = input("Enter the reason for this visit: ")
    notes = input("If you would like to leave any notes, type them here. To skip this question, press enter.\n")

    app = Appointment(date=selected_choice["date"],
                      time=selected_choice["time"],
                      pet_id=pet_id,
                      client_id=client_id,
                      reason=reason,
                      notes=notes)
    confirm = input(f"To confirm your appointment: {selected_choice["date"]} at {selected_choice["time"]}. Please enter 'yes'/'no'.").lower()     
    if confirm == "yes" or confirm == "y":
        clinic.add_app(app)
        print("Thank you for scheduling with Pawsitive Care Veterinary Care Clinic! We look forward to seeing you!")
    elif confirm == "no" or confirm == "n":
        print("Confirmation Cancelled.")
    else:
        print("Invalid input. Please try again.")    
        
def main():
    display_title()
    display_menu()

    clinic.connect()

    client_list = clinic.get_clients()
    pet_list = clinic.get_pets()

    while True:
        command = input("Enter Menu Option: ")
        if command == "1":
            view_personal_pet_info(client_list, pet_list)
        elif command == "2":
            edit_personal_info(client_list)
        elif command == "3":
            register_new()
        elif command == "4":
            view_pet_history(pet_list)
        elif command == "5":
            schedule_app(client_list)
        elif command == "6":
            print()
            break 
        else:
            print("Invalid Menu Option. Please try again.")
            display_menu()
    print("Thank you for visiting Pawsitive Care Veterinary Clinic!")
      
main()
