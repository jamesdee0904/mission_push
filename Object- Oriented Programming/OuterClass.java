public class OuterClass {
    //Instance variable
    public String name;

    //Constructor
    public OuterClass(){
        this.name = "Your Name!";
    }

    public OuterClass(String name){
        this.name = name;   
    }

    //Intance Method
    void getName(){
        System.out.println("Hello " + name);
    }

    //when to use nested class?
    //DATA STRUCTURE
    //if the inner class only belong and only used on the outer class!

    public static class InnerClass{
        public static String favFood = "adobo";
        public static String favColor = "Mink";
        public static int dreamSalary = 234;

        //Parameterized Intantiate
        static void getfave(OuterClass outer ){
            Utility.helloMsg();
            System.out.println(outer.name + "Your Favorites are: " + favColor + favColor + dreamSalary);
        }

      

    }
    
}
