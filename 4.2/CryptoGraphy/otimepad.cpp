#include <bits/stdc++.h>
using namespace std;
string Encrypt(string text, string key)
{
    freopen("chipher.txt", "w", stdout);
    freopen("input.txt", "r", stdin);

    string cipherText = "";

    int cipher[key.length()];

    for (int i = 0; i < key.length(); i++)
    {
        cipher[i] = text.at(i) - 'A' + key.at(i) - 'A';
    }

    for (int i = 0; i < key.length(); i++)
    {
        if (cipher[i] > 25)
        {
            cipher[i] = cipher[i] - 26;
        }
    }

    for (int i = 0; i < key.length(); i++)
    {
        int x = cipher[i] + 'A';
        cipherText += (char)x;
    }
    cout << cipherText << endl;
    return cipherText;
}
void Decrypt(string text, string key)
{
    freopen("chipher.txt", "r", stdin);
    freopen("output.txt", "r", stdout);
    string plainText = "";

    int plain[key.length()];

    for (int i = 0; i < key.length(); i++)
    {
        plain[i] = text.at(i) - 'A' - (key.at(i) - 'A');
    }

    for (int i = 0; i < key.length(); i++)
    {
        if (plain[i] < 0)
        {
            plain[i] = plain[i] + 26;
        }
    }

    for (int i = 0; i < key.length(); i++)
    {
        int x = plain[i] + 'A';
        plainText += (char)x;
    }

    cout << plainText << endl;
}
int main()
{

    string plainText = "Hello";
    string key = "MONEY";
    for (int i = 0; i < plainText.length(); i++)
    {
        plainText[i] = toupper(plainText[i]);
    }
    for (int i = 0; i < key.length(); i++)
    {
        key[i] = toupper(key[i]);
    }

    Encrypt(plainText, key);
    Decrypt(Encrypt(plainText, key), key);
    return 0;
}