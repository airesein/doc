interface Com{
    public static final int MAX=100;
    public abstract void on();
    public abstract float sum(float x,float y);
    default int max(int a,int b){
        outPutJava();
        return a>b?a:b;
    }
    public static void f(){
        System.out.println("注意是从JAVA SE 8 开始的");

    }
     public static void outPutJava(){
        System.out.println("Java");

    }

}
class AAA implements Com{
    public void on(){
        System.out.println("打开电视");
    }
    public float sum(float x,float y){
        return x+y;
    }
}
public class Ex6_1{
    public static void main(String args[]){
        AAA a =new AAA();
        System.out.println("接口中的常量"+AAA.MAX);
        System.out.println("调用on方法（重写的）：");
        a.on();
        System.out.println("调用sum方法（重写的）"+a.sum(12,18));
        System.out.println("调用接口提供的default方法"+a.max(12,78));
        Com.f();

    }
}