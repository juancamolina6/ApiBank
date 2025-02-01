FROM python:3.9-slim

WORKDIR /app

# 1. Copiar SOLO el .env primero para cachear
COPY .env .              

# 2. Instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 3. Copiar el resto del código
COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]