public abstract class AbstractLogger{
    public static int info = 1;
    public static int debug = 2;
    public static int error = 3;

    protected int level;

    protected AbstractLogger nextlogger;
    public void setNextlogger(AbstractLogger nexLogger){
        this.nextlogger = nexLogger;
    }
    public void logMessage(int level,String message){
        if(this.level<=level){
            write(message);
        }
        if(nextlogger !=null){
            nextlogger.logMessage(level, message);
         }

    }
    abstract protected void write(String message);
}