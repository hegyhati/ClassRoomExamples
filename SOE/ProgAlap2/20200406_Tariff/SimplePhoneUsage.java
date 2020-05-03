public class SimplePhoneUsage implements PhoneUsage {
  private Duration callDuration;
  private int smsCount;

  public SimplePhoneUsage(Duration callDuration, int smsCount){
    this.callDuration=callDuration;
    this.smsCount=smsCount;
  }

  @Override
  public int getSMSCount(){return smsCount;}

  @Override
  public Duration getCallDuration(){return callDuration;}
}
