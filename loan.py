import os
currentip ="65.1.137.201"
cmd ="host pguat.billdesk.io"
returned_value = os.system(cmd)
newip = "192.168.1.1"
if newip == currentip: 
    print("No change in IP's")
else:
   print("IP changed")

