- P2.

从B到A：源端口-80，源IP-B；  目的端口-26145，目的IP-C

从B到C：左边的连接：源端口-80，源IP-B；目的端口-26145，目的IP-C

右边的连接：源端口-80，源IP-B；目的端口-7532，目的IP-C
- P4.

a. 00111110

b. 01000000

c. a中字节分别变为：01011101、01100100
- P7.

ACK分组没有序号是因为接收方、发送方都不需要该序号
- P28.

TCP 让发送方 A 维护一个接收窗口来提供流量控制，主机 B 将实时的 rwnd 值放入发给 A 的报文中，通知 B 的缓存大小。

A 确保 LastByteSent - LastByteAcked <= rwnd，当缓存不足时，将暂停向 B 发送数据。
- P54.

优点是无需经历慢启动过程

缺点是 t1 时刻的 cwnd 和 ssthresh 比较陈旧，不能正确反映 t2 时刻的线路拥塞状态
