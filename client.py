import psutil
import requests
import time
import os

SERVER_URL = 'http://localhost:8055/add_device'
DEVICE_ID = 'Node01'  # Unique identifier for the device

def get_system_info():
    memory = psutil.virtual_memory()._asdict()
    cpu = psutil.cpu_percent(interval=1)
    disk = psutil.disk_usage('/')._asdict()
    
    # Read the balance from the specified file
    file_path = r'C:\Program Files (x86)\ETCMC\ETCMC Client\write_only_etcpow_balance.txt'
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            # Assuming the file contains a single line with the balance
            try:
                balance = float(file.readline().strip())  # Read and convert to float
            except ValueError:
                balance = 0.00  # Default value if conversion fails
    else:
        balance = 0.00  # Default value if file does not exist

    return {
        'device_id': DEVICE_ID,
        'memory': {
            'total': memory['total'],
            'available': memory['available'],
            'used': memory['used'],
            'percent': memory['percent']
        },
        'cpu': cpu,
        'disk': {
            'total': disk['total'],
            'used': disk['used'],
            'free': disk['free'],
            'percent': disk['percent']
        },
        'balance': round(balance, 2),  # Round to 2 decimal places
        'file_content': "Balance read from file"
    }

while True:
    system_info = get_system_info()
    response = requests.post(SERVER_URL, json=system_info)
    print(response.json())
    time.sleep(300)  # Wait for 5 minutes