FROM python:3

WORKDIR /code
COPY ./requirements.txt /code
RUN pip install -r requirements.txt
COPY src/ /code/src

EXPOSE 5000

CMD ['python', '/code/src/api.py']