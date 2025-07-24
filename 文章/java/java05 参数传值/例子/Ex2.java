class Circle{
    double radius;
    double findArea(double r){
        radius=r;
        return 3.14*radius*radius;
    }
}
class PassObject{
    Circle a;
    public void printAreas(Circle c,int time){
        a=c;
        for(double i=1;i<=time;i++){
            System.out.printf("半径:%f  面积:%f\n",i,a.findArea(i)); 
        }
    }
}
public class Ex2{
    public static void main(String[] arg){
        PassObject a=new PassObject();
        Circle c=new Circle();
        a.printAreas(c,5);
    }
}