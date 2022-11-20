
public abstract class game {
    abstract void initialize();
    abstract void startplay();
    abstract void endplay();

    public final void play(){
        initialize();
        startplay();
        endplay();
    }
    
}
