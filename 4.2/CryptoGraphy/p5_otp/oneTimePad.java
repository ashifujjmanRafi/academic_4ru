import java.util.*;
public class oneTimePad{
    int head,tail;
    String pad;
    public oneTimePad(String pad){
        this.pad = pad;
        head=tail = 0;
    }
    public String encryption(String data){
        String result = "";
        for(int i = 0;i<data.length();i++){
            int tex = (int)data.charAt(i);
            int key = (int)pad.charAt(head);
            int cipher = (tex+key)%256;
            result += (char)cipher;
            head = (head+1)%pad.length();
        }
        return result;
    }
    public String decryption(String data){
        String result = "";
        for(int i = 0;i<data.length();i++){
            int tex = (int)data.charAt(i);
            int key = (int)pad.charAt(tail);
            int cipher = (tex-key+256)%256;
            result += (char)cipher;
            tail = (tail+1)%pad.length();
        }
        return result;
    }

    public static void main(String[] args){
        oneTimePad otp = new oneTimePad("1234567890");
        String enc = otp.encryption("hello world hello world quote hell");
        System.out.println(enc);
        String dec = otp.decryption(enc);
        System.out.println(dec);

    } 


}