import java.util.List;

public class Planner {
  static Plan getBestPlan(List<? extends Plan> plans, PhoneUsage usage){
    if(plans.isEmpty()) return null;
    Plan bestPlan=plans.get(0);
    for(Plan plan: plans) 
      if(plan.getCost(usage)<bestPlan.getCost(usage)) 
        bestPlan=plan;
    return bestPlan;
  }
  
}
