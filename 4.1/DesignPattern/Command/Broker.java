import java.util.*;
public class Broker {
    private List<Order> orders = new ArrayList<>();

    public void takeOrder(Order order){
        orders.add(order);
    }
    public void placeOrders(){
        for(Order order:orders){
            order.execute();
        }
        orders.clear();
    }
    
    
}
