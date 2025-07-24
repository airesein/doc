
class Cube {
    Area mj;
    void setMj(Area c) {
        mj = c;
    }
    void set(int x) {
        mj.set(x);
    }
    int solve() {
        int sideArea = mj.solve();
        return sideArea * sideArea * sideArea;
    }
}

class Area {
    int a = -1;
    void set(int x) {
        a = x;
    }
    int solve() {
        if (a == -1) {
            return 0;
        } else {
            return a * a;
        }
    }
}

public class Ex {
    public static void main(String[] args){
        Cube m = new Cube();
        Area area = new Area();
        m.setMj(area);
        m.set(10);
        int x = m.solve();
        System.out.println(x);
    }
}    