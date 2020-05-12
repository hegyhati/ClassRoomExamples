import java.util.ArrayList;

public class HanoiTower {
    private ArrayList<Integer> disks;

    public HanoiTower(){
        disks = new ArrayList<Integer>();
    }
    public HanoiTower(int diskCount) {
        disks = new ArrayList<Integer>();
        for(int size = diskCount; size >= 1; size --){
            disks.add(size);
        }
    }

    public String toString(){
        String toReturn = "";
        for(int i=0; i<disks.size(); i++)
            toReturn += " " + disks.get(i);
        return toReturn;
    }

    public int pop(){
        if(!isEmpty()) {
            Integer toReturn = disks.get(disks.size() - 1);
            disks.remove(disks.size() - 1);
            return toReturn;
        } else return -1;
    }

    public boolean put(int size){
        if(isEmpty() || disks.get(disks.size()-1) > size) {
            disks.add(size);
            return true;
        } else return  false;
    }

    public boolean isEmpty(){
        return disks.size()==0;
    }

    public static void main(String[] args) {
        HanoiTower t = new HanoiTower();
        t.put(2);
        System.out.println(t);
        t.put(2);
        System.out.println(t);
        t.put(1);
        System.out.println(t);
    }
}
