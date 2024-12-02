#include <algorithm>
#include <fstream>
#include <iostream>
#include <numeric>
#include <vector>

int main()
{
    int elf = 0;
    std::vector<int> topThreeElves = {0, 0, 0};
    std::ifstream input("input.txt");

    for (std::string line; std::getline(input, line);)
    {
        if (line.empty())
        {
            if (elf > *min_element(topThreeElves.begin(), topThreeElves.end()))
            {
                topThreeElves.erase(min_element(topThreeElves.begin(), topThreeElves.end()));
                topThreeElves.push_back(elf);
            }
            elf = 0;
        }
        else
        {
            elf += std::stoi(line);
        }
    }

    std::cout << "The total is " << accumulate(topThreeElves.begin(), topThreeElves.end(), 0) << std::endl;
}