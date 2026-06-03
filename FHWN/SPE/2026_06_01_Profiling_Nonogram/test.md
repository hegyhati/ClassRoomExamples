# Web version

Get `httplib.h` from [here](https://github.com/yhirose/cpp-httplib).

```bash
$ g++ main.cpp -o web
$ ./web
```

## Enpoints examples:

## `/txt2clue/{comma_separated_number_list}`

Just parses a string into an array of numbers, and returns it as a JSON array.

```bash
$ curl http://localhost:8080/txt2clue/3,3,4,5,6
[3,3,4,5,6]
```

## `/line2clue/{complete line 1=filled 0=empty}`

Parses a complete line (only 1s and 0s) and returns the clues for that (as a JSON array).

```bash
$ curl http://localhost:8080/line2clue/11001110000001111111111111111111111111111110001
[2,3,30,1]
```

# `/lines4line/{partial line 1=filled 0=empty _=unknown}`

Returns each possible complete lines for a partial line as strings in a JSON array.

```bash
$ curl http://localhost:8080/lines4line/1_0_0
["11010","11000","10010","10000"]
```

# `/deduce/{partial line 1=filled 0=empty _=unknown}/{clues comma separated}`

Does a local deduction, returns a new partial line.

```bash 
$ curl http://localhost:8080/deduce/________________________/3,1,6,4,3
"_________111____1_______"
$ curl http://localhost:8080/deduce/1______________________1/3,1,6,4,3
"1110_____111____1___0111"
```

# Local test

Basically locally running the last endpoint.

```bash
$ g++ test.cpp -o test
$ ./test 1______________________1 3,1,6,4,3
1110_____111____1___0111
```

## Profiling with valgrind + callgrind

```bash
$ valgrind --tool=callgrind ./test 1______________________1 3,1,6,4,3

==71124== Callgrind, a call-graph generating cache profiler
==71124== Copyright (C) 2002-2017, and GNU GPL'd, by Josef Weidendorfer et al.
==71124== Using Valgrind-3.24.0 and LibVEX; rerun with -h for copyright info
==71124== Command: ./test 1______________________1 3,1,6,4,3
==71124== 
==71124== For interactive control, run 'callgrind_control -h'.
==71124== brk segment overflow in thread #1: can't grow to 0x4844000
==71124== (see section Limitations in user manual)
==71124== NOTE: further instances of this message will not be shown
1110_____111____1___0111
==71124== 
==71124== Events    : Ir
==71124== Collected : 61605041302
==71124== 
==71124== I   refs:      61,605,041,302
```

Note: it is WAY slower:

```bash
$ time ./test 1______________________1 3,1,6,4,3
1110_____111____1___0111

real	0m4.641s
user	0m4.428s
sys	    0m0.212s

$ time valgrind --tool=callgrind ./test 1______________________1 3,1,6,4,3
==79950== Callgrind, a call-graph generating cache profiler
==79950== Copyright (C) 2002-2017, and GNU GPL'd, by Josef Weidendorfer et al.
==79950== Using Valgrind-3.24.0 and LibVEX; rerun with -h for copyright info
==79950== Command: ./test 1______________________1 3,1,6,4,3
==79950== 
==79950== For interactive control, run 'callgrind_control -h'.
==79950== brk segment overflow in thread #1: can't grow to 0x4844000
==79950== (see section Limitations in user manual)
==79950== NOTE: further instances of this message will not be shown
1110_____111____1___0111
==79950== 
==79950== Events    : Ir
==79950== Collected : 61605041302
==79950== 
==79950== I   refs:      61,605,041,302

real	4m46.221s
user	4m45.863s
sys	    0m0.344s

```

Generates [`callgrind.out.{}`](./callgrind.out.71124).

Open it with [kcachegrind](https://kcachegrind.github.io/html/Home.html).


## Profiling with perf

```bash
$ time perf record ./test 1______________________1 3,1,6,4,3
1110_____111____1___0111
[ perf record: Woken up 3 times to write data ]
[ perf record: Captured and wrote 0.937 MB perf.data (19584 samples) ]

real	0m5.226s
user	0m4.714s
sys	    0m0.428s
```

Creates [`perf.data`](./perf.data) (binary).

Data can be looked at with `perf report` TUI.

This version only records the current top stackframe, use `-g` for complete callstack.

Then:

```bash
$ perf script > out.perf
$ git clone https://github.com/brendangregg/FlameGraph
$ FlameGraph/stackcollapse-perf.pl out.perf > folded.txt
$ FlameGraph/flamegraph.pl folded.txt > flamegraph.svg
```

to create a Flamegraph.


