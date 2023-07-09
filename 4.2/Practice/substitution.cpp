#include <bits/stdc++.h>
using namespace std;

map<string,string> encode,decode;

void createDic(){
    ifstream input;
    input.open("dic.txt");
    string s1,s2;
    while(input>>s1>>s2){
        encode[s1]=s2;
        decode[s2]=s1;
    }
    input.close();
}

string cipher(string s){
    string out = "",temp="";
    for(int i = 0 ;i<s.size();i++){
        
        if(isalpha(s[i])){
            temp += s[i];
            if(encode.find(temp)!=encode.end()){
                out+=encode[temp];
                temp = "";
            }
        }
        else
            out+=s[i];
    }
    return out;
}

string decipher(string s){
    string out = "",temp="";
    for(int i = 0 ;i<s.size();i++){
        if(isalpha(s[i])){
            temp += s[i];
            if(decode.find(temp)!= decode.end()){
                out+=decode[temp];
                temp = "";
            }
        }
        else
            out+=s[i];
    }

    return out;
}

int main(){

    createDic();
    string s = "hello world i am rafi";
    string enc = cipher(s);
    cout<<enc<<endl;
    string dec = decipher(enc);
    cout<<dec<<endl;
    return 0;
    
}