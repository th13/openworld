FROM python:3

WORKDIR /code
COPY ./requirements.txt /code/
RUN pip install -r requirements.txt
COPY ./api /code/api
RUN pip install -e ./api
COPY ./tests /code/tests

RUN pytest tests/

EXPOSE 5000

CMD ["python", "api/run.py"]