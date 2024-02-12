## Cassoni Backend :rocket:

env variables:

    :information: [Variables marked with * are mandatory and must be present in the .env file]

    # ___Project Setup___ #
    SECRET_KEY = string *
    DEBUG = bollean[default=True]

    # ___Database___ #
    USE_MYSQL = boolean[default=False]
    MYSQL_NAME = string(if USE_MYSQL is true, need to set this variable.)
    MYSQL_USER = string(if USE_MYSQL is true, need to set this variable.)
    MYSQL_PASS = string(if USE_MYSQL is true, need to set this variable.)
    MYSQL_HOST = url(if USE_MYSQL is true, need to set this variable.)
    MYSQL_PORT = int(if USE_MYSQL is true, need to set this variable.)
    DEPENDENT_EMAIL_ON_DEBUG = bool[default=True](in debug mode all email messages managing on console, if you want receiving email messages in debug mode setting this variable to False)

    USE_POSTGRES = boolean[default=False]
    POSTGRES_NAME = string(if USE_POSTGRES is true, need to set this variable.)
    POSTGRES_USER = string(if USE_POSTGRES is true, need to set this variable.)
    POSTGRES_PASS = string(if USE_POSTGRES is true, need to set this variable.)
    POSTGRES_HOST= url(if USE_POSTGRES is true, need to set this variable.)
    POSTGRES_PORT = int(if USE_POSTGRES is true, need to set this variable.)

    DEFAULT_DATABASE_NAME = str[set mysql or postgresql]

    # __Csrf and Allowed Host__ #
    ALLOWED_HOSTS = list, serpate with ","[default=*]
    CORS_ORIGIN_REGEX_WHITELIST = list, serpate with ","[default=*]
    CSRF_TRUSTED_ORIGINS list, serpate with ","[default=http://localhost:8000]

docker env variables:

    # db - postgresql #
        POSTGRES_USER = string *
        POSTGRES_PASSWORD = string *
        POSTGRES_DB = string

:question:

    For install pre-commit configuration on your git:
        pre-commit install


How To Run Docker :question:

    docker-compose up -d

How To Run Locally :question:

    pip install -r requirements.txt
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver or gunicorn src.config.wsgi:application --bind 0.0.0.0:8000

For Run Test Project Service :sparkles:

    python manage.py test --pattern="tests_*.py"
