#include<bits/stdc++.h>
using namespace std;

string cipher(string s,string key){
    int head = 0;
    string enc = "";
    for(int i = 0;i<s.size();i++){
        int temp = 0;
        if(isupper(s[i])){
            temp = (s[i]-'A' + key[i]-'A')%26;
            enc += temp+'A';
        }
        else if(islower(s[i])){
            temp = (s[i]-'a' + key[i]-'A')%26;
            enc += temp + 'a';
        }
        else 
            enc += s[i];

        // head = (head+1)%key.size();
    }
    return enc;
}

string decipher(string s,string key){
    int tail = 0;
    string dec = "";
    for(int i = 0;i<s.size();i++){
        int temp = 0;
        if(isupper(s[i])){
            temp = (s[i]-'A'- key[i] +'A'+26)%26;
            dec += temp+'A';
        }
        else if(islower(s[i])){
            temp = (s[i]-'a' - key[i]+'A'+26)%26;
            dec += temp+'a';
        }
        else 
            dec += s[i];
        //tail = (tail+1)%key.size();
    }
    return dec;
}


int main(){
    ifstream input;
    input.open("pad.txt");
    
    string key;
    string text = "DEPT COMPUTER SCIENCE AND ENGINEERING";
    getline(input,key);
    
    string enc = cipher(text,key);
    cout<<enc<<endl;
    string dec = decipher(enc,key);
    cout<<dec<<endl;

}