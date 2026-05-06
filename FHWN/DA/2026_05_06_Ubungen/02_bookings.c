/* 

Bookings

We operate an Airbnb, and received a bunch of booking requests. 
Each request consists of:
 - name (max 31 char) of the client
 - starting day of booking
 - ending day of booking

Days are simply numbers.  

As we are new on the market, our goal is to get as many 5 star reviews as possible. 
For that reason, we don't allow "tight booking", i.e., if a client leaves on day 4, another client cannot arrive on the same day, earliest possible is day 5, so that we have a day for cleaning, refilling, etc.

We want to find the maximum number of bookings (and thus 5star reviews) among the requests. 

Mathematically this problem is equivalent of finding tha largest independet (non-overlapping) subset of an interval system (set of intervals). 
Luckily, there is a well known algorithm for that: 
 1.) Sort all the intervals in increasing order based on their right endpoints (ending day of booking)
 2.) Select the first interval, and add it to the system (confirm the booking)
 3.) Continue going through the elements of the array, and for each booking:
  - if the it contains the endpoint of the included booking, just skip it.
  - if not, add it to the system (confirm it), and continue, but use this bookings endpoint from now.

 Implement this algorithm, and provide the maximal number of "mutually confirmable bookings".

 You CANNOT change main.

 (Plan carefully, what the Bookings struct should entail)

*/


struct Bookings {

}

int main(int argc, char** argv) {
    if (argc < 2) {
        printf("Provide the input file as command line argument.\n");
        return -1;
    }

    struct Bookings requests = read_bookings(argv[1]);
    struct Bookings confirmed = max_independent(requests);
    printf("Confirmed requests: ");
    print_bookings(confirmed);
    release(requests);
    release(confirmed);

    return 0;
}