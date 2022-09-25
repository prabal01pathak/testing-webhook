FROM python:3.10
WORKDIR /code
RUN pip3 install poetry
RUN  poetry config virtualenvs.create false
COPY ./poetry.lock /code
COPY ./pyproject.toml /code
RUN poetry install
COPY ./ /code
EXPOSE 8080
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]
