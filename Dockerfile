FROM python:3.9-slim-buster
COPY . .
WORKDIR .
RUN python3 -m pip install --default-timeout=100 -r requirements.txt
EXPOSE 8000
