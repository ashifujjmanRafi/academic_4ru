#include <bits/stdc++.h>
using namespace std;

string cipher(string s, int bs){
    string out = "";
    cout<<bs<<endl;
    for(int i=0;i<bs;i++){
        for(int j=i;j<s.size(); ){
            out += s[j];
            j+= bs;
        }
    }
    return out;

}

string decipher(string s,int bs){
    string out = "";
    int row = s.size()/bs;
    int temp = s.size()%bs;
    if(temp)
        row++;
    int total = 0;
    for(int i =0;i<row;i++){
        int cnt = temp;
        if(cnt){
            for(int j =i;j<s.size();){
                out+=s[j];
                if(cnt){
                    j+=row;
                    cnt--;
                }
                else
                    j+=row-1;
                total++;
                if(total==s.size())
                    break;
            }

        }

        else{
            for(int j = i;j<s.size(); ){
                out+= s[j];
                j+=row;
            }
        }

    }
    return out;

}

string transposition(string s,int ds){
    return cipher(cipher(s,ds),ds);
}
string reverseTransposition(string s,int ds){
    return decipher(decipher(s,ds),ds);
}

int main(){
    string text = "i am ashifujjman";
    int bs ;
    cin>>bs;
    string enc = transposition(text,bs);
    cout<<enc<<endl;
    string dec = reverseTransposition(enc,bs);
    cout<<dec<<endl;
    return 0;
}   