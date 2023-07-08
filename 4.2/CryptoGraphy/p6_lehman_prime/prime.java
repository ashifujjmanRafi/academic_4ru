import java.math.BigInteger;
import java.util.Random;

public class prime {

    public static boolean isPrime(BigInteger n, int iterations) {
        if (n.compareTo(BigInteger.ONE) <= 0) {
            return false;
        }
        if (n.equals(BigInteger.TWO)) {
            return true;
        }
        if (n.mod(BigInteger.TWO).equals(BigInteger.ZERO)) {
            return false;
        }

        Random random = new Random();
        for (int i = 0; i < iterations; i++) {
            // a = random int such that 2 <= a <= n-2
            BigInteger a = new BigInteger(n.bitLength(), random).mod(n.subtract(BigInteger.TWO)).add(BigInteger.TWO);
            // a^(n-1)/2 (mod n)
            BigInteger power = a.modPow(n.subtract(BigInteger.ONE).divide(BigInteger.TWO), n);
            // n is not prime if power != 1 (mod n) or power != -1 (mod n)
            if (!power.equals(BigInteger.ONE) && !power.equals(n.subtract(BigInteger.ONE))) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        
        BigInteger n = new BigInteger("13");
        int iterations = 10;
        boolean isPrime = isPrime(n, iterations);
        System.out.println(n + " is prime: " + isPrime);
    }
}
