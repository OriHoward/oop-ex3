# oop-ex3



## Detailed execution details of the algorithms
Times in java:

| Graph Size | isConnected | Center  |   TSP   | load     | save    |      shortestPath           |
|------------|-------------|---------|---------|----------|---------|-----------------------------|
| 1000       |   380msec   | 1.6 sec |   3sec  |201ms     |376ms    |239msec (100 to 312)         |
| 10k        |   1.9sec    | 4.1 Min |   20sec |558ms     | 200ms   |726msec (819 to 4012)        |
| 100k       |   17sec     |too long |1m,15sec |5.6sec    |9.2sec   |7.125sec(12933 to 44311)     |
| 1M         |   51sec     |too long |too long |15.7sec   |34.1sec  |24.5sec(312343 to 521256)    |
| G1 (16)    |   79msec    |  81msec |   67ms  | 17ms     | 90ms    |74msec (1 to 8)              |
| G2 (31)    |   84msec    |  90msec |   93ms  | 17ms     | 92ms    |91msec (5 to 13)             |
| G3 (48)    |   93msec    | 101msec |   92ms  | 37ms     | 78ms    |91msec (26 to 46)            |

times in python:

| Graph Size | isConnected | Center  |   TSP   | load   | save |             shortestPath        |
|------------|-------------|---------|---------|------  |------|---------------------------------|
| 1000       |   220msec   | 29 sec  | 400ms   |43ms    |150ms |84msec (100 to 312)              |
| 10k        |   2.3sec    |too long | 22sec   |542ms   |1.5sec|134msec (819 to 4012)            |
| 100k       |  82.388sec  |too long | 2 min   |12.7sec |32.5s |32.9sec (12933 to 44311          |
| 1M         | 3min,50sec  |too long |too long |35.7ec  |1m.30s| 2min (312343 to 521256)                                |
| G1 (16)    |   4msec     |  11msec |   4ms   |   3ms  |  4ms |1msec (1 to 8)                   |
| G2 (31)    |   4msec     |  9msec  |   7ms   |   5ms  |  2ms |2msec (5 to 13)                  |
| G3 (48)    |   5msec     | 27msec  |   12ms  |   6ms  |  3ms |3msec (26 to 46)                 |
