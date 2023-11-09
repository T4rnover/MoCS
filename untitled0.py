# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 13:37:48 2023

@author: Tarnover
"""

import subprocess

# Define the IP address range to scan
ip_range = '192.168.1.'
start_ip = 1
end_ip = 255

# Loop over each IP address in the range
for i in range(start_ip, end_ip+1):
    ip_address = ip_range + str(i)

    # Ping the IP address to check if it's active
    ping_output = subprocess.run(['ping', '-c', '1', '-W', '1', ip_address], capture_output=True)

    # Check the output for a successful ping response
    if b"1 received" in ping_output.stdout:
        print(f"Active IP address found at {ip_address}")