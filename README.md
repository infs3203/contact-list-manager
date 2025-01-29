
---

# Contact List Manager

A Flask-based web application for managing contacts. This application intentionally has some bugs for educational purposes in software testing. Various bugs have been identified and fixed using Git workflow, and new features have been added for improved functionality.

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Git

## Installation Instructions

### Clone the Repository
```bash
git clone <repository-url>
cd contact-list-manager
```

### Setting Up Virtual Environment

#### For macOS/Linux:
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate
```

#### For Windows:
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate
```

### Install Dependencies

With the virtual environment activated, install the required packages:
```bash
pip install -r requirements.txt
```

## Running the Application

### First Time Setup
When running the application for the first time, the database will be automatically created.

### Starting the Server

#### For macOS/Linux:
```bash
# Make sure your virtual environment is activated
source venv/bin/activate

# Run the application
python3 app.py
```

#### For Windows:
```bash
# Make sure your virtual environment is activated
venv\Scripts\activate

# Run the application
python app.py
```

The application will be available at `http://localhost:5001`

## Application Features

- Create new contacts
- View list of contacts
- Update existing contacts
- Delete contacts
- Search contacts
- Add profile pictures to contacts
- New fields for contacts: Birthdate and Address
- Dark mode toggle
- Prevent empty contact submissions
- Prevent duplicate contacts
- Redesigned homepage layout

## API Endpoints

- GET `/api/contacts` - List all contacts
- GET `/api/contacts/<id>` - Get a specific contact
- POST `/api/contacts` - Create a new contact
- PUT `/api/contacts/<id>` - Update a contact
- DELETE `/api/contacts/<id>` - Delete a contact

## Project Structure
```
contact-list-manager/
├── app.py               # Main Flask application
├── models.py           # Database models
├── forms.py            # Form definitions
├── requirements.txt    # Project dependencies
├── templates/          # HTML templates
│   ├── base.html
│   ├── index.html
│   ├── contacts.html
│   ├── add_contact.html
│   └── update_contact.html
└── static/
    └── js/
        └── search.js
```

## Recent Updates and Bug Fixes

### 1. **Delete Button Bug Fixed**
The delete button was previously unresponsive. The bug was fixed by properly linking the delete functionality, so the delete button now works as expected.

### 2. **Search Bar Bug Was Not Working**
The search bar was not returning any results. The search filter logic was fixed to allow searches by contact name and return relevant results.

### 3. **Dark Mode Feature Added**
A dark mode toggle has been introduced to allow users to switch between light and dark themes for improved usability and visual appeal.

### 4. **Contacts Can Now Add Profile Pictures**
Users can now upload a profile picture when creating or editing a contact. The picture will display next to the contact's name and other details.

### 5. **Empty Contact Submission Bug Fixed**
The application now ensures that users fill all required fields (name, phone number, etc.) before submitting a contact form. Empty submissions are no longer allowed.

### 6. **New Fields for Personal Info: Birthdate and Address**
New fields for birthdate and address have been added to the contact creation and editing forms, allowing users to store additional personal information.

### 7. **Prevent Duplicated Contacts**
A check has been added to prevent users from adding duplicate contacts with the same name and phone number. If a duplicate is detected, the user is alerted and prevented from submitting the form.

### 8. **Homepage New Design**
The homepage layout has been redesigned to improve navigation and user experience. The new design features cleaner visuals and more intuitive functionality.

## Git Workflow

Each bug fix or feature has been implemented in its own Git branch and pull request using Git workflow. Here's a brief overview of the steps taken:

1. **Fork the Repository:** A personal copy of the repository was created on GitHub.
2. **Identify Bugs and Features:** Bugs were manually tested and documented in GitHub issues.
3. **Create Branches:** Each bug/feature was fixed or added in its own branch (`bugfix/<bug-description>` or `feature/<feature-description>`).
4. **Commit and Push:** Changes were committed and pushed to GitHub.
5. **Pull Requests:** Each branch was merged into the main branch after review.
6. **Merge and Clean Up:** After merging, the branches were deleted locally to keep the repository clean.

## Troubleshooting

### Port Already in Use
If you get an error about port 5001 being in use:
1. Change the port number in `app.py`
2. Or kill the process using the port:
   ```bash
   # For macOS/Linux
   lsof -i :5001
   kill -9 <PID>
   
   # For Windows
   netstat -ano | findstr :5001
   taskkill /PID <PID> /F
   ```

### Virtual Environment Issues
If you have problems with the virtual environment:
1. Delete the `venv` directory
2. Re-create it following the installation steps above

### Database Issues
If you encounter database problems:
1. Delete the `contacts.db` file
2. Restart the application to create a fresh database

## Deactivating Virtual Environment

When you're done working on the project:
```bash
deactivate
```

## Note for Testing

This application contains intentionally introduced bugs for educational purposes in software testing. These bugs have been documented and fixed through Git workflow and feature improvements have been added.

---
