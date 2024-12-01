
FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    gcc && apt-get clean

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

RUN python manage.py collectstatic --noinput

RUN chmod -R 755 /app/staticfiles

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "my_project.wsgi:application"]
