public class Test {
    public static void main(String[] args) {
        CPU cpu = new CPU();
        cpu.setSpeed(2200);
        HardDisk disk = new HardDisk();
        disk.setAmount(200);
        PC pc = new PC();
        pc.setCPU(cpu);
        pc.setHardDisk(disk);
        pc.show();
    }
}

class PC {
    CPU cpu;
    HardDisk HD;

    public void setCPU(CPU c) {
        cpu = c;
    }

    public void setHardDisk(HardDisk h) {
        HD = h;
    }

    public void show() {
        System.out.println("CPU速度:" + cpu.getSpeed() + "MHz");
        System.out.println("硬盘容量:" + HD.getAmount() + "GB");
    }
}

class CPU {
    int speed;

    public int getSpeed() {
        return speed;
    }

    public void setSpeed(int m) {
        speed = m;
    }
}

class HardDisk {
    int amount;

    public int getAmount() {
        return amount;
    }

    public void setAmount(int m) {
        amount = m;
    }
}