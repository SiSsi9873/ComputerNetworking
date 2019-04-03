- P2

a. No, you can only transmit one packet at a time over a shared bus.

b. No, as discussed in the text, only one memory read/write can be done at a time over the shared system bus. 

c. No, in this case the two packets would have to be sent over the same output bus at the same time, which is not possible. 
- P5

a. 
Prefix Match		|		Link Interface 
-------------- | --------------
11100000  00        |         0 
11100000  01000000  |        	1 
1110000				      |   	    2 
11100001  1			    |		      3	 
otherwise			      |       	3 

b.  Prefix match for first address is 5th entry: link interface 3

Prefix match for second address is 3nd  entry: link interface 2
      
Prefix match for third address is 4th  entry: link interface 3
- P7
Destination Address Range			|		Link Interface
-------------- | --------------
11000000 through (32 addresses)	11011111		|		 0
10000000 through (64 addresses)	10111111 		|		 1
11100000 through (32 addresses)	11111111		|		 2
00000000 through (128 addresses) 01111111   |    3   
- P8
223.1.17.0/26

223.1.17.128/25

223.1.17.192/28
- P14
The maximum size of data field in each fragment = 680 (because there are 20 bytes IP header). Thus the number of required fragments =[(2400-20)/680] = 4 
Each fragment will have Identification number 422. Each fragment except the last one will be of size 700 bytes (including IP header). The last datagram will be of size 360 bytes (including IP header). The offsets of the 4 fragments will be 0, 85, 170, 255. Each of the first 3 fragments will have flag=1; the last fragment will have flag=0.
                                                               

