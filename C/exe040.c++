#include <iostream>
#include <unordered_map>
#include <vector>

int duplicados(const std::vector<int>& nums) {
    std::unordered_map<int, int> cont;
    int dup = 0;
    for (int num : nums) {
        cont[num]++;
    }
    for (auto it = cont.begin(); it != cont.end(); ++it) {
        dup += it->second - 1;
    }
    return dup;
}

int main() {
    std::vector<int> nums = {1, 2, 3, 1, 2, 4, 5, 4};
    std::cout << "Duplicados: " << duplicados(nums) << '\n';
}