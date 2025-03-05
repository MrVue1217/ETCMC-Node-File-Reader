ETCMC File reader using Python

![image](https://github.com/user-attachments/assets/57964875-60f3-4d30-8691-a439a25f47a1)

Required
Windows 10 or higher
Python 3

Add-Ons
Flask
psutil

2 files (server.py and client.py)

- Server.py can be added to a main PC\NAS that can host
- Client.py will be added to the Node PC
- Client.py will post to server of updates every 5 minutes. This can be change. 
  - (time.sleep(300)  # Wait for 5 minutes)

Installation

1. Install Python 3
2. Install Flask using Windows Powershell (pip install Flask)
3. Install psutil (pip install psutil)

Once Python and Add-on are install, prepare the client.py file to be monitor.

ETCMC installation
Edit the below items in the client.py file

 - (file_path = r'C:\Program Files (x86)\ETCMC\ETCMC Client\write_only_etcpow_balance.txt') # ETCMC File path (default path)
 - SERVER_URL = 'http://localhost:8055/add_device' # your host PC
 - DEVICE_ID = 'Node01'  # Unique identifier for each device

This is the file that will be read by the python script
(Do not change or update this file.)
'write_only_etcpow_balance.txt'

Once all shared folder has been added. You can customize the dashboard looks, color, column names, etc.

1. Open up a powershell window and navigate to the dirctory of the python script (app.py)
   example:
     - cd desktop\dashboard\ #path to your server.py file
     - enter: python server.py

   You pythion script should execute and should be accessible on the IP address (http://localhost:8055/add_device)
 ![image](https://github.com/user-attachments/assets/218efd90-5ae3-4914-b9e7-42cf47051c8a)


   
