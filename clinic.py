#!/usr/bin/env python3

import sqlite3

from contextlib import closing

from objects import Client, Pet, Appointment, Staff, MedicalHistory, Billing

conn = None

def connect():
    global conn
    if not conn:
        DB_FILE = "clinic.db"
        conn = sqlite3.connect(DB_FILE)
        conn.row_factory = sqlite3.Row


def close():
    global conn
    if conn:
        conn.close()
        conn = None

def make_client(row):
    return Client(row["ClientID"],row["firstName"], row["lastName"],
                  row["phoneNum"], row["email"], row["address"])

def make_pet(row):
    return Pet(row["PetID"],row["name"], row["breed"], row["species"],
               row["age"], row["gender"], row["ClientID"])

def make_app(row):
    return Appointment(row["AppID"],row["AppID"],row["date"],row["time"],row["reason"],row["notes"],row["PetID"],row["ClientID"])
                     
def make_medical_history(row):
    return MedicalHistory(row["RecordID"],row["PetID"],row["date"],row["diagnosis"],
                           row["treatment"],row["medication"],row["notes"])

def get_clients():
    query = '''SELECT ClientID, firstName, lastName, phoneNum, email, address
                FROM client'''
    with closing(conn.cursor()) as c:
        c.execute(query)
        results = c.fetchall()

        clients = []
        for row in results:
            client = make_client(row)
            clients.append(client)
        return clients

def get_pets():
    query = '''SELECT PetID, name, breed, species, age, gender, ClientID
                FROM pet'''
    with closing(conn.cursor()) as c:
        c.execute(query)
        results = c.fetchall()

        pets = []
        for row in results:
            pet = make_pet(row)
            pets.append(pet)
        return pets

def get_pet_history():
    query = '''SELECT RecordID, PetID, date, diagnosis, treatment, medication, notes
                FROM medical_history'''
    with closing(conn.cursor()) as c:
        c.execute(query)
        results = c.fetchall()

        medical_history = []
        for row in results:
            history = make_medical_history(row)
            medical_history.append(history)
        return medical_history

def get_app():
    query = '''SELECT AppID, date, time, PetID, ClientID, reason, notes, VetID
                FROM appointment'''
    with closing(conn.cursor()) as c:
        c.execute(query)
        results = c.fetchall()
        appointments = []
        for row in results:
            app = make_app(row)
            appointments.append(app)
        return appointments

def update_personal_info(client):
    query = '''UPDATE client
                SET phoneNum = ?, email = ?, address = ?
                WHERE ClientID = ?'''
    with closing(conn.cursor()) as c:
        values = (client.phone, client.email, client.address, client.client_id)
        c.execute(query,values)
        conn.commit()

def add_client(client):
    sql = '''INSERT INTO client
                (firstName, lastName, phoneNum,email,address)
            VALUES(?,?,?,?,?)'''
    with closing(conn.cursor()) as c:
        c.execute(sql, (client.first_name, client.last_name, client.phone, client.email, client.address))
        conn.commit()
        return c.lastrowid

def add_pet(pet):
    sql = '''INSERT INTO pet
                (name,breed,species,age,gender,ClientID)
            VALUES(?,?,?,?,?,?)'''
    with closing(conn.cursor()) as c:
        c.execute(sql, (pet.name, pet.breed, pet.species, pet.age, pet.gender, pet.client_id))
        conn.commit()

def add_app(app):
    sql = '''INSERT INTO appointment
                (date, time, PetID, ClientID,reason, notes)
            VALUES(?,?,?,?,?,?)'''
    with closing(conn.cursor()) as c:
        c.execute(sql, (app.date,app.time,app.pet_id,app.client_id,app.reason,app.notes))
        conn.commit()
