class People {
    int age, leg = 2, hand = 2;

    protected void showPeoleMess() {
        System.out.printf("%d岁,%d只腿,%d只手\t", age, leg, hand);
    }
}

class Student extends People {
    int number;

    void tellNumber() {
        System.out.printf("学号:%d\t", number);
    }

    int add(int x, int y) {
        return x + y;
    }
}

class UniverStudent extends Student {
    int multi(int x, int y) {
        return x * y;
    }
}

public class Example5_1 {
    public static void main(String[] args) {
        Student zhang = new Student();
        zhang.age = 17;
        zhang.number = 100101;
        zhang.showPeoleMess();
        zhang.tellNumber();
        int x = 9, y = 29;
        System.out.print("会做加法：");
        int result = zhang.add(x, y);
        System.out.printf("%d+%d=%d\n", x, y, result);
        UniverStudent geng = new UniverStudent();
        geng.age = 21;
        geng.number = 6609;
        geng.showPeoleMess();
        geng.tellNumber();
        System.out.print("会做加法：");
        result = geng.add(x, y);
        System.out.printf("%d+%d=%d\t", x, y, result);
        System.out.print("会做乘法：");
        result = geng.multi(x, y);
        System.out.printf("%d×%d=%d\n", x, y, result);
    }
}    