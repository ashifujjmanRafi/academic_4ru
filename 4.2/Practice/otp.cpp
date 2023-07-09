#include <bits/stdc++.h>
using namespace std;


string cipher(string s,string pad){
    string out = "";
    for(int i = 0 ;i<s.size();i++){
        if(isupper(s[i])){
            int temp = (s[i]-'A'+pad[i]-'a')%26;
            out+=temp+'A';
        }
        else if(islower(s[i])){
            int temp = (s[i]-'a'+pad[i]-'a')%26;
            out+=temp+'a';
        }
        else 
            out+=s[i];
    }
    return out;
}


string decipher(string s,string pad){
    string out = "";
    for(int i = 0 ;i<s.size();i++){
        if(isupper(s[i])){
            int temp = (s[i]-'A'-pad[i]+'a'+26)%26;
            out+=temp+'A';
        }
        else if(islower(s[i])){
            int temp = (s[i]-'a'-pad[i]+'a'+26)%26;
            out+=temp+'a';
        }
        else 
            out+=s[i];
    }
    return out;
}


int main(){
    string pad = "jgjojgogosnlvsioghiowjgpoqjphtuihguilshuihvsiohgowihognwifvnsilbvils";
    string in = "DEPERTMENT OF COMPUTER SCIENCE AND ENGINEERING";

    cout<<cipher(in,pad)<<endl;
    cout<<decipher(cipher(in,pad),pad)<<endl;


    return 0;
}