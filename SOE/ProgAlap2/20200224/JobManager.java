import java.security.KeyStore.Entry;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

class Job {
    String name;
    int startday;
    int duration;
    int payment;

    public Job(String name, int startday, int duration, int payment){
        this.name=name;
        this.startday=startday;
        this.duration=duration;
        this.payment=payment;
    }

    public boolean overlaps(Job other){
        return this.startday < other.startday+other.duration 
            && other.startday < this.startday+this.duration;
    }

    public String toString(){
        return name + " ["+this.startday+"-"+(this.startday+this.duration-1)+"] for $"+this.payment;
    }
}

class Schedule {
    ArrayList<Job> jobs;

    public Schedule(){
        jobs=new ArrayList<Job>();
    }

    public boolean accept(Job job) {
        for(Job acceptedjob: jobs)
            if(acceptedjob.overlaps(job)) return false;
        jobs.add(job);
        return true;
    }
    public String toString(){
        StringBuilder toReturn = new StringBuilder("Accepted jobs: \n");
        for(Job job: jobs)
            toReturn.append("   - " + job + "\n");
        return toReturn.toString();
    }
    public int totalPayment(){
        int sum=0;
        for(Job job: jobs)
            sum+=job.payment;
        return sum;
    }
}

class Manager{
    HashMap<String,Schedule> employees;
    
    public Manager(){
        employees = new HashMap<String,Schedule>();
    }
    public boolean register(String worker){
        if(employees.containsKey(worker)) return false;
        else {
            employees.put(worker, new Schedule());
            return true;
        }
    }
    public boolean accept(Job job){
        for(Map.Entry<String,Schedule> entry: employees.entrySet())
            if(entry.getValue().accept(job)) return true;
        return false;
    }
    public String toString(){
        StringBuilder toReturn = new StringBuilder("Workers:");
        for(Map.Entry<String,Schedule> entry: employees.entrySet())
            toReturn.append("\n *"+entry.getKey()+"*   ").append(entry.getValue());
        toReturn.append("\n");
        return toReturn.toString();
    }
    public int totalPayment(){
        int sum=0;
        for(Map.Entry<String,Schedule> entry: employees.entrySet())
            sum += entry.getValue().totalPayment();
        return sum;
    }

}

public class JobManager{
    public static void main(String[] args) {
        Manager manager = new Manager();
        Scanner sc=new Scanner(System.in);        
        
        do {
            System.out.print("Please enter the name of an employee: ");
            if(manager.register(sc.next())) {
                System.out.println("Got it, employee registered.");
            } else {
                System.out.println("Sorry, employee with the same name already exists.");
            }
            System.out.print("Want to add another employee? (YES/NO) ");
        } while (sc.next().equals("YES"));
        
        while(manager.totalPayment()<1000){
            System.out.print("I don't yet have enough money for the stuff I need, give me a job with its name, startday, duration and payment: ");
            Job tmpJob=new Job(sc.next(), sc.nextInt(), sc.nextInt(), sc.nextInt());
            if(manager.accept(tmpJob)) {
                System.out.println("Thanks, one of my employees will take care of that.");
            } else {
                System.out.println("Sorry bro', none of my employees can take that.");
            }
        }
        System.out.println("Got enough money!!!");
        System.out.println(manager);
    }
}
