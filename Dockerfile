#Storing the program into a container so it runs 24/7 as long as local machine is on
FROM python:3.10.6-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]
