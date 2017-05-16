FROM python:3

WORKDIR /code
COPY ./requirements.txt /code/
RUN pip install -r requirements.txt
COPY ./ws_api /code/ws_api
RUN pip install -e ./ws_api
COPY ./tests /code/tests

RUN pytest tests/

EXPOSE 5000

CMD ["python", "ws_api/server.py"]