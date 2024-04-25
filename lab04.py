from telnetlib import Telnet

# Gather host connection details and credentials
HOST = input('Specify the Host IP : ')
USER = input('Specify the Username: ')
PASS = input('Specify the Password: ')

# Gather interface configuration details
Interface = input('What Interface would you like to configure : ')
Ipaddr = input('Specify the IP Address : ')
SMask = input('Specify the Subnet mask : ')

# Establish a Telnet connection to the specified host
ab = Telnet(HOST)

# Send login credentials
ab.write(USER.encode('ascii') + b'\n')
ab.write(PASS.encode('ascii') + b'\n')

# Enter configuration mode
ab.write(b'config t\n')

# Construct and send interface configuration commands
int_cmd = 'Interface ' + Interface + '\n'
ipaddr_cmd = 'IP Address ' + Ipaddr + ' ' + SMask + '\n'
ab.write(int_cmd.encode('ascii'))
ab.write(ipaddr_cmd.encode('ascii'))

# Apply the configuration and exit configuration mode
ab.write(b'end\n')

# Verify the configuration
ab.write(b'sh ip int brief\n')

# Terminate the Telnet session
ab.write(b'exit\n')

# Read and print all output from the session
output = ab.read_all().decode('ascii')
print(output)

# Pause to allow user to review the output
input('Press Enter to Continue')
