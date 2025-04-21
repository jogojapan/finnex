# finnex: Personal Finance Manager
Experimentation with personal-finances management software.

## Setting Up the Development Environment

### Prerequisites

- Python 3.x
- PostgreSQL

### Steps to Set Up the Environment

1. Clone the Repository:

    ``` bash
    git clone https://github.com/your-username/finnex.git
    cd finnex
    ```
1. Create and Activate a Virtual Environment:

    ``` bash
    python -m venv myenv
    source finnexenv/bin/activate  # On Windows use ```myenv\Scripts\activate```
    ```
1. Install Python Dependencies:

    ``` bash
    bash pip install -r requirements.txt
    ```
1. Create a .env File:

    Create a .env file in the root directory of your project with the
    following content:

    ``` bash
    DB_NAME=your_db_name
    DB_USER=your_db_user
    DB_PASSWORD=your_db_password
    DB_HOST=localhost
    DB_PORT=5432
    ```
1. Run Migrations:

    ``` bash
    python manage.py migrate
    ```
1. Run the Development Server:

    ``` bash
    python manage.py runserver
    ```

### Adding New Dependencies

If you need to add new Python dependencies to the project, follow
these steps:

1. Install the New Package:

    ``` bash
    pip install new-package
    ```
1. Update `requirements.txt`:

    ``` bash
    pip freeze > requirements.txt
    ```
1. Commit the Changes:

    ``` bash
    git add requirements.txt
    git commit -m &quot;Add new-package to requirements.txt&quot;
    git push
    ```
