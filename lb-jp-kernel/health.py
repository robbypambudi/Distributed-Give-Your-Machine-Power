import requests

def check_worker_status(worker_name, port):
    url = f"http://localhost:{port}"
    try:
        # Try to make a request to the worker
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"{worker_name} is active on port {port}.")
        else:
            print(f"{worker_name} is not responding properly. Status code: {response.status_code}")
    except requests.ConnectionError:
        print(f"{worker_name} is not reachable on port {port}.")
    except requests.Timeout:
        print(f"{worker_name} timed out on port {port}.")

if __name__ == "__main__":
    workers = [
        ("Jupyter Worker 1", 8888),
        ("Jupyter Worker 2", 8889),
        ("Jupyter Worker 3", 8890),
        ("Jupyter Worker 4", 8891)
    ]
    
    for worker_name, port in workers:
        check_worker_status(worker_name, port)
