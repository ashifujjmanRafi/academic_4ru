
public class FactoryProducer {
    
    public static Factory createfFactory(String info) {

        if(info.equalsIgnoreCase("RealTime")){
            return new RTFatory();
        }
        else if(info.equalsIgnoreCase("RunTime")){
            return new RNFactory();
        }
        else {
            return null;
        }
    }
}
