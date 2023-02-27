import os  # Import the OS Library
from time import sleep  # Importing the function sleep to print ping information in a space of time determinate by the dev

"""
For some reason the information about the function below
will only be show when the user interrupt the running command.
It could be an issue related to Python's version or even my PC.
"""

# Variable created to receive everything that's inside the 'hostslist' file
list = open('hostslist', 'r')

# For loop created to iterate with each one of the IPs
for x in list:
    # Print at the commend line the statistics about the ping request
    os.system(f"ping -p 2 {x}")
    # Wait 3 seconds to show the PING information about the next IP inside the file
    sleep(3)
