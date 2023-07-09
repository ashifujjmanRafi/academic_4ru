import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

class MD5{
    public static void main(String[] args) throws NoSuchAlgorithmException{
        String in = "hello Md5";
        MessageDigest md = MessageDigest.getInstance("MD5");
        byte[] digest = md.digest(in.getBytes());
        StringBuilder sb = new StringBuilder();
        for(byte b :digest){
            sb.append(String.format("%02x",b));

        }
        String md5hash = sb.toString();
        System.out.println("Input: "+in);
        System.out.println("MD5 hash:"+md5hash);

    }
}