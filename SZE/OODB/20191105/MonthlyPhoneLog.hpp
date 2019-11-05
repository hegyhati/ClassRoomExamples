#ifndef MPL_HPP
#define MPL_HPP

class MonthlyPhoneLog {
  public:
    const int seconds;
    const int smscount;
    MonthlyPhoneLog(int seconds, int smscount)
    :seconds(seconds), smscount(smscount) {}
};



#endif
