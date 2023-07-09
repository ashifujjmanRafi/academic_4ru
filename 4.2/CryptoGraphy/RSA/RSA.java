import java.math.BigInteger;
import java.security.SecureRandom;

public class RSA {
    
    private BigInteger modulus;
    private BigInteger publicKey;
    private BigInteger privateKey;
    private int bitLength = 1024; 
    // length of the key in bits
    
    public RSA() {
        // generate random prime numbers
        SecureRandom random = new SecureRandom();
        BigInteger p = new BigInteger(bitLength/2, 100, random);
        BigInteger q = new BigInteger(bitLength/2, 100, random);
        System.out.println("p: " + p);
        System.out.println("q: " + q);

        // compute modulus and totient
        modulus = p.multiply(q);
        BigInteger phi = (p.subtract(BigInteger.ONE)).multiply(q.subtract(BigInteger.ONE));
        
        // compute public key
        publicKey = new BigInteger("65537"); // commonly used public exponent
        while (phi.gcd(publicKey).intValue() > 1) {
            publicKey = publicKey.add(new BigInteger("1"));
        }
        System.out.println("Public key: " + publicKey);
        
        // compute private key
        privateKey = publicKey.modInverse(phi);
    }
    
    public byte[] encrypt(byte[] message) {
        return (new BigInteger(message)).modPow(publicKey, modulus).toByteArray();
    }
    
    public byte[] decrypt(byte[] message) {
        return (new BigInteger(message)).modPow(privateKey, modulus).toByteArray();
    }
    
    public static void main(String[] args) {
        RSA rsa = new RSA();
        String originalMessage = "Hello, i am rafi!";
        byte[] encryptedMessage = rsa.encrypt(originalMessage.getBytes());
        byte[] decryptedMessage = rsa.decrypt(encryptedMessage);
        System.out.println("Original message: " + originalMessage);
        System.out.println("Encrypted message: " + new String(encryptedMessage));
        System.out.println("Decrypted message: " + new String(decryptedMessage));
    }
}
