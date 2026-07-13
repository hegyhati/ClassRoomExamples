# Job scheduling


## Overall goal

The task is to schedule all of the jobs in a file **on a single machine**. 

Each job has:
 - a processing time: time needed on the machine
 - deadline: the time by which the job should be completed
 - dependencies: other jobs that must be finished before this job.

The goal is to minimize **total tardiness**.
Tardiness is 0 if job is finished before its deadline, and `completion_time - deadline` if not.

## Input files

There are 3 input files to test, which follow this format:

```
JOBS <count>
<id> <processing_time> <deadline> | <dep_id> <dep_id> ... |
<id> <processing_time> <deadline> | <dep_id> <dep_id> ... |
<id> <processing_time> <deadline> | <dep_id> <dep_id> ... |
```

You can assume, that the IDs are integers in increasing order, starting from 0.

## General

 - Code that fails to compile or segfaults results in 0 points.
 - Code with memory leaks results in 50% of the points.
 - `main` must not be changed besides changing the name of the testfile.
 - You may alter any other functions, add helper functions, etc. 
 - `debug(...)` behaves like `printf` but can be turned off by a single macro change.
 - No need to handle any errors (file not there, file in wrong format, etc.).

## Tasks

### Basic structs & functions - 3 points



```C
typedef struct {
    // TODO
} Jobs;

Jobs* read_jobs(const char *filename)
{
    FILE *f = fopen(filename, "r");
    int jobcount, jobid, proctime, deadline, dependency; // buffer variables
    Jobs* jobs = NULL;

    fscanf(f, "JOBS %d", &jobcount);
    debug(" | %3d jobs found in file %s\n",jobcount, filename);
    // TODO

    for (int i = 0; i < jobcount; ++i) {
        fscanf(f, " %d %d %d | ", &jobid, &proctime, &deadline);
        debug(" | Job %3d has processing time of %2d and deadline of %3d, its dependencies are: ", jobid, proctime, deadline);
        //TODO 

        while (fscanf(f, " %d", &dependency) == 1) {
            debug(" Job %3d,", dependency);
            // TODO
        }
        fscanf(f, " |");
        debug("\n");
    }
    fclose(f);
    return jobs;
}

void deallocate_jobs(Jobs** pjobs) {
    // TODO
}
```

Design the struct in so that it holds all the information described above. Then extend the parsing function, and make a function that releases allocated memory.

**Pay attention** to pointers.
Only pointers to structs are stored in `main` / passed to functions / etc.

Minus 1 point, if dependency logic is not stored. 

### `JobOrder` struct & release function

This is just a simple array of integers, that can store the ids of jobs in the order the machine will execute them.

```c
typedef struct {
    int jobcount;
    int* jobids; 
} JobOrder;

void deallocate_joborder(JobOrder** porder) {
    if (*porder) {
        free((*porder)->jobids);
        free(*porder);
        *porder = NULL;
    }
}
```
### Tardiness calculation - 3 points

This function receives both the data about jobs, and an order (both as pointers!), and calculates the starting / completion time of each job, then computes the total tardiness. Machine starts working at time 0.

```c
int total_tardiness(const Jobs* const jobs, const JobOrder* const order) {
    // TODO
    return -1;
}
```

This function do not need to check if dependencies are satisfied.

Example:

| Job | proctime | deadline |
| --- | --- | --- |
| 0 | 3 |  5 |
| 1 | 6 | 9 |
| 2 | 4 | 6 |


If job order is `0,2,1`, then:

| Job | start | proctime | end | deadline | tardiness |
| --- | --- | --- | --- | --- | --- |
| 0 | 0 | 3 | 0+3 = 3 | 5 | 0 |
| 2 | 3 | 4 | 3+4 = 7 | 6 | 7-6 = 1 |
| 1 | 7 | 6 | 7+6 = 13 | 9 | 13-9 = 4 |


The total tardiness is 0+1+4 = 5. 


### EDD job order with NO dependencies - 4 points

EDD (Earliest Due Date) is simple strategy that sorts the jobs in the increasing order of their deadline. For the above example the EDD order would be `0,2,1`.

Implement this logic in the function below. 
If two jobs have the same due date, you can select the order arbitrary among them. 

You **DON'T** need to consider dependencies at all at this stage, but the function should run in at most `O(jobcount * log(jobcount))` time (in average case).

```c
JobOrder* EDD(const Jobs * const jobs ) {
    JobOrder* order = NULL;
    // TODO 
    return order;
}
```

### SPT job order WITH dependencies - 5 points

SPT (Shortest Processing Time) is another simple strategy, that selects, at each step the available job with the shortest processing time. 
The SPT order for the above example would be `0,2,1`, which was used as an example for tardiness calculation.

However, for this order **you need to consider the dependencies**. 
For example, if in the above example, Job 2 depends on job 1, then:
 - Initially only Job 0 and Job 1 can be started as they have no dependencies.
 - Job 0 has smaller proctime so it will be executed first.
 - After that, Job 2 cannot be selected yet, as it depends on Job 1, so Job 1 is now the job with minimal proctime.
 - After that finally Job 2 can be executed.


```c
JobOrder* SPT(const Jobs * const jobs ) {
    JobOrder* order = NULL;
    // TODO 
    return order;
}
```

For this strategy, there is no running time restriction.