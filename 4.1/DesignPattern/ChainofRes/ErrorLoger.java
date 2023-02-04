public class ErrorLoger extends AbstractLogger {

    public ErrorLoger(int level){
        this.level = level;
    }

    @Override
    protected void write(String message){
        System.out.println("Error console message" +message);
    }
    
}
