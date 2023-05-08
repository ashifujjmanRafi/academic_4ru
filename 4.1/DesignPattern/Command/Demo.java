public class Demo {
    public static void main(String[] args) {
        Stock abStock = new Stock();

        BuyStock buystockorder = new BuyStock(abStock);
        SellStock sellstockorder = new SellStock(abStock);

        Broker broker = new Broker();
        broker.takeOrder(buystockorder);
        broker.takeOrder(sellstockorder);

        broker.placeOrders();


    }
}
