FROM python:3.10-slim

WORKDIR /app

COPY . .
RUN pip install requirements.txt

EXPOSE 8501
EXPOSE 9999

CMD["./start.sh"]