import java.util.ArrayList;
import java.util.Collection;
import java.util.Scanner;



interface Drawable{
    boolean covers(double x, double y);
}

interface Boxable {
    double getMinX();
    double getMaxX();
    double getMinY();
    double getMaxY();
}


class Point implements Boxable{
    public double x;
    public double y;
    public Point(double x, double y){this.x=x;this.y=y;}
    public double getMinX(){return x;}
    public double getMaxX(){return x;}
    public double getMinY(){return y;}
    public double getMaxY(){return y;}
}

class Circle implements Drawable, Boxable{
    private Point center;
    private double radius;
    public Circle(double x, double y, double r){
        center = new Point(x,y);
        radius=r;
    }

    @Override
    public boolean covers(double x, double y) {
        return (center.x-x)*(center.x-x)+(center.y-y)*(center.y-y)<radius*radius;
    }
    public double getMinX(){return center.x-radius;}
    public double getMaxX(){return center.x+radius;}
    public double getMinY(){return center.y-radius;}
    public double getMaxY(){return center.y+radius;}
}
class Rectangle implements Drawable{
    private Point topleft;
    private Point bottomright;
    public Rectangle(double x1, double y1, double x2, double y2){
        topleft=new Point(Math.min(x1,x2),Math.max(y1,y2));
        bottomright= new Point(Math.max(x1,x2),Math.min(y1,y2));
    }

    @Override
    public boolean covers(double x, double y) {
        return x >= topleft.x && x <= bottomright.x && y >= bottomright.y && y <= topleft.y;
    }
    public double getMinX(){return topleft.x;}
    public double getMaxX(){return bottomright.x;}
    public double getMinY(){return bottomright.y;}
    public double getMaxY(){return topleft.y;}    
}



interface Renderer{
    void render(Collection<? extends Drawable> drawables);
}

class CharacterRenderer implements Renderer{
    private Rectangle view=new Rectangle(-10,-10,10,10);
    private double resolution=1;
    public static final String covered4="██";
    public static final String covered3="▓▓";
    public static final String covered2="▒▒";
    public static final String covered1="░░";
    public static final String notcovered="--";

    CharacterRenderer setView(double topleftX, double topleftY, double bottomrightX, double bottomrightY){
        view=new Rectangle(topleftX,topleftY,bottomrightX,bottomrightY);
        return this;
    }
    CharacterRenderer setResolution(double resolution){
        this.resolution=resolution;
        return this;
    }
    private String getCoverString(int covercount){
        switch(covercount){
            case 0: return notcovered;
            case 1: return covered1;
            case 2: return covered2;
            case 3: return covered3;
            default: return covered4;
        }
    }

    @Override
    public void render(Collection<? extends Drawable> shapes) {
        // For efficiency, the collection could be filtered if :
        //  - the drawable extends (use instanceof) Boxable
        //  - and the box is outside of the view
        // => only render those shapes that are within the view
        for(double y=view.getMaxY(); y > view.getMinY(); y-=resolution){
            for(double x=view.getMinX(); x<view.getMaxX(); x+=resolution){
                int covercount=0;
                for(Drawable shape : shapes){
                    if (shape.covers(x+resolution/2,y-resolution/2)) covercount++;
                }
                System.out.print(getCoverString(covercount));
            }
            System.out.println();
        }
    }
    private void Zoom(double scale){
        double dx=view.getMaxX()-view.getMinX();
        double dy=view.getMaxX()-view.getMinX();
        setView(view.getMinX()-(1-scale)*dx, view.getMinY()-(1-scale)*dy, view.getMaxX()+(1-scale)*dx, view.getMaxY()+(1-scale)*dy);
    }
    public void ZoomIn(){Zoom(1.8);}
    public void ZoomOut(){Zoom(0.6);} // TODO fix numbers so zoomin negates zoomout
    public void Enhance(){resolution*=0.75;}
}

public class Main{
    static void interactive(Collection<? extends Drawable> shapes){
        String command = new String();
        Scanner sc = new Scanner(System.in);
        CharacterRenderer r=new CharacterRenderer();
        do {
            if (command.equals("ZoomIn")) {r.ZoomIn();}
            else if (command.equals("ZoomOut")) {r.ZoomOut();}
            else if (command.equals("Enhance")) {r.Enhance();}
            // add other operations such as moving the camera
            r.render(shapes);
            command=sc.next();
        } while (!command.equals("exit"));
        System.out.println("Bye bye.");
        sc.close();
    }

    public static void main(String[] args) {
        ArrayList<Drawable> shapes = new ArrayList<Drawable>();
        shapes.add(new Circle(0,0,6)); // origoban sugara 3
        shapes.add(new Circle(3,3,4));
        shapes.add(new Rectangle(-8,4,4,-6)); // egyik x egyik y masik x masik y
        //...
        interactive(shapes);
    }
}
