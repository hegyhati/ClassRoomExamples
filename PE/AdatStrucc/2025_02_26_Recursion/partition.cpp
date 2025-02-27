#include <iostream>

int partition_max(int n, int k) {
    if (k==1) return 1;
    if (n==1) return 1;
    if (k>n) return partition_max(n,n);
    if (k==n) return 1 + partition_max(n,n-1);
    return partition_max(n-k,k) + partition_max(n,k-1);
}

int main() {
    std::cout << partition_max(10,10) << std::endl;
    std::cout << partition_max(100,100) << std::endl;
}