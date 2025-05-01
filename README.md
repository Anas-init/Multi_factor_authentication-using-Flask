# Flask MFA Application

This repository contains a Multi-Factor Authentication (MFA) application built with Flask. Follow the instructions below to set up and run the project locally.

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)
- git (optional, for cloning the repository)

## Setup Instructions

### 1. Clone the Repository (Optional)

```bash
git clone https://github.com/Anas-init/Multi_factor_authentication-using-Flask.git
cd Multi_factor_authentication-using-Flask
```

### 2. Create and Activate Virtual Environment

#### On Windows:

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
.\venv\Scripts\activate

#### On macOS/Linux:
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

### 3. Install Dependencies

Once the virtual environment is activated, install all required packages:
pip install -r requirements.txt

### 4. Set Up Environment Variables

#### On Windows (PowerShell):

Use the following script to load environment variables from your `.env` file:

Get-Content .env | ForEach-Object {
    if ($_ -match "^\s*export\s+([^=]+)=(.*)$") {
        $key = $matches[1].Trim()
        $value = $matches[2].Trim().Trim('"')  # Remove surrounding quotes
        [System.Environment]::SetEnvironmentVariable($key, $value, "Process")
    }
}

#### On macOS/Linux:

source .env

### 5. Initialize the Database

Run the following commands to create and initialize the database:

flask db init
flask db migrate -m "Initial migration"
flask db upgrade

### 6. Run the Application

flask --app src run


The application will be available at `http://127.0.0.1:5000/` by default.

## Project Structure

project/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   └── templates/
├── migrations/
├── .env
├── .gitignore
├── config.py
├── requirements.txt
└── run.py

## Authentication Flow

1. User registers with email and password
2. User enables MFA in account settings
3. User scans QR code with authentication app
4. On subsequent logins, user provides:
   - Username/email and password
   - One-time password from authentication app

## Troubleshooting

### Common Issues

1. **Database errors**: Ensure your database connection string is correct in the `.env` file.
2. **Missing dependencies**: Verify that all packages are installed with `pip list`.
3. **Environment variables not loading**: Check that your `.env` file has the correct format.


## License

[MIT License](LICENSE)