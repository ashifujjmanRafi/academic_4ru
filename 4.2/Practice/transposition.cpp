#include <bits/stdc++.h>
using namespace std;

string cipher(string s, int col){
    string out = "";
    for(int i=0;i<col;i++){
        for(int j=i;j<s.size();){
            out += s[j];
            j += col;
        }     
    }
    return out;
}

string decipher(string s, int col){
    string out = "";
    int row = s.size()/col;
    int temp = s.size()%col;
    if(temp)
        row++;  
    for(int i = 0 ;i<row;i++){
        int cnt = temp;
        if(cnt){
            for(int j = i;j<s.size();){
                out+=s[j];
                if(cnt){
                    j+= row;
                    cnt--;
                }
                else
                    j+= row-1;
            }
        }
        else{
            for(int j = i;j<s.size();){
                out+= s[j];
                j+=row;
            }
        }
    }
    return out;
}

string transposition(string s,int col){
    return cipher(cipher(s,col),col);
}
string reverseTransposition(string s,int col){
    return decipher(decipher(s,col),col);
}

int main(){
    string s = "DEPERTMENT OF COMPUTER SCIENCE AND ENGINEERING";
    int col;
    cin>>col;
    string enc = transposition(s,col);
    cout<<enc<<endl;
    string dec = reverseTransposition(enc,col);
    cout<<dec<<endl;
    return 0;
}