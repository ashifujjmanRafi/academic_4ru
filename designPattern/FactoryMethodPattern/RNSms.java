// package designPattern.FactoryMethodPattern;

public class RNSms implements Notification {

    @Override
    public void notifyUser(String msg) {
        System.out.println("RunTime SMS Notification: " + msg);
    }

}
    
