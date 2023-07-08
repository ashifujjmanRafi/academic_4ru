import java.math.BigInteger;
import java.util.Random;

public class deffiehellman{
    public static void main(String[] args) {
        BigInteger P, G, a, b, x, y, Ka, Kb;

        P = BigInteger.valueOf(353);
        G = BigInteger.valueOf(3);
        System.out.println(P+" "+G);

        System.out.println("\nP = "+P+" G = "+G);
        
        //define private key a,  b
        a = BigInteger.valueOf(123);
        b = BigInteger.valueOf(234);
        System.out.println("\nPrivate Key a = "+a+",  b = "+b);
        // key generate
        x = G.modPow(a, P);
        y = G.modPow(b, P);

        System.out.println("\nGenerated Key x = "+x+",  y = "+y);

        //generate secrete key
        Ka = y.modPow(a, P);
        Kb = x.modPow(b, P);

        System.out.println("\nPrivate Key Ka = "+Ka+",  Kb = "+Kb);
        System.out.println();
    }
}