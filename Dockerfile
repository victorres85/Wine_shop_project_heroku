
# syntax=docker/dockerfile:1

FROM python:3
# Set up and activate virtual environment
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY requirements.txt .
#run command bellow has been added on 30/08 at 09:40
# RUN apk add --update --no-cache postgresql-client jpeg-dev && \
#     apk add --update --no-cache --virtual .tmp-build-deps \
#     gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev

RUN pip install -r requirements.txt
#RUN apk del .tmp-build-deps

WORKDIR /usr/src/app

COPY . /usr/src/app

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]