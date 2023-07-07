import java.io.File;
import java.util.*;
public class Demo{
    public static void main(String[] args) throws Exception{
        File file = new File("input.txt");
        Scanner sc = new Scanner(file);
        String input,tem;
        input = "";
        while(sc.hasNextLine()){
            tem = sc.nextLine();
            input = input+tem;
        }
        sc.close();
        System.out.println(input);
        cesercipher cc = new cesercipher(3,26);
        String enc = cc.encryption(input);
        System.out.println(enc);
        
        String dec = cc.decryption(enc);
        System.out.println(dec);
        }
}