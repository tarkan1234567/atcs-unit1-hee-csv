#include <iostream>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
using namespace std;

int main() {
    set<int> orderedValues;
    map<int, int> orderedMap;

    unordered_set<int> unorderedValues;
    unordered_map<int, int> unorderedMap;

    int numbers[] = {30, 10, 50, 20, 40};

    for (int num : numbers) {
        orderedValues.insert(num);
        unorderedValues.insert(num);

        orderedMap[num] = num * 2;
        unorderedMap[num] = num * 2;
    }

    cout << "Ordered Set: ";
    for (int num : orderedValues)
        cout << num << " ";

    cout << "\nUnordered Set: ";
    for (int num : unorderedValues)
        cout << num << " ";

    cout << "\nOrdered Map: ";
    for (auto pair : orderedMap)
        cout << pair.first << ":" << pair.second << " ";

    cout << "\nUnordered Map: ";
    for (auto pair : unorderedMap)
        cout << pair.first << ":" << pair.second << " ";

    return 0;
}
