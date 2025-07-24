public class sz{
	public static void main(String[] args){
        int a[]=new int[3];
        int b[]=new int[4];
        a[0]=1;a[1]=3;a[2]=3;
        b[0]=1;b[1]=2;b[2]=3;b[3]=4;
        a=b;
        for(int i=0;i<4;i++){
            System.out.println(a[i]);
        }
    }
    
}