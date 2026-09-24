import java.util.ArrayList;
import java.util.function.BiPredicate;

public class RunCollection {
    private final ArrayList<Run>  _runs = new ArrayList<>();

    public void addRun(Run run) { _runs.add(run); }
    
    public double getTotalDistanceInKm(){
        double total = 0;
        for (Run run: _runs){ total += run.getDistanceInKm(); }
        return total;
    }

    private Run getBest(BiPredicate<Run, Run> isBetter) {
        if (_runs.isEmpty()) return null;
        Run longest = _runs.get(0);
        for (Run run : _runs) 
            if (isBetter.test(run,longest))
                longest = run;
        return longest;
    }

    public Run getLongestRun() { return getBest(Run::isLongerThan); }
    public Run getFastestRun() { return getBest(Run::isFasterThan); }

}