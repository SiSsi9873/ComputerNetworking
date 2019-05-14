- P6

a)we get 1000110000, with a remainder of R=0000.

b)we get 0101010101, with a remainder of R=1111.

c)we get 1011010111, with a remainder of R=1001.
- P7

a)Without loss of generality, suppose ith bit is flipped, where 0<= i <= d+r-1 and assume that the least significant bit is 0th bit.   
A single bit error means that the received data is K=D*2r XOR R + 2i. It is clear that if we divide K by G, then the reminder is not zero.
In general, if G contains at least two 1’s, then a single bit error can always be detected. 

b)The key insight here is that G can be divided by 11 (binary number), but any number of odd-number of 1’s cannot be divided by 11. 
Thus, a sequence (not necessarily contiguous) of odd-number bit errors cannot be divided by 11, thus it cannot be divided by G. 
- P10

a)A’s average throughput is given by pA(1-pB).  
Total efficiency is pA(1-pB) + pB(1-pA).

b)A’s throughput is pA(1-pB)=2pB(1-pB)= 2pB- 2(pB)2. 
B’s throughput is pB(1-pA)=pB(1-2pB)= pB- 2(pB)2. 
Clearly, A’s throughput is not twice as large as B’s. 
In order to make pA(1-pB)= 2 pB(1-pA), we need that pA= 2 – (pA / pB).

c)A’s throughput is 2p(1-p)N-1, and any other node has throughput p(1-p)N-2(1-2p).
- P18

At t=0, A transmits. At t=576, A would finish transmitting. In the worst case, B begins transmitting at time t=324, 
which is the time right before the first bit of A’s frame arrives at B. At time t=324+325=649 's first bit arrives at A.
Because 649> 576, A finishes transmitting before it detects that B has transmitted. So A incorrectly thinks that its frame was successfully transmitted without a collision.

- P24

Each departmental hub is a single collision domain that can have a maximum throughput of 100 Mbps. 
The links connecting the web server and the mail server has a maximum throughput of 100 Mbps.
Hence, if the three collision domains and the web server and mail server send out data at their maximum possible rates of 100 Mbps each, 
a maximum total aggregate throughput of 500 Mbps can be achieved among the 11 end systems.
