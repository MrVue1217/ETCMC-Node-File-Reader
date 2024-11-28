import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import os
from dash.dash_table.Format import Group
from dash import dash_table
import dash_table.Format as Format
from dash.dash_table.Format import Group
from datetime import datetime  # Import datetime for timestamp

shared_paths = [ # share path and folder names. Share path must be accessible on local network
    {'path': r'\\192.168.10.210\ETCMC Client', 'file': 'write_only_etcpow_balance.txt', 'node': 'ETCMC Node 01'},
    {'path': r'\\192.168.10.211\ETCMC Client', 'file': 'write_only_etcpow_balance.txt', 'node': 'ETCMC Node 02'},
    {'path': r'\\192.168.10.212\ETCMC Client', 'file': 'write_only_etcpow_balance.txt', 'node': 'ETCMC Node 03'},
    {'path': r'\\192.168.10.213\ETCMC Client', 'file': 'write_only_etcpow_balance.txt', 'node': 'ETCMC Node 04'},
    {'path': r'\\192.168.10.214\ETCMC Client', 'file': 'write_only_etcpow_balance.txt', 'node': 'ETCMC Node 05'},
    {'path': r'\\192.168.10.215\ETCMC Client', 'file': 'write_only_etcpow_balance.txt', 'node': 'ETCMC Node 06'},
    {'path': r'\\192.168.10.216\ETCMC Client', 'file': 'write_only_etcpow_balance.txt', 'node': 'ETCMC Node 07'},
    {'path': r'\\192.168.10.217\ETCMC Client', 'file': 'write_only_etcpow_balance.txt', 'node': 'ETCMC Node 08'},
    {'path': r'\\192.168.10.218\ETCMC Client', 'file': 'write_only_etcpow_balance.txt', 'node': 'ETCMC Node 09'},
    {'path': r'\\192.168.10.219\ETCMC Client', 'file': 'write_only_etcpow_balance.txt', 'node': 'ETCMC Node 10'}
]

def read_text_file(shared_path, file_name):
    file_path = os.path.join(shared_path, file_name)
    try:
        with open(file_path, 'r') as file:
            contents = file.read()
        return contents
    except FileNotFoundError:
        return "File not found"
    except Exception as e:
        return f"Error reading file: {e}"

app = dash.Dash(__name__)

app.layout = html.Div(
    children=[
        html.Div(
            children=[
                html.H3(
                    children='ETCMC Node Dashboard',
                    style={'color': '', 'display': 'inline-block'}  # Font Color
                ),
                html.Button('Refresh', id='refresh-button', n_clicks=0, style={'display': 'inline-block', 'margin-left': '10px'})
            ]
        ),
        dash_table.DataTable(
            id='table',
            columns=[
                {'name': 'Node', 'id': 'Node'},
                {'name': 'Balance', 'id': 'Contents', 'type': 'numeric', 'format': Format.Format(precision=2)}
            ],
            data=[],
            style_table={'overflowY': 'hidden', 'width': '100%'},
            style_cell={'textAlign': 'left', 'fontSize': 14, 'width': 'auto'} 
        ),
        html.Div(id='last-refresh', style={'margin-top': '20px', 'fontSize': 14}),
        dcc.Interval(
            id='interval-component',
            interval=300000,  # 5 minutes in milliseconds, change as needed
            n_intervals=0
        )
    ]
)

@app.callback(
    [Output('table', 'data'),
     Output('last-refresh', 'children')],
    [Input('interval-component', 'n_intervals'), Input('refresh-button', 'n_clicks')]
)
def update_table(n, n_clicks):
    table_data = []
    for path in shared_paths:
        contents = read_text_file(path['path'], path['file'])
        
        # Check if contents can be converted to float
        try:
            balance = float(contents)
            table_data.append({'Node': path['node'], 'Contents': balance})  # Directly store float
        except ValueError:
            table_data.append({'Node': path['node'], 'Contents': 'N/A'})  # Or handle the error as needed

    # Get the current time for the last time refresh
    last_refresh_time = datetime.now().strftime("%m-%d-%Y %H:%M:%S")
    last_refresh_message = f"Last Refreshed: {last_refresh_time}"

    return table_data, last_refresh_message

if __name__ == '__main__':
    app.run_server(host='192.168.10.201', port=8050) # Server IP and port
