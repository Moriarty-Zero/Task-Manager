# Task Manager

Task Manager is a web application for task management developed using Python and Django. The application allows users to create, edit, and delete tasks, as well as track their progress.

---

## Description

This application enables you to:
- Register and log in as a user.
- Manage a personal task list.
- Use a simple and intuitive interface built with Bootstrap.

---

## Requirements

To run the project, you will need:
- **Python 3.9** or later.
- **Django 4.2**.
- **PostgreSQL** or **SQLite** (default).

All dependencies are listed in the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Create an admin user:
   ```bash
   python manage.py createsuperuser
   ```

6. Start the development server:
   ```bash
   python manage.py runserver
   ```

Open http://127.0.0.1:8000/ in your browser.

---

## Usage

1. Register or log in to the system.
2. Use the interface to create, edit, and delete tasks.
3. Access the admin panel at `/admin` to manage all data (for admin users).

---

## Technologies

The project was built with:
- Python 3.9
- Django 4.2
- PostgreSQL
- Bootstrap 5 for UI styling

---

## Contribution

Contributions to the project are welcome!

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-your-feature`.
3. Make your changes and commit them: `git commit -m "Description of changes"`.
4. Submit a pull request.

---

## Author

**Oleksiy Klymchuk**  
[GitHub Profile](https://github.com/MoriartyZero)  
[Email](oleksiyklumchuk@gmail.com)

---

## License

This project is licensed under the [MIT License](LICENSE).
