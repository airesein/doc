class Vehicle{
    String brand;
    double speed;
    Vehicle(){
       brand="耐地";
       speed=6;
    }
    void displayInfo(){
        System.out.print("品牌:"+brand+" 速度:"+speed+'\n');
    }  
}
class Car extends Vehicle{
    int numDoors=4;
    void displayInfo(){
        System.out.print("品牌:"+brand+" 速度:"+speed+" 车门数量:"+numDoors+'\n');
    }  
}
class Bicycle extends Vehicle{
    boolean isMountainBike=true;
    void displayInfo(){
        System.out.print("品牌:"+brand+" 速度:"+speed+" 是否为山地车:"+isMountainBike+'\n');
    }  
}
public class Ex{
    public static void main(String arg[]){
        Car a=new Car();
        Bicycle b=new Bicycle();
        a.displayInfo();
        b.displayInfo();
    }
}