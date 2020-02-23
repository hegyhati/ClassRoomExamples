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
    Job[] jobs;
    int count;

    public Schedule(int jobcount){
        this.jobs=new Job[jobcount];
        this.count=0;
    }

    public boolean isFull(){return count==jobs.length;}

    public boolean accept(Job job) {
        if (isFull()) return false;
        for(int j=0; j<count; j++)
            if(jobs[j].overlaps(job)) return false;
        jobs[count++]=job;
        return true;
    }
    public void print(){
        System.out.println("Accepted jobs:");
        for(int j=0;j<count;j++)
            System.out.println("   - "+jobs[j]);
    }
}

public class JobManager{
    public static void main(String[] args) {
        Schedule sch=new Schedule(3);
        Scanner sc=new Scanner(System.in);
        while(!sch.isFull()){
            System.out.println("I can still do some stuff, give me the jobs name, startday, duration and payment.");
            Job tmpJob=new Job(sc.next(), sc.nextInt(), sc.nextInt(), sc.nextInt());
            if(sch.accept(tmpJob)) {
                System.out.println("Thanks, I'll take care of that.");
            } else {
                System.out.println("Sorry bro', conflicts with another accepted job.");
            }
        }
        System.out.println("Got my hands full:");
        sch.print();
    }
}
