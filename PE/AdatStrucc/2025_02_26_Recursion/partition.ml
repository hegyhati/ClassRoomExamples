let rec partition_max number max_number =
    match (number, max_number) with
    | (_, 1) -> 1
    | (1, _) -> 1
    | (n, k) when k>n -> partition_max n n
    | (n, k) when n==k -> 1 + partition_max n (n - 1)
    | (n, k) -> partition_max n (k - 1) + partition_max (n - k) k
;;

print_int (partition_max 10 10);
print_int (partition_max 100 100);
print_newline ();;