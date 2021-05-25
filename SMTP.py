from socket import *
import base64 # module

msg = "\r\n I love Computer Networks !"
endmsg = "\r\n.\r\n"

mailserver = ("mail.smtp2go.com", 2525)

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(mailserver)

recv = clientSocket.recv(1024).decode()
print("Message after connection request: " + recv)
if recv[:3] != '220':
    print('220 reply not received from server.')


# Send EHLO command and print server response.

# Same as HELO but tells the server that the client may want to use the 
# Extended SMTP (ESMTP) protocol instead.

# The client sends this command to the SMTP server to identify itself 
# and initiate the SMTP conversation.
heloCommand = 'EHLO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')


# After the client has sent the EHLO command to the server, 
# the server often sends a list of available ESMTP commands back to the client.


# After that the AUTH LOGIN command has been sent to the server, the server asks for 
# username and password by sending BASE64 encoded text (questions) to the client


# Info for username and password
# SMTP Authentication is part of Extended SMTP, which is initiated with the EHLO command
username =  "19021293@vnu.edu.vn" # the username for your server
password = "Hung2712" # the password for your server
base64_str = ("\x00" + username + "\x00" + password).encode()
base64_str = base64.b64encode(base64_str)
authMsg = "AUTH PLAIN ".encode() + base64_str + "\r\n".encode()
clientSocket.send(authMsg)
recv_auth = clientSocket.recv(1024)
print(recv_auth.decode())
if recv1[:3] != '250':
    print('250 reply not received from server.')


# Send MAIL FROM command and print server response.

# Use the MAIL FROM command to specify the e-mail address of the sender.

# This command also tells the SMTP server that a new mail transaction is starting and 
# makes the server to reset all its state tables and buffers etc.

# '<>': Specifies the full path address of the sender of the mail.
mailFrom = "MAIL FROM: <anyemailid@gmail.com> \r\n"
clientSocket.send(mailFrom.encode())
recv2 = clientSocket.recv(1024).decode()
print("After MAIL FROM command: "+ recv2)
if recv1[:3] != '250':
    print('250 reply not received from server.')


# Send RCPT TO command and print server response.

# Use the RCPT TO command to specify the e-mail address of the recipients.

# This command can be repeated multiple times for a given e-mail message in order to 
# deliver a single e-mail message to multiple recipients.

# '<>': Specifies the full path address of the mail recipient.
rcptTo = "RCPT TO: <hungdoan2712@gmail.com> \r\n"
clientSocket.send(rcptTo.encode())
recv3 = clientSocket.recv(1024).decode()
print("After RCPT TO command: " + recv3)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Send DATA command and print server response.

# The DATA command informs the server that now will the message data be sent 
# (e-mail header, body text etc). 
data = "DATA\r\n"
clientSocket.send(data.encode())
recv4 = clientSocket.recv(1024).decode()
print("After DATA command: " + recv4)
if recv1[:3] != '250':
    print('250 reply not received from server.')


# Send message data.
# The single dot below the message contents informs the SMTP server when the message data ends. 
# After a single dot has been sent to the server and the server has responded, 
# a QUIT command is sent to terminate the session.
subject = "Subject: SMTP mail client testing \r\n" 
clientSocket.send(subject.encode())
clientSocket.send(msg.encode())
clientSocket.send(endmsg.encode())
recv_msg = clientSocket.recv(1024)
print("Response after sending message body: " + recv_msg.decode())
if recv1[:3] != '250':
    print('250 reply not received from server.')


# Send QUIT command and get server response.
# Use the QUIT command to end SMTP processing.
clientSocket.send("QUIT\r\n".encode())
message = clientSocket.recv(1024)
print(message.decode())
clientSocket.close()