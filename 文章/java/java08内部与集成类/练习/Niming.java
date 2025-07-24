abstract class Bank{
    int money;
    public  Bank(){

        
        money=100;
    }
    public Bank(int money){
        this.money=money;
    }
    public abstract void output();


    
}
class ShowBank{
    void showMess(Bank bank){
        bank.output();
    }
}
public class Niming{
    public static void main(String[] args){
        ShowBank showBank=new ShowBank();
        showBank.showMess(new Bank(200){
            public void output(){
                money+=100;
                System.out.printf("资金："+"%d",money);
            }
        });
    }
}