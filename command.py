from doit.action import CmdAction
from django.core.management import call_command


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
