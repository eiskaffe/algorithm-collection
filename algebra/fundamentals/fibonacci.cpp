#include <iostream>
#include <bits/stdc++.h>

long long fib1(long long n) {
    if (n == 0 || n == 1) {
        return n;
    }
    return fib1(n - 1) + fib1(n - 2);
}

long long fib2(long long n) {
    long long a = 0;
    long long b = 1;
    long long tmp;
    for (int i = 0; i < n; i++) {
        tmp = b;
        b = a + b;
        a = tmp;
    }
    return a;
}

int main() {
    std::cout << "n=7 (recursive) " << fib1(7) << "\n";
    std::cout << "n=7 (loop) " << fib2(7) << "\n";
    std::cout << "---\n";
    std::cout << "n=10000 (recursive) " << fib1(10000) << "\n";
    std::cout << "n=10000 (loop) " << fib2(10000) << "\n";

    return 0;
}