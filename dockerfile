from python:latest

# disable the console
env PYTHONBUFFERED 1

workdir /app

copy requirements.txt .
run pip install -r requirements.txt
copy . .
cmd ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
