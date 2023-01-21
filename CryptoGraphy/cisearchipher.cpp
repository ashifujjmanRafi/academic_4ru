#include <bits/stdc++.h>
using namespace std;

string encrypted(string text,int s){

    string result = "";
    for (int i = 0; i < text.length(); i++) {
        if (isupper(text[i]))
            result += char(int(text[i] + s - 65) % 26 + 65);
        else if(islower(text[i]))
            result += char(int(text[i] + s - 97) % 26 + 97);
        else
            result += text[i];
    }
   return result;
}

void decrypted(string text,int s){
    string result = "";

    for (int i = 0; i < text.length(); i++) {
        if (isupper(text[i]))
            result += char(int(text[i] - s - 65+26) % 26 + 65);
            
        else if(islower(text[i]))
            result += char(int(text[i] -s - 97+26) % 26 + 97);
        else
            result += text[i];
    }
    cout<<"Decrypted msg is :"<<result<<endl;
}

int main(){
    string text = "abxc zys";
    int s = 4;
    cout<<"NORMAL TEXT IS :"<<text<<endl;
    string e_msg = encrypted(text,s);
    cout<<"Cipher TEXT IS :"<<e_msg<<endl;
    decrypted(e_msg,s);
    
    return 0;
    

}