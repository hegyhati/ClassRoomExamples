import java.io.File;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.NoSuchElementException;
import java.io.FileNotFoundException;

public abstract class Plan{
  private String name;

  protected Plan(String name){
    this.name=name;
  }
  public String getName(){return name;}

  public abstract double getCost(PhoneUsage usage);
}
