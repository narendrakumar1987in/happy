from telnetlib import Telnet

# Prompting user for input
myinterface = input('What Interface would you like to configure [E0/0, Loopback200, etc]: ')
Ipaddr = input('Specify the IP Address: ')
SMask = input('Specify the Subnet Mask: ')

# Establishing Telnet connection
ab = Telnet('192.168.18.74')

# Sending login credentials
ab.write(b'khawar\n')
ab.write(b'cisco\n')

# Entering configuration mode
ab.write(b'config t\n')

# Constructing and sending interface configuration commands
int_cmd = 'Interface ' + myinterface + '\n'
ipaddr_cmd = 'ip address ' + Ipaddr + ' ' + SMask + '\n'
ab.write(int_cmd.encode('ascii'))
ab.write(ipaddr_cmd.encode('ascii'))

# Enabling the interface and ending configuration mode
ab.write(b'no shut\n')
ab.write(b'end\n')

# Checking the configuration
ab.write(b'sh ip int brief\n')

# Exiting the session
ab.write(b'exit\n')

# Reading and decoding all output from the session
output = ab.read_all().decode('ascii')
print(output)

# Pausing so the user can see the output
input('Press ENTER to Continue')
