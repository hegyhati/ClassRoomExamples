import java.util.ArrayList;
import java.util.Scanner;

class Bid {
    public final String name;
    public final int price;
    public Bid(String name, int price){
        this.name=name;
        this.price=price;
    }
}

class Product {
    public final String name;
    public final String description;
    public Product(String name, String description){
        this.name=name;
        this.description=description;
    }
    public Product(Product another){
        this.name=another.name;
        this.description=another.description;
    }
}

class Bidding {
    private final Product product;

    private final int startPrice;
    private final int minimalPrice;
    private final int minPriceIncrease;

    private ArrayList<Bid> bids = new ArrayList<Bid>();

    private boolean open = true;

    public Bidding(Product product, int startPrice, int minimalPrice, int minPriceIncrease){
        this.product=new Product(product);
        this.startPrice = startPrice;
        this.minimalPrice = minimalPrice;
        this.minPriceIncrease = minPriceIncrease;
    }
    public boolean bid(String bidderName, int bidPrice){
        if(open && ( 
            bids.isEmpty() && bidPrice >= startPrice
            ||
            !bids.isEmpty() && bidPrice >= bids.get(0).price + minPriceIncrease
            )
        ){
            bids.add(0, new Bid(bidderName, bidPrice));
            return true;
        } else return false;
    }
    public void close(){
        open=false;
    }
    public boolean wasSuccessful(){
        return !open && !bids.isEmpty() && bids.get(0).price >= minimalPrice;
    }
    public Bid getWinner(){
        if(wasSuccessful()) return bids.get(0);
        else return null;
    }
    public String toString(){
        StringBuilder toReturn = new StringBuilder("");
        toReturn.append("Product: " + product.name + "\n");
        toReturn.append("Description: " + product.description + "\n");
        if(open){
            toReturn.append("Bidding is active\n");
            if(bids.isEmpty()){
                toReturn.append("No bids yet, starting price is " + startPrice + " HUF\n");
            } else {
                toReturn.append("Last bid: "+bids.get(0).price + " HUF\n");
            }
            toReturn.append("Minimal increase is "+minPriceIncrease+" HUF\n");
        } else {
            toReturn.append("Bidding is closed\n");
            if(wasSuccessful()) toReturn.append("Bid was successful.\n");
            else toReturn.append("Bid was not successful.\n");
            toReturn.append("Bids: \n");
            for(Bid bid: bids){
                toReturn.append(" - "+bid.price+" HUF by "+bid.name+"\n");
            }
        }
        return toReturn.toString();
    }
}





public class BidSystem{
    public static void main(String[] args) {
        Product gloves = new Product("Winter gloves", "These are the most awesome cozy winter warm gloves for your hand. Buy now, dont miss it!!!!!111!!!!");
        
        Bidding bidding = new Bidding(gloves,200,2500,150);
        System.out.println(bidding);
        
        Scanner sc = new Scanner(System.in);
        System.out.println("Any new bid?");
        String response=sc.next();

        while(response.matches("[yY]es")){
            System.out.println(bidding);
            System.out.print("New bidder name: ");
            String bidder = sc.next();
            System.out.print("New bid: ");
            int bid = sc.nextInt();
            if (bidding.bid(bidder, bid)){
                System.out.println("Bid successful.");
            } else {
                System.out.println("Bidding failed.");
            }
            System.out.println("Any new bid?");
            response=sc.next();
        }
        bidding.close();
        System.out.println(bidding);
    }
}
