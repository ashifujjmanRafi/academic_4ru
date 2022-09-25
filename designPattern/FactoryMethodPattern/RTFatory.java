public class RTFatory extends Factory{

    @Override
    public Notification createNotification(String type) {
        
        if(type.equalsIgnoreCase("Sms")){
            return new RTSms();
        }
        else if(type.equalsIgnoreCase("Email")){
            return new RTEmail();
        }
        else
            return null;
    }

    
}
