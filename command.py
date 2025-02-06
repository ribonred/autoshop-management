from doit.action import CmdAction
from doit.tools import Interactive


def task_server():
    command = "python manage.py runserver"
    return {
        "actions": [CmdAction(command)],
        "verbosity": 2,
    }


def task_tailwind():
    command = "npx tailwindcss -i ./assets/static/src/input.css -o ./assets/static/src/output.css --watch"
    return {
        "actions": [CmdAction(command)],
    }


def task_flushdb():
    command = "python manage.py flush --no-input"
    return {
        "actions": [CmdAction(command)],
        "verbosity": 2,
    }


def task_runwatch():
    return {
        "actions": None,
        "task_dep": ["server", "tailwind"],
    }


def task_migrations():
    command = "python manage.py makemigrations"
    return {
        "actions": [Interactive(command)],
    }


def task_collectstatic():
    command = "python manage.py collectstatic --noinput"
    return {
        "actions": [command],
    }


def task_migrate():
    command = "python manage.py migrate"
    return {
        "actions": [Interactive(command)],
    }


def task_prepare():
    """
    prepare
    """

    return {
        "actions": [Interactive("echo preparation completed...")],
        "task_dep": [
            "migrations",
            "migrate",
            "collectstatic",
        ],
    }
