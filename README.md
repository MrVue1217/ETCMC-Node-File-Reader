ETCMC File reader using Python

![image](https://github.com/user-attachments/assets/d42d574b-319b-407f-a56c-6429cdf46f02)



Required
Windows 10 or higher
Python 3

Add-Ons
Dash
Pandas

Installation

1. Install Python 3
2. Install Dash using Windows Powershell (pip install dash)
3. Install Pandas (pip install pandas)

Once Python and Add-on are install, prepare the sharing folders to be monitor.

Under ETCMC installation folder path (C:\Program Files\ETCMC\ETCMC Client)

Share the ETCMC Folder within your local network sharing (ETCMC Client)
![image](https://github.com/user-attachments/assets/e896b4f9-38e2-40a4-8322-cab2f8820514)

Do this for all ETCMC Nodes you have

 Once all folders are shared on the local network, prepare your python script.

 Edit the path here:
 {'path': r'\\10.10.15.210\ETCMC Client', 'file': 'write_only_etcpow_balance.txt', 'node': 'ETCMC Node 01'},

This is the file that will be read by the python script
(Don not change or update this file.)
'write_only_etcpow_balance.txt'

Once all shared folder has been added. You can customize the dashboard looks, color, column names, etc.

1. Open up a powershell window and navigate to the dirctory of the python script (app.py)
   example:
     cd desktop\dashboard\
   ![image](https://github.com/user-attachments/assets/e62f1cc0-f763-4bc4-aa59-246c698dbc78)


   enter: python app.py

   You pythion script should execute and should be accessible on the IP address
   ![image](https://github.com/user-attachments/assets/d02b9051-5607-48b7-8689-6e67954a31e6)

   
