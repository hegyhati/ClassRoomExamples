import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.NoSuchElementException;
import java.util.Scanner;

public class PrePayedPlan extends Plan{
    private String name;
    private double minuteCost;
    private double smsCost;

    public PrePayedPlan(String name, double minuteCost, double smsCost){
      super(name);
      this.minuteCost=minuteCost;
      this.smsCost=smsCost;
    }

    public PrePayedPlan(double minuteCost, double smsCost){
      this("Custom PrePayed Plan", minuteCost, smsCost);
    }

    protected PrePayedPlan (Scanner sc) throws NoSuchElementException {
      this(sc.next(), sc.nextDouble(), sc.nextDouble());
    }

    @Override
    public double getCost(PhoneUsage usage){
      return usage.getCallDuration().inMinutes() * minuteCost + usage.getSMSCount()* smsCost;
    }

    public static List<Plan> loadPlansFromFile(String filePath){
      ArrayList<Plan> plans = new ArrayList<Plan>();
      try{
        Scanner sc = new Scanner(new File(filePath));
        try {
          while(sc.hasNextLine())
            plans.add(new PrePayedPlan(sc));
        } catch (NoSuchElementException e) {
          System.err.println("Plan data file corrupt, " + plans.size() + " plans were parsed successfully.");
        } finally {
          sc.close();
        }
      } catch (FileNotFoundException e) {
        System.err.println("Plan data file not found.");
      }  
      return plans;
    }
}
