# oop-ex3



## Detailed execution details of the algorithms
Times in java:

| Graph Size | isConnected | Center  |   TSP   | load     | save |      shortestPath           |
|------------|-------------|---------|---------|----------|------|-----------------------------|
| 1000       |   380msec   | 1.6 sec |         |201ms     | 30ms |239msec (100 to 312)         |
| 10k        |   1.9sec    | 4.1 Min |         |558ms     | 31ms |726msec (819 to 4012)        |
| 100k       |   17sec     |too long |         |5.6sec    | 55ms |7.125sec(12933 to 44311)     |
| 1M         |   51sec     |too long |         |15.7sec   | 78ms |24.5sec(312343 to 521256)    |
| G1 (16)    |   79msec    |  81msec |         | 17ms     | 29ms |74msec (1 to 8)              |
| G2 (31)    |   84msec    |  90msec |         | 17ms     | 38ms |91msec (5 to 13)             |
| G3 (48)    |   93msec    | 101msec |         | 37ms     | 28ms |91msec (26 to 46)            |

times in python:

| Graph Size | isConnected | Center  |   TSP   | load   | save |             shortestPath        |
|------------|-------------|---------|---------|------  |------|---------------------------------|
| 1000       |   220msec   | 29 sec  |         |43ms    | 4ms  |84msec (100 to 312)              |
| 10k        |   2.3sec    |too long |         |542ms   | 4ms  |134msec (819 to 4012)            |
| 100k       |  82.388sec  |too long |         |12.7sec | 22ms |32.9sec (12933 to 44311          |
| 1M         | 3min,50sec  |too long |         |        |      |                                 |
| G1 (16)    |   4msec     |  11msec |         |   3ms  |  4ms |1msec (1 to 8)                   |
| G2 (31)    |   4msec     |  9msec  |         |   5ms  |  2ms |2msec (5 to 13)                  |
| G3 (48)    |   5msec     | 27msec  |         |   6ms  |  3ms |3msec (26 to 46)                 |
