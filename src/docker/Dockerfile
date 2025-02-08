FROM python:3.12-slim

WORKDIR /app
COPY ./src/poetry.lock ./src/pyproject.toml ./

RUN python -m pip install --no-cache-dir poetry==1.8.5
RUN poetry config virtualenvs.create false && poetry install --no-dev

COPY ./src/ ./

EXPOSE 7777

CMD ["python3", "-u", "main.py"]
