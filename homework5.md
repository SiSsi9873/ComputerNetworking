- P1

y-x-u, y-x-v-u, y-x-w-u, y-x-w-v-u,

y-w-u, y-w-v-u, y-w-x-u, y-w-x-v-u, y-w-v-x-u,

y-z-w-u, y-z-w-v-u, y-z-w-x-u, y-z-w-x-v-u, y-z-w-v-x-u

- P3

Step	| N’ | D(t),p(t)|	D(u),p(u)|	D(v),p(v)|	D(w),p(w)|	D(y),p(y)|	D(z),p(z)
---|---|---|---|---|---|---|---
0	|x	|∞	|∞	|3,x	|6,x	|6,x	|8,x
1	|xv	|7,v	|6,v	|3,x	|6,x	|6,x	|8,x
2	|xvu	|7,v	|6,v	|3,x	|6,x	|6,x	|8,x
3	|xvuw	|7,v	|6,v	|3,x	|6,x	|6,x	|8,x
4	|xvuwy	|7,v	|6,v	|3,x	|6,x	|6,x	|8,x
5	|xvuwyt	|7,v	|6,v	|3,x	|6,x	|6,x	|8,x
6	|xvuwytz	|7,v	|6,v	|3,x	|6,x	|6,x	|8,x

- P9

NO, this is because that decreasing link cost won’t cause a loop (caused by the next-hop relation of between two nodes of that link). Connecting two nodes with a link is equivalent to decreasing the link weight from infinite to the finite weight.

- P15

a)I1 because this interface begins the least cost path from 1d towards the gateway router 1c.

b)I2. Both routes have equal AS-PATH length but I2 begins the path that has the closest NEXT-HOP router.

c)I1. I1 begins the path that has the shortest AS-PATH.

- P18
BitTorrent file sharing and Skype P2P applications.

Consider a BitTorrent file sharing network in which peer 1, 2, and 3 are in stub networks W, X, and Y respectively. Due the mechanism of BitTorrent’s file sharing, it is quire possible that peer 2 gets data chunks from peer 1 and then forwards those data chunks to 3. This is equivalent to B forwarding data that is finally destined to stub network Y.

