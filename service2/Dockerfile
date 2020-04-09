FROM python:3.6

# Install apt dependencies
RUN apt update
RUN apt install python3 -y
RUN apt install python3-pip -y

WORKDIR /app
COPY requirements.txt .
RUN pip3 install -r requirements.txt
ENTRYPOINT ["/usr/local/bin/python3", "app.py"]
COPY . .
