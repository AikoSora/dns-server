FROM python:3.11

RUN mkdir /app

WORKDIR /app

COPY Pipfile Pipfile.lock .

RUN pip install pipenv

RUN pipenv install --dev --system --deploy

COPY app .

RUN python manage.py collectstatic --noinput

CMD gunicorn src.wsgi:application --bind 0.0.0.0:8000
