import java.util.Scanner;

import javax.swing.JOptionPane;

class Time {
    int seconds;
    
    public Time(int seconds){this.seconds=seconds;}
    public Time(int minutes, int seconds){this.seconds=minutes*60+seconds;}
    public Time(int hours, int minutes, int seconds){this.seconds=hours*3600+minutes*60+seconds;}

    public void increase(Time other){this.seconds+=other.seconds;}
    public Time add(Time other){return new Time(this.seconds+other.seconds);}

    public String toString(){
        int hours=this.seconds/3600;
        int minutes=(this.seconds/60)%60;
        int seconds=this.seconds%60;
        if (hours>0) return String.format("%d:%02d:%02d",hours,minutes, seconds);
        else return String.format("%d:%02d",minutes, seconds);
    }

    public int getSeconds(){return this.seconds;}
}

class Run {
    double distance; // meters
    Time duration;

    public Run(double distance, int seconds){
        this.distance=distance;
        this.duration=new Time(seconds);
    }
    public double speed(){
        return distance/duration.getSeconds();
    }
    public double speedInKmH(){
        return speed()*3.6;
    }
    public String toString(){
        return distance/1000 + " kilometers in "+duration+", with the average speed of "+speedInKmH()+" km/h";
    }
    public void print() {
        System.out.println(this);
    }
    public void showInMessageDialog() {
        JOptionPane.showMessageDialog(null, this, "Run statustics", JOptionPane.INFORMATION_MESSAGE);
    }
}


public class RunManager{

    public static void main(String[] args) {
        Run[] runs = new Run[3];
        Scanner sc=new Scanner(System.in);
        // Scanner sc=new Scanner(new File(args[1]))
        for (int i=0;i<3;i++){
            runs[i]= new Run(sc.nextDouble(),sc.nextInt());
        }
        sc.close();
        int minidx = 0;
        for(int i=0;i<runs.length;++i){
            if(runs[i].speed() < runs[minidx].speed())
                minidx = i;
        }
        System.out.println("The fastest run: ");
        runs[minidx].print();
        System.out.println(runs[minidx ]);
        runs[minidx].showInMessageDialog();

    }
}
