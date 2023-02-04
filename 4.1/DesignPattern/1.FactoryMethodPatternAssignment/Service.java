
public class Service {

    public static void main(String[] args) {
        //creating  two factory real and run time
        Factory r = FactoryProducer.createfFactory("RealTime");
        Factory run1 = FactoryProducer.createfFactory("RunTime");

        //creating notification for real time
        Notification n1 = r.createNotification("SMS");
        n1.notifyUser("gp offer");
        Notification n2 = r.createNotification("EMAIL");
        n2.notifyUser("Quora texted you");

        //creating notification for run time
        Notification n3 = run1.createNotification("Sms");
        n3.notifyUser("otp");
        Notification n4 = run1.createNotification("Email");
        n4.notifyUser("googole password");


    }

    
}
