# QueueSine

Simple restaurant reservation app written in Django + Bootstrap + HTMX.

This project is intended to be used as a part of my senior project, replacing [restaurant-pos](https://github.com/Jangsoodlor/restaurant-pos) due to changes to the senior project's scope and requirements.

## Installation

1. Clone or download this repository

1. [Optional] Create a virtual environment for this project and activate it ([how?](https://docs.python.org/3/library/venv.html))

1. Install required packages
    ```bash
    pip install -r requirements.txt
    ```

1. Make database migrations and migrate your database.
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
1. Download [compiled Bootstrap bundle](https://www.kaggle.com/datasets/graphquest/restaurant-menu-items) and extract it to `./static` directory

1. [Optional] Seed initial data
    ```bash
    python manage.py seed --limit=50
    ```

1. Run Django
    ```bash
    python manage.py runserver
    ```

1. Visit `localhost:8000/restaurants` and enjoy!
