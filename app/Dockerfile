FROM python:3.9-slim

WORKDIR /app

# Copy requirements và cài đặt
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy toàn bộ mã nguồn
COPY . .

# Expose port ứng dụng chạy
EXPOSE 5000

# Chạy ứng dụng
CMD ["python", "app.py"]