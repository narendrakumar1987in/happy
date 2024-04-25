from telnetlib import Telnet

# Gathering host connection details and credentials from the user
HOST = input('Specify the Host IP : ')
USER = input('Specify the Username: ')
PASS = input('Specify the Password: ')

# Asking the user for the number of user accounts to create
num_users = input('How many users would you like to create: ')
num_users = int(num_users)  # Converting the string input to an integer

# Establishing a Telnet connection to the specified host
ab = Telnet(HOST)
ab.write(USER.encode('ascii') + b'\n')  # Sending the login username
ab.write(PASS.encode('ascii') + b'\n')  # Sending the login password
ab.write(b'config t\n')  # Entering configuration mode

# Loop to create the specified number of user accounts
while (num_users > 0):
    username = input('Specify the Username to be created : ')
    userpass = input('Specify the Password: ')
    userpriv = input('Specify the exec level: ')

    # Constructing and sending a command to create each user with given details
    ab.write(b'Username ' + username.encode('ascii') + b' privilege ' + userpriv.encode('ascii') + b' password ' + userpass.encode('ascii') + b'\n')
    num_users -= 1  # Decrementing the counter after each user is created

ab.write(b'end\n')  # Exiting configuration mode
ab.write(b'sh run | inc username\n')  # Command to show running configuration entries that include 'username'
ab.write(b'exit\n')  # Exiting the Telnet session

# Reading and printing all output from the session
output = ab.read_all().decode('ascii')
print(output)

# Pausing to allow the user to review the output
input('Press Enter to Continue')
