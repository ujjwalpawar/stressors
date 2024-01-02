#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>
#include <time.h>

double timespec_to_seconds(struct timespec ts) {
    return (double)ts.tv_sec + (double)ts.tv_nsec / 1e9;
}

double time_passed(struct timespec start_time, struct timespec end_time) {
    double start_time_seconds = timespec_to_seconds(start_time);
    double end_time_seconds = timespec_to_seconds(end_time);
    return end_time_seconds - start_time_seconds;
}

int main(int argc, char *argv[]) {
    char *a = argv[1]; // stressor value used 165000 
    char *b = argv[2]; // number of times to run the stressor 
    char *filename = argv[3]; // file to write the timestamps to
    int fixed = atoi(a);  
    int j = 1000;
    int count = atoi(b);
    int k = 0;
    FILE *fp = fopen(filename, "w");
    if (fp == NULL) {
        printf("Failed to open file\n");
        exit(1);
    }
    while (k < count) {
        j = 1000;
        struct timespec start_time, end_time;
        clock_gettime(CLOCK_REALTIME, &start_time);
        while (j > 0) {
            while (i > 0) {
                i--;
            }
            usleep(500);
            i = fixed;
            j--;
        }
        clock_gettime(CLOCK_REALTIME, &end_time);
        double time_passed_seconds = time_passed(start_time, end_time);
        printf("Stress time %lf seconds\n", time_passed_seconds);
        printf("Sleeping for %lf seconds\n", 10.0 - time_passed_seconds);
        int sleep_time = (int)(10.0 - time_passed_seconds);
        printf("Sleeping for %d seconds\n", sleep_time);
        sleep(sleep_time);
        k++;
        fprintf(fp, "%lld,%lld\n", (long long)start_time.tv_sec * 1000000000LL + start_time.tv_nsec, (long long)end_time.tv_sec * 1000000000LL + end_time.tv_nsec);
    }
    fclose(fp);
    return 0;
}
