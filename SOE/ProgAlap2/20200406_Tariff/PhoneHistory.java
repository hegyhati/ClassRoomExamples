import java.io.File;
import java.io.FileNotFoundException;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.LocalTime;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.NoSuchElementException;
import java.util.Scanner;


enum PhoneActionDirection {
  INCOMING, OUTGOING
}

class PhoneAction {
  private LocalDateTime time;
  private String otherNumber;
  private PhoneActionDirection direction;
  public PhoneAction(LocalDateTime time, String otherNumber, PhoneActionDirection direction){
    this.time=time;
    this.otherNumber=otherNumber;
    this.direction=direction;
  }
  public PhoneActionDirection getDirection(){return direction;}
}

class SMSAction extends PhoneAction {
  private int count;
  public SMSAction(LocalDateTime time, String otherNumber, PhoneActionDirection direction, int count){
    super(time, otherNumber, direction);
    this.count=count;
  }
  public int getCount(){return count;}
}

class CallAction extends PhoneAction {
  Duration duration;
  public CallAction(LocalDateTime time, String otherNumber, PhoneActionDirection direction, Duration duration){
    super(time, otherNumber, direction);
    this.duration=duration;
  }
  public Duration getDuration(){return duration;}
}

public class PhoneHistory implements PhoneUsage{
  
  ArrayList<PhoneAction> actions;

  public PhoneHistory(String fileName){
    actions = new ArrayList<PhoneAction>();
    try{
      Scanner sc = new Scanner(new File(fileName));
      try {
        while(sc.hasNextLine()){
          LocalDateTime time;
          String otherNumber;
          String directionString;
          PhoneActionDirection direction;
          String type;
          time=LocalDateTime.of(
            LocalDate.parse(sc.next(),DateTimeFormatter.ofPattern("yyyy.MM.dd")),
            LocalTime.parse(sc.next(),DateTimeFormatter.ofPattern("HH:mm:ss")));
          type=sc.next();
          directionString=sc.next();
          if(0==directionString.compareTo("IN")) direction=PhoneActionDirection.INCOMING;
          else if (0==directionString.compareTo("OUT")) direction=PhoneActionDirection.OUTGOING;
          else throw new NoSuchElementException("Incorrect Phone Action Direction");
          otherNumber=sc.next();
          if(0==type.compareTo("CALL")) {
            Duration duration=new Duration(sc.next());
            actions.add(new CallAction(time, otherNumber, direction, duration));
          } else if (0==type.compareTo("SMS")) {
            int count=sc.nextInt();
            actions.add(new SMSAction(time, otherNumber, direction, count));
          } else throw new NoSuchElementException("Incorrect Phone Action");
        }
      } catch (NoSuchElementException e) {
        System.err.println("Phone history file corrupt, " + actions.size() + " actions were parsed successfully.");
      } finally {
        sc.close();
      }
    } catch (FileNotFoundException e) {
      System.err.println("History data file not found.");
    }  
  }
  
  @Override
  public int getSMSCount() {
    int totalOutCount = 0;
    for(PhoneAction action:actions){
      if(action.getDirection()==PhoneActionDirection.OUTGOING && action instanceof SMSAction) {
        totalOutCount+= ((SMSAction) action).getCount();
      }
    }
    return totalOutCount;
  }

  @Override
  public Duration getCallDuration() {
    Duration totalOutDuration = new Duration();
    for(PhoneAction action:actions){
      if(action.getDirection()==PhoneActionDirection.OUTGOING && action instanceof CallAction) {
        totalOutDuration.add(((CallAction) action).getDuration());
      }
    }
    return totalOutDuration;
  }
  
}
