public class RTSms implements Notification {

    @Override
    public void notifyUser(String msg) {
        System.out.println("RealTime SMS Notification: " + msg);
    }

}