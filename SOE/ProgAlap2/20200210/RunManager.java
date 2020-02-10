class Run {
    float distance; // meters
    int duration; // seconds
}


public class RunManager{
    static float speed(Run run){
        return run.distance / run.duration;
    }
    static void print(Run run) {
        System.out.println(run.distance + " meters in "+run.duration+" seconds, with the average speed of "+speed(run)+"m/s");
    }

    public static void main(String[] args) {
        Run[] runs = new Run[3];
        runs[0]=new Run();
        runs[0].distance=12000;
        runs[0].duration=3600;
        runs[1]=new Run();
        runs[1].distance=5000;
        runs[1].duration=1500;
        runs[2]=new Run();
        runs[2].distance=10012;
        runs[2].duration=3114;
        int minidx = 0;
        for(int i=0;i<runs.length;++i){
            if(speed(runs[i]) < speed(runs[minidx]))
                minidx = i;
        }
        System.out.println("The fastest run: ");
        print(runs[minidx]);

    }
}
