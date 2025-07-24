class University {
    void enterRule(double math, double english, double chinese) {
        double total = math + english + chinese;
        if (total >= 180)
            System.out.println(total + "达到大学录取线");
        else
            System.out.println(total + "未达到大学录取线");
    }
}
class ImportantUniversity extends University {
    void enterRule(double math, double english, double chinese) {
        double total = math + english + chinese;
        if (total >= 220)
            System.out.println(total + "达到重点大学录取线");
        else
            System.out.println(total + "未达到重点大学录取线");
    }
}
public class Example5_4 {
    public static void main(String args[]) {
        double math = 62, english = 76.5, chinese = 67;
        ImportantUniversity univer = new ImportantUniversity();
        univer.enterRule(math, english, chinese); 
        math = 91;
        english = 82;
        chinese = 86;
        univer.enterRule(math, english, chinese); 
    }
}