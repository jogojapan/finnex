# finnex: Personal Finance Manager
Experimentation with personal-finances management software.

## Architecture (future; still working on it)

``` mermaid
%% Django-React-Nginx Architecture (Validated)
graph TD
    %% Entities
    User[("User/Browser")] -->|"HTTPS: domain.com"| Nginx
    User -->|"HTTPS: api.domain.com"| Nginx

    subgraph "Webserver"
        direction TB
        Nginx["nginx"] -->|"Serves static files"| React
        Nginx -->|"Proxies to Gunicorn"| Django
    end

    subgraph "Frontend"
        React["React App (Static Files)"]
    end

    subgraph "Backend"
        Django["Django (Gunicorn)"] --> Database[("Database")]
    end

    %% Styling (no inline comments!)
    class User user
    class Nginx nginx
    class React react
    class Django django
    class Database database
    classDef user fill:#f0f0f0,stroke:#20232a,stroke-width:2px,color:#333
    classDef nginx fill:#f0f8ff,stroke:#20232a,stroke-width:2px,color:#333,rx:8,ry:8
    classDef react fill:#619a9b,stroke:#20232a,stroke-width:2px,color:#ccc,rx:8,ry:8
    classDef django fill:#619a9b,stroke:#20232a,color:#ccc,rx:8,ry:8
    classDef database fill:#336791,stroke:#20232a,color:#ccc,rx:8,ry:8
```

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
    python -m venv finnexenv
    source finnexenv/bin/activate  # On Windows use ```myenv\Scripts\activate```
    ```
    
    (You may later leave this environment by entering `deactivate`.)
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
