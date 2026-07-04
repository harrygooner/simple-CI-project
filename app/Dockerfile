# Sử dụng base image nhẹ để tối ưu build time (một tiêu chí trong Task 4)
FROM python:3.9-slim

# Thiết lập thư mục làm việc
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