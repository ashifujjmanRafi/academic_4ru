import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class MD5{
    public static void main(String[] args){
        String input = "i am rafi";
        System.out.println("Input: " + input);
        String Hash = computeHash(input);
        System.out.println("Hash: " + Hash);
    }

    public static String computeHash(String input) {

        try{
            MessageDigest md = MessageDigest.getInstance("MD5");
            md.update(input.getBytes());
            byte[] digest = md.digest();
            StringBuffer sb = new StringBuffer();
            for (byte b : digest) {
                sb.append(String.format("%02x", b & 0xff));
            }
            return sb.toString();
        }catch(NoSuchAlgorithmException e){
            throw new RuntimeException(e);
        }
        
    }
}