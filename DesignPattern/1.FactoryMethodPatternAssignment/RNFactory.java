// package designPattern.FactoryMethodPattern;


public class RNFactory extends Factory{
    @Override

    public Notification createNotification(String type) {
        if(type.equalsIgnoreCase("Sms")){
            return new RNSms();
        }
        else if(type.equalsIgnoreCase("Email")){
            return new RNEmail();
        }
        else
            return null;
    }
    
}
