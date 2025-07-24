interface Animal {
    void cry();
    String getAnimalName();
}
class Simulator {
    void playSound(Animal animal) {
        animal.cry();
        System.out.println(animal.getAnimalName());
    }
}

class Dog implements Animal {
    public void cry() {
        System.out.println("汪汪汪");
    }
    public String getAnimalName() {
        return "Dog";
    }
}

class Cat implements Animal {
    public void cry() {
        System.out.println("喵喵喵");
    }
    public String getAnimalName() {
        return "Cat";
    }
}

public class Application {
    public static void main(String[] args) {
        Simulator simulator = new Simulator();
        simulator.playSound(new Dog());
        simulator.playSound(new Cat());
    }
}