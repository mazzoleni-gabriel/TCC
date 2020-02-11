FROM python:3
ENV PYTHONUNBUFFERED 0
RUN mkdir -p /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY ./docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh
#ENTRYPOINT /docker-entrypoint.sh
COPY . /code/