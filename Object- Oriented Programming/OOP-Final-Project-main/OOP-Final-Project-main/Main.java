import Methods.Admin;
import Methods.Student;

import javax.swing.text.View;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Student student = new Student();
        Admin admin = new Admin(student);
        while (true){
            System.out.println(" - ".repeat(22));
            System.out.println("\t[1] Admin");
            System.out.println("\t[2] Student");
            System.out.println("\t[3] Exit");
            System.out.print("\t\tEnter a number: ");
            int num = sc.nextInt();
            if (num == 1){
                admin.login();
            } else if (num == 2) {
                student.getInfo();
            }else if (num == 3){
                break;
            }else {
                System.out.println(" - ".repeat(22));
                System.out.println("\t\tInvalid input.");
                System.out.println(" - ".repeat(22));
            }

        }
    }
}
