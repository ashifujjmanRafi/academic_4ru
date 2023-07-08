#include <bits/stdc++.h>
using namespace std;

string cipher(string s, int key)
{
    string out = "";
    for (int i = 0; i < key; i++)
    {
        for (int j = i; j < s.size();)
        {
            out += s[j];
            j += key;
        }
    }
    return out;
}

string decipher(string s, int key)
{
    string out = "";
    int temp = s.size() % key;
    int row = s.size() / key;
    if (temp)
        row++;
    int total = 0;
    for (int i = 0; i < row; i++)
    {
        temp = s.size() % key;
        if (temp)
        {
            for (int j = i; j < s.size();)
            {
                out += s[j];
                if (temp)
                {
                    j += row;
                    temp--;
                }
                else
                    j += row - 1;

                total++;
                if (total == s.size())
                    break;
            }
        }
        else
        {
            for (int j = i; j < s.size();)
            {
                out += s[j];
                j += row;
            }
        }
    }
    return out;
}

string transposition(string s,int key){
    string out = cipher(cipher(s,key),key);
    return out;
}

string reversetransposition(string s,int key){
    string out = decipher(decipher(s,key),key);
    return out;
}


int main()
{
    string text = "i am ashifujjman";
    int key;
    cin >> key;
    string enc = transposition(text, key);
    cout << enc << endl;
    string dec = reversetransposition(enc, key);
    cout << dec << endl;
}