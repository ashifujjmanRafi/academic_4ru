#include <bits/stdc++.h>
using namespace std;

map<string,string> encoder,decoder;

void createDictionary(){
    ifstream input;
    input.open("dictionary.txt");
    string s1,s2;
    while(input>>s1>>s2){
        encoder[s1]=s2;
        decoder[s2]=s1;
    }
    input.close();
}

string cipher(string s){
    string enc="",temp ="";
    for(int i = 0;i<s.size();i++){
        if(isalpha(s[i])){
            temp+=s[i];
            if(encoder.find(temp)!=encoder.end()){
                enc+=encoder[temp];
                temp = "";
            }
            
        }
        else
            enc += s[i];
    }
    return enc;
}

string decipher(string s){
    string dec="",temp="";
    for(int i = 0;i<s.size();i++){
        if(isalpha(s[i])){
            temp+=s[i];
            if(decoder.find(temp)!=decoder.end()){
                dec += decoder[temp];
                temp = "";
            }
        }
        else
            dec += s[i];
        
    }
    return dec;
}

int main(){
    ifstream input;
    input.open("input.txt");
    ofstream output;
    output.open("output.txt");
    createDictionary();
    string str,enc,dec;
    while(getline(input,str)){
        enc = cipher(str);
        output<<enc<<endl;
        dec = decipher(enc);
        output<<dec<<endl;
    }
    
    return 0;
}