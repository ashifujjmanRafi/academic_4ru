import java.math.BigInteger;
import java.util.Random;

class lprime{
    public static boolean isPrime(BigInteger n,int it){

        if(n.compareTo(BigInteger.ZERO)<=0)
            return false;
        if(n.equals(BigInteger.TWO))
            return true;
        if(n.mod(BigInteger.TWO).equals(BigInteger.ZERO))
            return false;
        Random random = new Random();

        for(int i = 0;i<it;i++){
            BigInteger a = new BigInteger(n.bitLength(),random).mod(n.subtract(BigInteger.TWO)).add(BigInteger.TWO);
            BigInteger power = a.modPow(n.subtract(BigInteger.ONE).divide(BigInteger.TWO),n);
            if(!power.equals(BigInteger.ONE) && ! power.equals(n.subtract(BigInteger.ONE)))
                return false;
        }
        return true;
    }

    public static void main(String[] args){
        BigInteger n = new BigInteger("19");
        int iteration = 10;
        System.out.println(n+" is prime "+isPrime(n,iteration));
    }
}