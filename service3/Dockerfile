#Use Python Image
FROM python:3.6.8

# Install apt dependencies
RUN apt update
RUN apt install python3 -y
RUN apt install python3-pip -y

WORKDIR /opt/service3

# Copy contents into image

COPY . ${WORKDIR}

# run pip dependencies
RUN pip3 install -r requirements.txt

# Expose correct port
EXPOSE 5002

# Create an entrypoint
ENTRYPOINT ["/usr/local/bin/python3", "app.py"]

