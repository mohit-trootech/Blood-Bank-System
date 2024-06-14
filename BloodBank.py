from Inventory import Inventory
from database import *


class BloodBank:

    @staticmethod
    def donor_details(donor_name, donor_age, donor_blood_type):
        query = f"""
        INSERT INTO donor ( donor_name, donor_age, donor_blood_type )
        VALUES ( "{donor_name}", {donor_age}, "{donor_blood_type}" )
"""
        db_query(query, False)
        mydb.commit()
        print(f"{donor_name} is Registered Successfully with blood bank - {donor_blood_type}, {donor_age}")

    @staticmethod
    def request_blood(hospital_name,
                      patient_name, patient_age, patient_blood_type,
                      donor_name, donor_age, donor_blood_type):
        query = f"""INSERT INTO request 
        (hospital_name,patient_name,patient_age,patient_blood_type,
                      donor_name, donor_age, donor_blood_type)
        VALUES ( "{hospital_name}",
        "{patient_name}",{patient_age},"{patient_blood_type}",
                      "{donor_name}", {donor_age}, "{donor_blood_type}" );"""
        db_query(query, False)
        BloodBank.donor_details(donor_name, donor_age, donor_blood_type)
        Inventory.add_blood(donor_blood_type)
        Inventory.deduct_blood(patient_blood_type)
        mydb.commit()
        print("Thanks for using Blood Bank")
