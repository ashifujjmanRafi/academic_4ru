// package designPattern.FactoryMethodPattern;

public class RNEmail implements Notification {

    @Override
    public void notifyUser(String msg) {
        System.out.println("RunTime Email Notification: " + msg);
    }

}
