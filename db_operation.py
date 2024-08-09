import mysql.connector
import os
from dotenv import load_dotenv
load_dotenv()

# Now the environment variables will be loaded from the .env file


def save_to_database(patient_data):
    # Database connection
    conn = mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME')
    )
    cursor = conn.cursor()

    try:
        # Insert patient and medical data
        cursor.execute(
            """
            INSERT INTO patients (
                dated, mr_no, name, father_name, dob, occupation, contact_no, 
                age, marital_status, cnic_no, sex, category, address,
                chief_complaints, hopi, past_hx, birth_hx, immunization, developmental_hx,
                family_hx, allergies, drug_hx, social_hx, antenatal_gynal_obs,
                jaundice, pallor, koilonychia, lymph_nodes, rr, hr, bp, temp,
                git, cns, cvs, ent, thyroid, provisional_dx, investigations, treatment,
                follow_up, final_diagnosis, final_investigations
            ) VALUES (
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                %s, %s, %s, %s
            )
            """,
            patient_data
        )

        # Commit the transaction
        conn.commit()

        print("Data inserted successfully.")

    except mysql.connector.Error as e:
        print(f"Error: {e}")
        conn.rollback()

    finally:
        cursor.close()
        conn.close()
