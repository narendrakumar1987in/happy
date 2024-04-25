from telnetlib import Telnet

# User input for command
cmd_exec = input('Enter the Command: ')

# Establishing a connection
mytel = Telnet('192.168.18.74')

# Login credentials
mytel.write(b'khawar\n')
mytel.write(b'cisco\n')

# Ensuring the terminal does not paginate the output
mytel.write(b'terminal length 0\n')

# Sending the user's command
mytel.write(cmd_exec.encode('ascii') + b'\n')

# Exiting the Telnet session
mytel.write(b'exit\n')

# Reading and decoding all the data from the server until the connection is closed
output = mytel.read_all().decode('ascii')
print(output)

# Pause to allow the user to read the output
input('Press Enter to Continue')

# Closing the connection
mytel.close()
