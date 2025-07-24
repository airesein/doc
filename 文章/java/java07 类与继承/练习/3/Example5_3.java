class Goods {
    public double weight;
    public void oldSetWeight(double w) {
        weight = w;
        System.out.println("double型的weight = " + weight);
    }
    public double oldGetPrice() {
        double price = weight * 10;
        return price;
    }
}
class CheapGoods extends Goods {
    public int weight;
    public void newSetWeight(int w) {
        weight = w;
        System.out.println("int型的weight = " + weight);
    }
    public double newGetPrice() {
        double price = weight * 10;
        return price;
    }
}
public class Example5_3 {
    public static void main(String args[]) {
        CheapGoods cheapGoods = new CheapGoods();
        cheapGoods.newSetWeight(198);
        System.out.println("对象cheapGoods的weight的值是:" + cheapGoods.weight);
        System.out.println("cheapGoods用子类新增的优惠方法计算价格: " + cheapGoods.newGetPrice());
        cheapGoods.oldSetWeight(198.987);
        System.out.println("cheapGoods使用继承的方法(无优惠)计算价格: " + cheapGoods.oldGetPrice());
    }
}