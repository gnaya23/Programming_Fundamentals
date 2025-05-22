#!/usr/bin/env python3
from dataclasses import dataclass

@dataclass
class Client:

    def __init__(self, client_id: int, first_name: str, last_name: str, phone: str, email: str, address: str):
        self.client_id = client_id
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.address = address
        
class Pet:
    def __init__(self, pet_id: int, name: str, breed: str, species: str, age: int, gender: str, client_id: int):
        self.pet_id = pet_id
        self.name = name
        self.breed = breed
        self.species = species
        self.age = age
        self.gender = gender
        self.client_id = client_id

class Appointment:
    def __init__(self, date: str, time: str, pet_id: int, client_id: int,reason: str,notes: str,vet_id:int= None, app_id:int= None):
        self.app_id = app_id
        self.date = date
        self.time = time
        self.pet_id = pet_id
        self.client_id = client_id
        self.reason = reason
        self.notes = notes
        self.vet_id = vet_id


class Staff:
    def __init__(self, vet_id: int, name: str, position: str, phone: str, email: str):
        self.vet_id = vet_id
        self.name = name
        self.position = position
        self.phone = phone
        self.email = email


class MedicalHistory:
    def __init__(self, record_id: int, pet_id: int, date: str, diagnosis: str, treatment: str, medication: str, notes: str):
        self.record_id = record_id
        self.pet_id = pet_id
        self.date = date
        self.diagnosis = diagnosis
        self.treatment = treatment
        self.medication = medication
        self.notes = notes

class Billing:
    def __init__(self, invoice_id: int, client_id: int, date: str, total_amount: float, payment_status: str):
        self.invoice_id = invoice_id
        self.client_id = client_id
        self.date = date
        self.total_amount = total_amount
        self.payment_status = payemnt_status
    

    
    
    
    
    
