public class cesercipher{
    int key,modulo;
    public cesercipher(int key,int modulo){
        this.key = key;
        this.modulo = modulo;
    }
    public String encryption(String input){
        String enc = "";
        for(int i = 0;i<input.length();i++){
            char ch = input.charAt(i);
            if(ch>='a'&&ch<='z'){
                ch = (char)('a'+(ch-'a'+key)%modulo);
            }
            else if(ch>='A'&&ch<='Z'){
                ch = (char)('A'+(ch-'A'+key)%modulo);
            }

            enc = enc+ch;
        }
        return enc;
    }

    public String decryption (String input){
        String dec = "";
        for(int i = 0;i<input.length();i++){
            char ch = input.charAt(i);
            if(ch>='a'&&ch<='z'){
                ch = (char)('a'+(ch-'a'-key+modulo)%modulo);
            }
            else if(ch>='A'&&ch<='Z'){
                ch = (char)('A'+(ch-'A'-key+modulo)%modulo);
            }
            
            dec = dec+ch;

        }
        return dec;
    }

    public static void main(String[] args){
        cesercipher cc = new cesercipher(3,26);
        String enc = cc.encryption("hello world hello world quote hell");
        System.out.println(enc);
        String dec = cc.decryption(enc);
        System.out.println(dec);
    }
}