FROM python:3.12-slim

WORKDIR /amocrm_integrations

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "application.main:app", "--host", "0.0.0.0", "--port", "8080"]