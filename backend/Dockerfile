# Python 3.11 ka lightweight official image
FROM python:3.11-slim

# Container ke andar apna working folder set kar rahe hain
WORKDIR /app

# Requirements file copy karke libraries install karna
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Ab backend ka saara code container mein copy kar do
COPY . .

# FastAPI server chalane ki aakhri command (0.0.0.0 zaroori hai external access ke liye)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]