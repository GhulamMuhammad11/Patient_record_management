import streamlit as st
from user_authentication import is_authenticated
from db_operation import save_to_database
from datetime import datetime

# Set the page layout to wide and set the background color to white
st.set_page_config(layout="wide")

# Function to show the main content of the app
def show_app_content():
    # Title of the app with logo
    logo_path = "logo.png"  # Path to the uploaded logo image

    # Create a container for the logo and title
    col1, col2 = st.columns([1, 9])
    with col1:
        st.image(logo_path, width=100)
    with col2:
        st.markdown("<h1>Manzoor Medical Hall And Children's Clinic</h1>", unsafe_allow_html=True)

    # Personal Information section
    st.header("Personal Information")

    # Creating a container for the personal information
    today = datetime.today()
    ten_years_ago = today.replace(year=today.year - 150)
    ten_years_from_now = today.replace(year=today.year + 50)

    # Creating a container for the personal information
    with st.container():
        col1, col2, col3 = st.columns(3)
        dated = col1.date_input("Dated", min_value=ten_years_ago, max_value=ten_years_from_now)
        mr_no = col2.text_input("MR No")
        name = col3.text_input("Name")
        father_name = col1.text_input("Father Name")
        dob = col2.date_input("Date of Birth", min_value=ten_years_ago, max_value=ten_years_from_now)
        occupation = col3.text_input("Occupation")
        contact_no = col1.text_input("Contact No")
        age = col2.number_input("Age", min_value=0)
        marital_status = col3.text_input("Marital Status")
        cnic_no = col1.text_input("CNIC No")
        sex = col2.radio("Sex", ('Male', 'Female', 'Other'))
        category = col3.radio("Category", ['Deserving', 'Non-Deserving'])
        address = st.text_area("Address")

    # Medical Information section
    st.header("Medical Information")

    # Creating a container for the medical information
    with st.container():
        chief_complaints = st.text_area("Chief Complaints")
        hopi = st.text_area("HOPI")
        past_hx = st.text_area("Past HX")
        birth_hx = st.text_area("Birth HX")
        immunization = st.text_area("Immunization")
        developmental_hx = st.text_area("Developmental HX")
        family_hx = st.text_area("Family HX")
        allergies = st.text_area("Allergies")
        drug_hx = st.text_area("Drug HX")
        social_hx = st.text_area("Social HX")
        antenatal_gynal_obs = st.text_area("ANTENATAL/GYNAL/OBS")

    # Physical Examination section
    st.header("Physical Examination")

    # General Physical Examination and Vital Signs
    col1, col2 = st.columns(2)

    with col1:
        st.write("GPE(General Physical Examination)")
        jaundice = st.checkbox("Jaundice")
        pallor = st.checkbox("Pallor")
        koilonychia = st.checkbox("Koilonychia")
        lymph_nodes = st.checkbox("Lymph Nodes")

    with col2:
        st.write("Vital Signs")
        rr = st.checkbox("RR (Respiratory Rate)")
        hr = st.checkbox("HR (Heart Rate)")
        bp = st.checkbox("BP (Blood Pressure)")
        temp = st.checkbox("Temp (Temperature)")

    with col1:
        st.write("Respiratory System")
        git = st.checkbox("GIT (Gastrointestinal Tract)")
        cns = st.checkbox("CNS (Central Nervous System)")
        cvs = st.checkbox("CVS (Cardiovascular System)")
        ent = st.checkbox("ENT (Ear Nose Throat)")
        thyroid = st.checkbox("Thyroid")

    # Provisional Diagnosis
    st.subheader("Provisional Dx (Provisional Diagnosis)")
    provisional_dx = st.text_area("Provisional Dx")

    # Investigations and Treatment
    investigations = st.text_area("Investigations")

    treatment = st.text_area("Treatment")

    # Follow up and Final Diagnosis
    follow_up = st.text_area("Follow up")

    final_diagnosis = st.text_area("Final Diagnosis")

    # Final Investigations
    final_investigations = st.text_area("Final Investigations")

    # Add the Submit button
    if st.button("Submit"):
        # Combine all fields into one tuple
        patient_data = (
            dated, mr_no, name, father_name, dob, occupation, contact_no, age,
            marital_status, cnic_no, sex, category, address,
            chief_complaints, hopi, past_hx, birth_hx, immunization, developmental_hx,
            family_hx, allergies, drug_hx, social_hx, antenatal_gynal_obs,
            jaundice, pallor, koilonychia, lymph_nodes, rr, hr, bp, temp,
            git, cns, cvs, ent, thyroid, provisional_dx, investigations, treatment,
            follow_up, final_diagnosis, final_investigations
        )

        # Call the function to save data to the database
        save_to_database(patient_data)
        st.success("Data successfully submitted!")

# Function to handle login
def handle_login(username, password):
    if is_authenticated(username, password):
        st.session_state.authenticated = True
        st.session_state.login_success = True
    else:
        st.session_state.login_success = False

# Main function
def main():
    # Initialize session state
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
    if "login_success" not in st.session_state:
        st.session_state.login_success = None

    if not st.session_state.authenticated:
        st.title("Login Page")

        # Login form
        login_username = st.text_input("Username")
        login_password = st.text_input("Password", type="password")
        login_button = st.button("Login", on_click=lambda: handle_login(login_username, login_password))

        if st.session_state.login_success == False:
            st.error("Invalid username or password")
    else:
        show_app_content()

if __name__ == "__main__":
    main()
