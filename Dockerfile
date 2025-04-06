FROM python:3.12-slim

RUN pip install pipenv

WORKDIR /app
COPY ./Pipfile ./Pipfile.lock /app/

RUN pipenv install --system --dev
RUN pip install psycopg2-binary

COPY . /app/

EXPOSE 5000

CMD ["pipenv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000"]
