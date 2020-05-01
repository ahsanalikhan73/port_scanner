
If the response contains a TCP layer, we have to test its flags value. The flags are coded on 9 bits, the ones we consider here are the control bits (on 6 bits):

URG = 0x20
ACK = 0x10
PSH = 0x08
RST = 0x04
SYN = 0x02
FIN = 0x01

So if the response flags value is 0x12 we have a SYN/ACK: The port is open. We send back a RST packet so we do not establish a connection.

If the response flags value is 0x14 we have RST/ACK: The port is closed

