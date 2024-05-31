# Django File Upload Project

This project is a Django-based web application that allows users to upload an Excel/CSV file, processes the file to generate a summary report, and sends the summary via email. The application is deployed on Heroku for testing. and check the  all things

## Features

- Upload Excel/CSV files
- Process the file to generate a summary report
- Email the summary report
- Deployed on Heroku

## Getting Started

These instructions will help you set up the project on your local machine for development and testing purposes.

### Prerequisites

- Python 3.8+
- Django 5.0+
- Pandas
- Openpyxl
- Gunicorn
- Heroku CLI (if deploying to Heroku)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/django-file-upload.git
    cd django-file-upload
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Run database migrations:

    ```bash
    python manage.py migrate
    ```

5. Create a superuser to access the admin interface:

    ```bash
    python manage.py createsuperuser
    ```

6. Start the development server:

    ```bash
    python manage.py runserver
    ```

    Visit `http://127.0.0.1:8000/fileupload/upload/` to upload files.

### Project Structure

- `myproject/` - Main project directory
- `fileupload/` - Django app for file upload
- `templates/fileupload/` - HTML templates for the app
- `static/` - Static files (if any)
- `requirements.txt` - List of dependencies
- `Procfile` - Heroku configuration file

### Deployment

To deploy this application to Heroku, follow these steps:

1. Login to Heroku:

    ```bash
    heroku login
    ```

2. Create a new Heroku application:

    ```bash
    heroku create
    ```

3. Push the code to Heroku:

    ```bash
    git push heroku master
    ```

4. Run database migrations on Heroku:

    ```bash
    heroku run python manage.py migrate
    ```

5. Access your deployed application at the URL provided by Heroku.

### Usage

1. Navigate to the upload page.
2. Choose an Excel/CSV file to upload.
3. Submit the form.
4. The server processes the file and sends a summary report via email.

### Example Data

The dataset should have the following columns:

- `State`
- `DPD`

Example:

| State | DPD |
|-------|-----|
| Assam | 32  |
| Assam | 25  |
| UP    | 61  |

### Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Acknowledgments

- Thanks to the Django and Pandas communities for their excellent documentation and support.

