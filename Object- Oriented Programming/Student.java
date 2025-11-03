public class Student {
    //Instance and static
    //Instance-> belongs to the instance of the class
    //Static-> belongs to the class itself

    //access modifiers
    //private
    //protected
    //public
    //void or none

    //Instance variables
    public String name;
    public int age;
    public boolean isValid;
    public double salary;

    public static String address;

    //Constructor does what? ->
    //is used to initliaze intance variables
    //must be the same name of the class
    //it automatically called when an instance of a class is created
    //this keyword always points to instance variables

    //Constructor
    public Student(String name, int age, boolean isValid, double salary){
        System.out.println("This constructor is called!");
        this.name = name;
        this.age = age;
        this.isValid = isValid;
        this.salary = salary;
    }
    //PRACTICE DOESNT MAKE U PERFECT BUT IT MAKES YOU BETTER THAN YESTERDAY!!!

    //is it allowed to have multiple constructor in 1 class?
    public Student(){
        System.out.println("This is a constructor without parameter!");
        this.name = "Mark";
        this.age = 45;
        this.isValid = true;
        this.salary = 123.456;
    }

    public Student(String name){
        System.out.println("This constructor does have 1 parameter!");
        this.name = name;
    }

    //Nested Class

    //Inheritance-> Parent Class -> Child Class





}
