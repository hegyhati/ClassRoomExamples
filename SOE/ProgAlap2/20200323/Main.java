import java.util.ArrayList;

class Ember {
    String nev;
    int szuldatum;
}

class EgyetemiPolgar extends Ember{
    String neptun;
}

class Hallgato extends EgyetemiPolgar{
    String szak;
    int kezdeseve;
}

final class Oktato extends EgyetemiPolgar{
    String tanszek;
    String beosztas;
}

class BuszSofor extends Ember{
    String volan;
    String kepesites;
}

class A {
    private int a;
    A(int a){this.a=a;}
    int getA(){return a;}
    void print() {System.out.println(a);}
}

class B extends A {
    int b;
    B (int a, int b){super(a);this.b=b;}
    void print() {System.out.println(getA()+"," + b);}
}

class Teglalap{
    double a;
    double b;
    Teglalap(double a, double b){this.a=a;this.b=b;}
    double getTerulet(){return a*b;}
    double getKerulet(){return 2*(a+b);}
}

class Negyzet extends Teglalap {
    Negyzet(double a){super(a,a);}
}

public class Main{
    public static void main(String[] args) {
        A pelda = new A(3);
        B pelda2 = new B(4,5);
        ArrayList<A> lista = new ArrayList<A>();
        lista.add(pelda);
        lista.add(pelda2);
        for(A elem:lista){
            elem.print();
        }

        Teglalap negyzet1=new Negyzet(2);

    }
}
