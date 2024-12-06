/**
 * Someone else's solution. Really liked it.
 * Unfortunatelly, I couldn't solve it by myself.
 */
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <set>
#include <array>
#include <utility>
#include <algorithm>
#include <type_traits>

template<typename T>
struct Coord
{
    bool operator <  (const Coord& p) const {
        if (x < p.x) return true;
        else if (p.x < x) return false;
        else return y < p.y;
    }

    Coord operator + (const Coord& p) const {
        return Coord{x + p.x, y + p.y};
    }

    template<typename U>
    typename std::enable_if<std::is_integral<T>::value, bool>::type
    Within(const U& grid) const {
        return x >= 0 && y >= 0 && x < grid.size() && y < grid[x].size();
    }

    template<typename U>
    typename std::enable_if<std::is_integral<T>::value, typename U::value_type::value_type>::type
    GetAt(const U& grid) const {
        return grid[x][y];
    }

    T x = {}, y = {};
};

using Point = Coord<int>;
const std::array<Point, 4> directions = {Point{-1, 0}, Point{0, 1}, Point{1, 0}, Point{0, -1}};

using Guard = std::pair<Point, int>;

std::string file = "6.txt";

int main(int argc, char* argv[])
{
    auto ChronoStart = std::chrono::high_resolution_clock::now();

    std::ifstream in(file);
    if (!in)
    {
        std::cerr << "Could not open inputFilename " << argv[1] << "\n";
        return -1;
    }

    std::string line;
    std::vector<std::string> map;
    Point guard;
    int dir = 0, part2 = 0;

    while (std::getline(in, line))
    {
        auto pos = line.find('^');
        if (pos != std::string::npos)
            guard = Point{static_cast<int>(map.size()), static_cast<int>(pos)};
        map.push_back(std::move(line));
    }
    Guard testStart = {guard, 0};

    std::set<Point> visited = {guard};
    while (true)
    {
        Point np = guard + directions[dir];
        if (!np.Within(map))
            break;
        if (np.GetAt(map) == '#')
            dir = (dir + 1) % 4;
        else
        {
            guard = np;
            visited.insert(guard);
        }
    }

    for (int x = 0; x < map.size(); ++x)
    {
        for (int y = 0; y < map.front().size(); ++y)
        {
            if (map[x][y] == '.' && visited.find({x, y}) != visited.end())
            {
                map[x][y] = '#';

                std::set<Guard> check = {testStart};
                guard = testStart.first;
                dir = 0;

                while (true)
                {
                    Point np = guard + directions[dir];
                    if (!np.Within(map))
                        break;
                    if (np.GetAt(map) == '#')
                        dir = (dir + 1) % 4;
                    else
                        guard = np;

                    if (!check.insert({np, dir}).second)
                    {
                        ++part2;
                        break;
                    }
                }
                map[x][y] = '.';
            }
        }
    }

    std::cout << "Part 1: " << visited.size() << "\n";
    std::cout << "Part 2: " << part2 << "\n";

    return 0;
}
