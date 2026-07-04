import requests

def test_live_server_healthy():
    # Địa chỉ này sẽ được thay đổi linh hoạt theo IP của Minikube/K8s Cluster
    target_url = "http://localhost:8080/" 
    
    try:
        response = requests.get(target_url, timeout=5)
        # Kiểm tra xem Server có phản hồi mã 200 OK không
        assert response.status_code == 200
        
        # Kiểm tra xem dữ liệu trả về có đúng định dạng JSON chuẩn không
        data = response.json()
        assert data["status"] == "healthy"
        assert data["environment"] == "production"
        print("Integration Test Passed: Live Server đang hoạt động hoàn hảo!")
    except Exception as e:
        print(f"Integration Test Failed: Không thể kết nối tới Server. Lỗi: {e}")
        assert False