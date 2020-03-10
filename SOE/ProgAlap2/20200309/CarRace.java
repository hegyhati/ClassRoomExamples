import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

class Vector{
    public int x;
    public int y;
    public Vector(int x, int y){
        this.x=x;
        this.y=y;
    }
    public void add(Vector other){
        x+=other.x;
        y+=other.y;
    }
    public String toString(){
        return "("+x+","+y+")";
    }
    public boolean equals(Vector other){
        return x==other.x && y==other.y;
    }
}

class Car {
    public final String symbol;
    private Vector position;
    private Vector velocity = new Vector(0,0);

    public Vector getPosition(){return position;}

    public Car (int posX, int posY){
        this.position=new Vector(posX,posY);
        this.symbol="<>";
    }

    public Car (int posX, int posY, String symbol){
        this.position=new Vector(posX,posY);
        this.symbol=(symbol+"<>").substring(0,2);
    }

    private static int normalize(int n){
        if (n<-1) return -1;
        else if (n>1) return 1;
        else return n;
    }
    private static Vector normalize(Vector acceleration){
        return new Vector(normalize(acceleration.x),normalize(acceleration.y));
    }
    public void moveWithAcceleration(Vector acceleration){
        velocity.add(normalize(acceleration));
        position.add(velocity);
    }
    public String toString(){
        return "Position: "+position+", Velocity: "+velocity;
    }
}
class Track {
    public static final String emptySymbol = "..";
    public static final String finishSymbol = "##";
    public static final String borderSymbol = "==";
    public final int length;
    public final int width;
    public Track(int length, int width){
        this.length=length;
        this.width=width;
    }
    public void printState(List<Car> competitors){
        for(int x=0; x<=length; x++) {System.out.print(borderSymbol);} System.out.println();
        for(int y=width/2; y>=-width/2; y--){
            for(int x=0; x<length; x++){
                boolean occupied=false;
                for(Car car : competitors) 
                    if(car.getPosition().equals(new Vector(x,y))) {
                        System.out.print(car.symbol);
                        occupied=true;
                        break;
                    }
                if(!occupied) System.out.print(emptySymbol);
            }
            System.out.println(finishSymbol);
        }
        for(int x=0; x<=length; x++) {System.out.print(borderSymbol);} System.out.println();
    }
    public boolean onTrack(Car car){
        return car.getPosition().x >= 0 && Math.abs(car.getPosition().y)<=width/2;
    }
}


public class CarRace {
    private final Track track;
    private final List<Car> competitors;
    public static Scanner sc = null;

    public CarRace(Track track, List<Car> competitors){
        this.track=track;
        this.competitors=competitors;
    }

    public boolean isFinished(){
        for(Car car: competitors)
            if(track.onTrack(car) && car.getPosition().x >= track.length) return true;
        return false;
    }

    public static Vector inputAcceleration(Car car){
        System.out.print("Please provide acceleration for "+car.symbol+" //  "+car+":");
        Vector acceleration=new Vector(sc.nextInt(),sc.nextInt());
        return acceleration;
    }
    public void race(){
        while (!isFinished()) {
            track.printState(competitors);
            for(Car car: competitors)
                if(track.onTrack(car)) car.moveWithAcceleration(inputAcceleration(car));
        }
    }



    public static void main(String[] args) {
        CarRace.sc=new Scanner(System.in);
        CarRace race = new CarRace(new Track(50,21),List.of(new Car(2,2),new Car(0,0,"O>")));
        race.race();
        CarRace.sc.close();
    }
}
