from logic import get_test_string, delete_pairs_iteratively, count_open_close

import time

for _ in range(20):
    s = get_test_string(100_000)
    t0 = time.time()
    r1 = delete_pairs_iteratively(s)
    t1 = time.time()
    r2 = count_open_close(s)
    t2 = time.time()
    if r1 == r2:
        print(f"{r1} {t1-t0} {t2-t1}")