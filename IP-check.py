import subprocess
import sys

host_ip = subprocess.run("host pguat.billdesk.io | awk '{print $4}'" , shell=True, capture_output=True, text=True)

host_ip_list = host_ip.stdout.split("\n")

host_ip_list = list(filter(None, host_ip_list))
sorted_host_ip_list = sorted(host_ip_list)

with open('input.txt') as file:
    lines = file.read()

whitelisted_ips = lines.split("\n")
whitelisted_ips = list(filter(None, whitelisted_ips))
sorted_whitelisted_ips = sorted(whitelisted_ips)

if sorted_host_ip_list == sorted_whitelisted_ips :
    print("no change")
else:
    print("ip changed")



