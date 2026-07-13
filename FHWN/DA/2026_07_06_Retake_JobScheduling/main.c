#include <stdio.h>
#include <stdlib.h>

#define DEBUG 1
#define debug(...) do { if (DEBUG) printf(__VA_ARGS__); } while (0)



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


JobOrder* EDD(const Jobs * const jobs ) {
    JobOrder* order = NULL;
    // TODO 
    return order;
}

JobOrder* SPT(const Jobs * const jobs ) {
    JobOrder* order = NULL;
    // TODO 
    return order;
}


int total_tardiness(const Jobs* const jobs, const JobOrder* const order) {
    // TODO
    return -1;
}


int main() {
    Jobs* jobs = read_jobs("jobs_large.txt");
    
    
    JobOrder* edd_order = EDD(jobs);
    printf("Total tardiness with EDD order disregarding dependencies: %d\n", total_tardiness(jobs,edd_order));
    deallocate_joborder(&edd_order);
    
    JobOrder* spt_order = SPT(jobs);
    printf("Total tardiness with SPT order respecting dependencies: %d\n", total_tardiness(jobs,spt_order));    
    deallocate_joborder(&spt_order);
    
    deallocate_jobs(&jobs);
    return 0;
}