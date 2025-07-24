//PC CPU HardDisk Test
class CPU{
    int speed;
    void setSpeed(int m){
        speed=m;
    }
    int getSpeed(){
        return speed;
    }
}
class HardDisk{
    int amount;
    void setAmount(int m){
        amount=m;
    }
    int getAmount(){
        return amount;
    }
}
class PC{
    CPU cpu;
    HardDisk HD;
    void setCPU(CPU c){
        cpu=c;
    }
    void setHardDisk(HardDisk h){
        HD=h;
    }
    void show(){
        System.out.printf("CPU的速度：%d 硬盘的容量：%d",cpu.getSpeed(),HD.getAmount());
    }
}
public class Test{
    public static void main(String[] args){
        CPU cpu=new CPU();
        cpu.setSpeed(2200);
        HardDisk disk=new HardDisk();
        disk.setAmount(200);
        PC pc=new PC();
        pc.setCPU(cpu);
        pc.setHardDisk(disk);
        pc.show();
    }
}