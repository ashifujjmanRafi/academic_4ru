#include <bits/stdc++.h>
using namespace std;

string cipher(string s,int key){
    string cipher = "";
    for(int i = 0;i<s.size();i++){
        int temp = 0;
        if(isupper(s[i])){
            temp = (s[i]- 'A'+key)%26;
            cipher += (temp + 'A');
        }
        else if(islower(s[i])){
            temp = (s[i]- 'a'+key)%26;
            cipher += (temp + 'a');
        }
        else
            cipher += s[i];
    }
    return cipher;
}

string decipher(string s,int key){
    string dec = "";
    for(int i = 0;i<s.size();i++){
        int temp = 0;
        if(isupper(s[i])){
            temp = (s[i]-'A'+26-key)%26;
            dec += temp + 'A';
        }
        else if(islower(s[i])){
            temp = (s[i]-'a'+26-key)%26;
            dec += temp + 'a';
        }
        else
            dec += s[i];
    }
    return dec;
}

int main(){

    string s;
    getline(cin,s);
    int key = 3;
    string enc = cipher(s,key);
    cout<<enc<<endl;
    string dec = decipher(enc,key);
    cout<<dec<<endl;
return 0;
}