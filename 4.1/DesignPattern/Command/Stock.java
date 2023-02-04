public class Stock {

    private String name = "r";
    private int quantity = 10;


    public void buy(){
        System.out.println("Stock [name: "+name+", Quantity :"+ quantity+ "] bought");

    }
    public void sell(){
        System.out.println("Stock [name: "+name+", Quantity :"+ quantity+ "] SOLD");
    }
    
}
