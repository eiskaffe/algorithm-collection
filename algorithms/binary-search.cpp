#include <iostream>

int binarySearch(int array[], int len, int x) {
    // Time complexity: O(log N)
    int high = len;
    int low = 0;
    int mid;
    while (low <= high) {
        mid = (low + high) / 2;
        if (array[mid] == x) {
            return mid;
        }
        else if (array[mid] < x) {
            low = mid + 1;
        }
        else {
            high = mid - 1;
        }
    }
    return -1;
}

int main() {
    int length = 10;
    int sampleArray[length] = {1, 2, 3, 4, 5, 6, 7, 8 , 9, 10};
    int x = 11;

    std::cout << binarySearch(sampleArray, length, x);

    return 0;
}