FROM python:3.9-alpine

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app .
ENV PORT=3489
CMD python flask_app.py