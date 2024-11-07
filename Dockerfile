FROM python:alpine
WORKDIR /app
COPY send_email.py .
COPY requirements.txt .
RUN pip install -r requirements.txt
CMD [ "python", "./send_email.py" ]
