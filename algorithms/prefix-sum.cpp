#include <iostream>
#include <vector>

std::vector<int> prefixSum(std::vector<int> in_vector) {
    std::vector<int> prefix = {0};
    int current = 0;
    for (int i = 0; i < in_vector.size(); i++) {
        current += in_vector[i];
        prefix.push_back(current);
    }
    return prefix;
}

int main() {
    std::vector<int> vector{1, 2, 3, 4};
    std::vector<int> sum = prefixSum(vector);
    for (int val : sum) {
        std::cout << val << " ";
    }
    return 0;
}