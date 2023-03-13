import os  # Import the OS Library

"""
For some reason the informations about the function below 
will only be show when the user interrupt the running command.
It could be an issue related to Python's version or even my PC.
"""

# Create a variable that receives the ip to be verified
host = input('Type a site link (host) to be verified: ')

# Print at the commend line the statistics about the ping request
os.system('ping -n 6 {}'.format(host))
