public class RTEmail implements Notification {

    @Override
    public void notifyUser(String msg) {
        System.out.println("RealTime Email Notification: " + msg);
    }

}
