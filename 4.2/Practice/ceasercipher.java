
string cipher(string s,int key){
    string out = "";
    for(int i =0 ;i<s.size();i++){
        if(isupper(s[i])){
            int temp = (s[i]-'A'+key)%26;
            out += temp+'A';
        }
        else if(islower(s[i])){
            int temp = (s[i]-'a'+key)%26;
            out += temp + 'a';
        }
        else 
            out+=s[i];
    }
    return out;
}

string decipher(string s, int key){
    string out = "";
    for(int i =0 ;i<s.size();i++){
        if(isupper(s[i])){
            int temp = (s[i]-'A'-key+26)%26;
            out += temp+'A';
        }
        else if(islower(s[i])){
            int temp = (s[i]-'a'-key+26)%26;
            out += temp + 'a';
        }
        else 
            out+=s[i];
    }
    return out;

}


int main(){
    ifstream input;
    input.open("cin.txt");
    string s;
    int key=3;
    while(getline(input,s)){

        cout<<"cipher text is : ";
        string enc = cipher(s,key);
        cout<<enc<<endl;
        string dec = decipher(enc,key);
        cout<<"normal text is : ";
        cout<<dec<<endl;

        cout<<endl;
    }
    return 0;
}