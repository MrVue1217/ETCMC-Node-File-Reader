from flask import Flask, request, jsonify, render_template_string
import psutil
import os

app = Flask(__name__)

# Store device information
devices = {}

@app.route('/add_device', methods=['POST'])
def add_device():
    data = request.json
    device_id = data.get('device_id')
    devices[device_id] = data
    return jsonify({"message": "Device added successfully!"}), 200

@app.route('/devices', methods=['GET'])
def get_devices():
    return jsonify(devices), 200

@app.route('/devices_table', methods=['GET'])
def devices_table():
    # HTML template for displaying devices in a table
    html = """
    <!doctype html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <title>Device Information</title>
        <style>
            table {
                width: 100%;
                border-collapse: collapse;
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <h1>Device Information</h1>
        <table>
            <tr>
                <th>Device ID</th>
                <th>Memory Used (%)</th>
                <th>CPU Usage (%)</th>
                <th>Disk Used (%)</th>
                <th>Balance</th>
                
            </tr>
            {% for device_id, info in devices.items() %}
            <tr>
                <td>{{ device_id }}</td>
                <td>{{ info.memory.percent }}%</td>
                <td>{{ info.cpu }}</td>
                <td>{{ info.disk.percent }}%</td>
                <td>{{ info.balance }}</td>
                <td>{{ info.file_content }}</td>
            </tr>
            {% endfor %}
        </table>
    </body>
    </html>
    """
    return render_template_string(html, devices=devices)

if __name__ == '__main__':
    app.run(host='10.10.15.62', port=8055)