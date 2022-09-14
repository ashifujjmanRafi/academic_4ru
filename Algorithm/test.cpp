// You have to build a wall using three columns of brick. Each brick has same width but unfortunately their height may vary. You can change the height of a column by removing and discarding its topmost brick any number of times.

// Find the maximum possible height of the column such that the wall’s height is not uneven. That means all of the columns are exactly same height. So, you must remove zero or more bricks from the top of zero or more of the three columns until they are all the same height, then return the height.


// Input:
// The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case contains three lines. The first line contains three space separated integers H1, H2 and H3 denoting the height of the three columns.

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    int t;
    cin >> t;
    while(t--)
    {
        int h1, h2, h3;
        cin >> h1 >> h2 >> h3;
        vector<int> v{h1, h2, h3};
        sort(v.begin(), v.end());
        cout << v[2] << endl;
    }
    return 0;
}