## 1. ping另外一台计算机
![ping](https://github.com/SiSsi9873/ComputerNetworking/blob/master/ping.png)
## 2. tracert一个服务器
![tracert](https://github.com/SiSsi9873/ComputerNetworking/blob/master/tracert.png)
## 3. 习题
- P2

共 N 段链路，编号为 1 2 … N+1；当 t1 = NL/R：

分组 1 到达地点 N+1，分组 2 到达 N，...，分组 P 到达地点 N-P+2；

从地点 N-P+2 到地点 N+1，花费时间（代入公式 1-1） t2 = (N + 1 - (N - P + 2)) L / R = (P - 1)L/R

因此 t = t1 + t2 = (N + P - 1)L/R
- P5

a.收费站将整个车队推向公路的时间为 t1 = (10辆车)/(5辆车/min) = 2 min;

两收费站之间距离 75 km，从一个收费站到另一个的时间 t2 = 75km/(100km/h) = 0.75 h;

总时间 d = 3t1 + 2t2 = 96 min

b. t1' = (8辆车)/(5辆车/min) = 1.6 min

d' = 3t1' + 2t2 = 94.8 min
- P7

主机 A 产生 56 字节的分组需要 = 56 * 8b / 64kbps = 7ms

传输时延 = 56 * 8b / 2Mbps = 0.224ms

总时间 = 7ms + 10ms + 0.224ms = 17.224ms
## 4. wireshark相关资源
[wireshark](https://github.com/SiSsi9873/wireshark)
