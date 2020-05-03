import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.NoSuchElementException;
import java.util.Scanner;

public class PostPayedPlan extends PrePayedPlan{
  private double monthlyFee;

  public PostPayedPlan(String name, double monthlyFee, double minuteCost, double smsCost){
    super(name,minuteCost,smsCost);
    this.monthlyFee=monthlyFee;
  }

  public PostPayedPlan(double monthlyFee, double minuteCost, double smsCost){
    this("Custom PrePayed Plan", monthlyFee, minuteCost, smsCost);
  }

  protected  PostPayedPlan(Scanner sc) throws NoSuchElementException {
    this(sc.next(), sc.nextDouble(), sc.nextDouble(), sc.nextDouble());
  }

  @Override
  public double getCost(PhoneUsage usage){
    return Math.max(super.getCost(usage),monthlyFee);
  }  


  public static List<Plan> loadPlansFromFile(String filePath){
    ArrayList<Plan> plans = new ArrayList<Plan>();
    try{
      Scanner sc = new Scanner(new File(filePath));
      try {
        while(sc.hasNextLine())
          plans.add(new PostPayedPlan(sc));
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
