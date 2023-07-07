public class Demo {
    public static void main(String[] args) {
        String pad = "1234567890";
        oneTimePad otp = new oneTimePad(pad);
        String enc = otp.encryption("Hello World!");
        System.out.println(enc);
        String dec = otp.decryption(enc);
        System.out.println(dec);
    }
}