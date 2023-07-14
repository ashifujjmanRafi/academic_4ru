#include <bits/stdc++.h>
using namespace std;

void encoding(){
    ifstream input;
    input.open("input.txt");

    ofstream output;
    output.open("encrypted.txt");

    string s;
    bool flag = false;
    int i,j;

    while(getline(input,s)){
        if(flag)
            output<<endl;
        for(i=0;i<s.size();i++){
            int cnt = 0;
            for(j=i;s[i]==s[j];j++)
                cnt++;
            if(cnt>1)
                output<<(char)255<<(char)cnt<<s[i];
            else
                output<<s[i];
            i=j-1;
        }
        flag = true;
    }
    input.close();
    output.close();
}

void decoding(){

    ifstream input;
    input.open("encrypted.txt");

    ofstream output;
    output.open("decrypted.txt");

    string s;
    bool flag = false;
    int i,j;

    while(getline(input,s)){
        if(flag)
            output<<endl;
        for(i=0;i<s.size();i++){
            if(s[i]==(char)255){
                for(j=0;j<(int)s[i+1];j++){
                    output<<s[i+2];
                }
                i = i+2;
            }
            else
                output<<s[i];
        }
        flag = true;
    }
    input.close();
    output.close();
    
}

int main(){
    encoding();
    decoding();
}