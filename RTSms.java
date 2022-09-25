//import designPattern.FactoryMethodPattern.Notification;

public class RTSms implements Notification {
    @Override
    public void notifyUser(String msg) {
        System.out.println("Sending Real Time SMS notification: " + msg);
    }
}
    
