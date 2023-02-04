
public class Demo {

    private static AbstractLogger getChain()
    {
        AbstractLogger error = new ErrorLoger(AbstractLogger.error);
        AbstractLogger file = new FileLogger(AbstractLogger.debug);
        AbstractLogger console = new ConsoleLogger(AbstractLogger.info);

        error.setNextlogger(file);
        file.setNextlogger(console);

        return error;
    }

    public static void main(String[] args) {
        
        AbstractLogger loggerchain = getChain();

        loggerchain.logMessage(AbstractLogger.info,"this is an information");

        loggerchain.logMessage(AbstractLogger.error,"  + error message");

    }


    
}
