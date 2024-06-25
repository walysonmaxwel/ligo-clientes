FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    gcc \
    netcat-openbsd \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*


COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . /app
# COPY migrations/ /app/migrations
# COPY entrypoint.sh /app/entrypoint.sh
# RUN chmod +x /app/entrypoint.sh
RUN chmod +x entrypoint.sh


EXPOSE 5000
# CMD ["sh", "-c", "flask db migrate && flask db upgrade && flask run --host=0.0.0.0"]

ENTRYPOINT ["/app/entrypoint.sh"]