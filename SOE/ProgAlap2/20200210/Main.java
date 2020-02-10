

public class Main{

    public static char getMissingChar(String text) {
        for(char c=32;c<0xFFFF;c++)
            if(text.lastIndexOf(c)==-1) return c;
        return 0;
    }

    // Currently unused, alternative for the above
    public static char getMissingChar2(String text) {
        boolean[] has=new boolean[65536];
        for(int idx=0;idx<text.length();++idx)
            has[text.charAt(idx)]=true;        
        for(char c=32; c<65536; ++c)
            if(!has[c]) return c;
        return 0;
    }

    public static String swapCharacter(String original, char c1, char c2, char temporary) {
        return original.replace(c1,temporary)
                       .replace(c2,c1)
                       .replace(temporary,c2);
    }

    public static String swapCharacter(String original, char c1, char c2){
        char missing=getMissingChar(original);
        if(missing!=0) return swapCharacter(original, c1, c2, missing);
        else {
            String toReturn="";
            for(int idx=0;idx<original.length();++idx){
                if(original.charAt(idx)==c1) toReturn+=c2;
                else if(original.charAt(idx)==c2) toReturn+=c1;
                else toReturn+=original.charAt(idx);
            } 
            return toReturn;
        } 
    }

    public static void main(String[] args) { 
        String ize="Elmentem boltba karalabet venni, mert azt szeretem.";
        ize=swapCharacter(ize, 'a', 'e');
        ize=swapCharacter(ize, 'A', 'E');
        System.out.println(ize);
    }
}
