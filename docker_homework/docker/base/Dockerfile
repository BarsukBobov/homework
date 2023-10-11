FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV TZ=Etc/UTC

WORKDIR /code
COPY . /code

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
    && echo $TZ > /etc/timezone \
    && apt update \
    && apt install -y --assume-yes python3-dev build-essential libpq-dev python3-pip\
    && python3 -m pip install -r requirements/base.txt

CMD python3 main.py