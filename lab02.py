from telnetlib import Telnet

# Establish connection
mytel = Telnet('192.168.18.74')

# Login credentials and initial configuration
mytel.write(b'khawar\n')
mytel.write(b'cisco\n')
mytel.write(b'terminal length 0\n')
mytel.write(b'enable\n')

# Display current interface configuration
mytel.write(b'show ip int br\n')

# Configuration changes
mytel.write(b'conf t\n')
mytel.write(b'interface Loopback55\n')
mytel.write(b'ip address 55.5.5.5 255.255.255.0\n')
mytel.write(b'end\n')

# Display new interface configuration
mytel.write(b'show ip int br\n')

# Exit the session
mytel.write(b'exit\n')

# Read all output and print
output = mytel.read_all().decode('ascii')
print(output)

'''
# Pause to allow the user to read the output
input('Press Enter to Continue')

# Closing the connection
mytel.close()
'''