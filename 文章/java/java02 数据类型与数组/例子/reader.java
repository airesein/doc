import java.util.Scanner;
public class reader{
	public static void main(String[] args){
		Scanner reader=new Scanner(System.in);
		double x=reader.nextDouble(),sum=0;
		while(x!=0){
			sum+=x;		
			x=reader.nextDouble();
		}
		
		System.out.printf("%6f",sum);
	}


}