#include <bits/stdc++.h>
using namespace std;

void rleEncoding()
{

    ifstream input;
    input.open("input.txt");

    ofstream output;
    output.open("encrypted.txt");

    string str;
    bool flag = false;
    int i, j;

    while (getline(input, str))
    {

        if (flag)
        {
            output << endl;
        }
        for (i = 0; i < str.size(); i++)
        {
            int cnt = 0;
            for (j = i; str[j] == str[i]; j++)
            {
                cnt++;
            }

            if (cnt > 1)
            {
                output << (char)255 <<(char)cnt << str[i];
            }
            else
            {
                output << str[i];
            }

            i = j - 1;
        }
        flag = true;
    }
    input.close();
    output.close();
}

void rleDecoding(){
    ifstream input;
    ofstream output;
    input.open("encrypted.txt");
    output.open("decrypted.txt");

    int i,j;
    bool flag = false;
    string s;
    while(getline(input,s)){
        if(flag)
            output<<endl;

        for(i=0;i<s.size();i++){
            if(s[i]==char(255)){
                for(j=0;j<(int)s[i+1];j++)
                    output<<s[i+2];
                i+=2;
            }
            
            else
                output<<s[i];

        }
        flag=true;
    }
    input.close();
    output.close();

}

int main()
{

    rleEncoding();
    rleDecoding();
    return 0;
}