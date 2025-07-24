//10的阶层
public class  jc{
    public static void main(String[] args){
        int sum=0,t=1;
        for(int i=1;i<=10;i++){
            t=t*i;
            sum=sum+t;

        }
        System.out.println("1!+2!+3!+...+10!="+sum);


    }
}