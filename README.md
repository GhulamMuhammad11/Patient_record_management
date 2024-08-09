# Patient Record Management System

## Project Description

The **Patient Record Management System** is a web application designed for efficient management of patient data. Built using Streamlit and MySQL, this system allows users to input, store, and retrieve patient information, including personal details, medical history, and physical examination data. The system is tailored for use in clinics, ensuring quick and secure access to patient records.

## Features

- **User Authentication**: Secure login for authorized access.
- **Patient Data Management**: Easy input and storage of patient details.
- **Medical Information Storage**: Comprehensive fields for medical history and examination data.
- **Responsive Design**: User-friendly interface with responsive design.

## Installation Instructions

### 1. Clone the Repository

git clone https://github.com/yourusername/patient-record-management.git
cd patient-record-management

### 2. Create and Activate a Virtual Environment

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


### 3. Install Dependencies

pip install -r requirements.txt

### 4. Set Up the MySQL Database
1. Create a MySQL database.
2. Use the `patients.sql` file to create the necessary tables.
3. Create a `.env` file in the root directory and add your MySQL credentials:
    ```
    DB_HOST=your_db_host
    DB_USER=your_db_username
    DB_PASSWORD=your_db_password
    DB_NAME=your_db_name
    ```

### 5. Add Other Configuration
1. Add your Streamlit configuration to the `.env` file:
    ```
    STREAMLIT_PORT=8501  # Optional: Default is 8501
    ```

## Usage Instructions

### 1. Run the Application
```
streamlit run app.py
```

### 2. Access the Application
Open your web browser and go to `http://localhost:8501` (or the port you've specified) to access the application.

### 3. Login
Use the login credentials provided by the administrator to access the application.

## Deployment Instructions

### 1. Prepare the Application for Deployment
- Ensure all dependencies are listed in `requirements.txt`.
- Confirm that the `.env` file is configured correctly for the production environment.
- Set up a production database and update the credentials in the `.env` file.

### 2. Deploy to a Server
- Use a cloud provider like Heroku, AWS, or a virtual private server (VPS).
- Install necessary packages on the server (Python, MySQL).
- Clone the repository on the server.
- Set up the environment (Python virtual environment, dependencies, environment variables).
- Run the application using a process manager like `gunicorn` (if deploying on a VPS) or through the platform’s interface (e.g., Heroku).

### 3. Start the Application
- On a VPS, you can use the following command:
    ```
    gunicorn app:main --bind 0.0.0.0:$PORT
    ```
- For platforms like Heroku, deployment scripts will handle this.

### 4. Access the Deployed Application
- Use the server's IP address or domain name to access the application.