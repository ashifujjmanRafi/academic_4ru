#include <bits/stdc++.h>
using namespace std;

void RLE_encode(const string &input_file, const string &output_file)
{
    ifstream fin(input_file);
    ofstream fout(output_file);

    string str;
    int i, j;
    bool flag = false;

    while (getline(fin, str))
    {
        if (flag)
        {
            fout << endl;
        }

        for (i = 0; i < str.size(); i++)
        {
            int cnt = 0;
            for (j = i; str[j] == str[i]; j++)
            {
                cnt++;
            }

            fout << str[i] << "(" << (char)cnt << ")";
            i = j - 1;
        }

        flag = true;
    }

    fin.close();
    fout.close();
}

void RLE_decode(const string &input_file, const string &output_file)
{
    ifstream fin(input_file);
    ofstream fout(output_file);

    string str;
    int i, j;
    bool flag = false;

    while (getline(fin, str))
    {
        if (flag)
        {
            fout << endl;
        }

        for (i = 0; str[i]; i++)
        {
            if (str[i] == '(')
            {
                int cnt = 0;
                for (j = i + 1; str[j] && str[j] != ')'; j++)
                {
                    //cout<<(int)str[j]<<endl;
                    cnt = cnt * 10 + (int)str[j];
                }
                cout<<cnt<<endl;
                for (j = 0; j < abs(cnt); j++)
                {
                    fout << str[i - 1];
                }
            }
        }

        flag = true;
    }

    fin.close();
    fout.close();
}

int main()
{
    string input_file = "input.txt";
    string compressed_file = "compressed.txt";
    string decompressed_file = "decompressed.txt";

    RLE_encode(input_file, compressed_file);
    RLE_decode(compressed_file, decompressed_file);

    return 0;
}
