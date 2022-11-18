public  class SingleObj {

    private  static  SingleObj instance = new SingleObj();

    private SingleObj(){};

    public  static  SingleObj getInstance(){
        return  instance;
    }
    public void showmes(){
        System.out.println("only one instance");
    }
}