import java.math.BigInteger;
import java.util.Random;

class keyExchange{

    public static void main(String[] args){
        BigInteger p,alpha,xa,xb,ya,yb,ka,kb;

        p = BigInteger.valueOf(353);
        alpha = BigInteger.valueOf(3);

        xa = BigInteger.valueOf(123);
        xb = BigInteger.valueOf(324);

        ya = alpha.modPow(xa,p);
        yb = alpha.modPow(xb,p);

        ka = yb.modPow(xa,p);
        kb = ya.modPow(xb,p);

        System.out.println("ka "+ka+"=="+" kb "+kb);
    }

}