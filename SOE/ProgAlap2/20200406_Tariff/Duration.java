public class Duration{
  private int seconds;

  public Duration(){seconds=0;}
  public Duration(String duration){
    seconds  = Integer.parseInt(duration.substring(0, 2)) * 3600 +
               Integer.parseInt(duration.substring(3, 5)) * 60 +
               Integer.parseInt(duration.substring(6, 8));   
  }
  public double inMinutes(){return seconds/60.0;}
  public Duration add(Duration other){
    seconds+=other.seconds;
    return this;
  }  
  public String toString(){
    return ""
      + seconds/3600 + " hours "
      + (seconds%3600)/60 + " minutes "
      + seconds%60 + " seconds";
  }
}
