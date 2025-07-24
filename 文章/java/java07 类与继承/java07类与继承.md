# 继承

继承得到的类是**子类**，被继承的类是**父类（超类）**

```java
class 子类名 extends 父类名{

}
```

根节点是Object类（java.long中），``` class A与class A extends Object一样```

**同一包中，继承除了private之外的**

**不同包中，继承protected、public的**

**子类初始化时，父类所有的都分配内存，默认使用父类的无参数的构造方法，若无则用super**

```  super(name, age);```

# 成员变量的隐藏 

若子类的成员变量与父类同名，则父类的成员变量就会被**隐藏**

**访问隐藏的**

``` java
//子类
class Child extends Parent {
    int variable = 20;

    public void printBothVariables() {
        // 访问父类的变量
        System.out.println("父类变量的值: " + super.variable);
        // 访问子类的变量
        System.out.println("子类变量的值: " + variable);
    }
}
```

# 重写

**重写不能降低方法的访问权限，但能提高访问权限**

**子类中重写方法需要和父类被重写的方法具有相同的方法名、参数列表以及返回值类型。**

# instanceof

左侧是对象，右侧是类，如果左侧是右侧的，则是true

# final

```java
final class A{
    
}
```

final修饰类，类不能被继承

final修饰变量，变成常量

final修饰方法，不能被重写

# 上转型对象

在 Java 里，上转型对象指的是将一个子类对象赋值给父类类型的变量。这种操作也被叫做向上转型，它是一种自动类型转换，不需要额外的强制类型转换操作。

1. **可调用父类成员**：上转型对象能够调用父类中定义的成员变量和方法。
2. **可调用子类重写方法**：若子类对父类的某个方法进行了重写，那么上转型对象调用该方法时，执行的是子类重写后的方法。
3. **不可调用子类特有成员**：上转型对象无法直接调用子类中特有的成员变量和方法。

# abstract

抽象类，抽象方法，抽象类可以没有抽象方法

抽象方法只能被声明，不能被实现，不能被final修饰

```java
abstract int min(a,b);
```

abstract类不能用new创建该类的对象

抽象类的子类必须实现父类的所有的抽象方法2
