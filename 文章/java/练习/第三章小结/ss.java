public class ss {
    public static void main(String[] args) {
        System.out.print("100 以内的素数：");
        for (int i = 2; i <= 100; i++) {
            boolean pd = true;
            for (int j = 2; j <= i/2; j++) {
                if (i % j == 0) {
                    pd = false;
                    break;
                }
            }
            if (pd) {
                System.out.print(i + "、");
            }
        }
    }
}    