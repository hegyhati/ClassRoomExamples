from logic import get_test_string, delete_pairs_iteratively, count_open_close

import timeit


print("basic")

for _ in range(20):
    s = get_test_string(100_000)
    t1 = timeit.timeit(f"delete_pairs_iteratively(\"{s}\")", setup="from logic import delete_pairs_iteratively", number=1) 
    t2 = timeit.timeit(f"count_open_close(\"{s}\")", setup="from logic import count_open_close", number=1) 
    print(f"{t1} {t2}")
    
print("lambda")

for _ in range(20):
    s = get_test_string(100_000)
    t1 = timeit.timeit(lambda: delete_pairs_iteratively(s), number=1) 
    t2 = timeit.timeit(lambda: count_open_close(s), number=1) 
    print(f"{t1} {t2}")