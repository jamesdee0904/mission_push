package Methods;

import javax.swing.plaf.synth.SynthOptionPaneUI;
import java.awt.*;
import java.util.Map;
import java.util.Scanner;

public class Admin {
    Scanner sc = new Scanner(System.in);
    private String admin_email = "admin";
    private String password = "admin123";
    private Student student;

    public Admin(Student student) {
        this.student = student;
    }

    public void login() {
        Welcome welcomeAdmin = new Welcome() {
            @Override
            void welcome() {
                System.out.println(" - ".repeat(7) + "Login Admin" + " - ".repeat(7));
            }
        };
        System.out.print("Admin Email: ");
        String email = sc.nextLine();
        System.out.print("Admin Password: ");
        String pass = sc.nextLine();
        if (email.equals(admin_email) && pass.equals(password)) {
            while (true) {
                System.out.println("\t[1] Student Login");
                System.out.println("\t[2] Borrowed Book");
                System.out.println("\t[3] Returned Book");
                System.out.println("\t[4] View Available Books");
                System.out.println("\t[5] Add New Book");
                System.out.println("\t[6] Exit");
                System.out.print("\t\tEnter number: ");
                int num = sc.nextInt();
                sc.nextLine();

                if (num == 1) {
                    studentLogin();
                } else if (num == 2) {
                    borrowedBook();
                } else if (num == 3) {
                    returnedBook();
                } else if (num == 4) {
                    View view = new View();
                    view.showAvailableBooks();
                } else if (num == 5) {
                    AddBook addBook = new AddBook();
                    addBook.addNewBook();
                } else if (num == 6) {
                    break;
                } else {
                    System.out.println("Invalid input, re-try.");
                }
            }
        }
    }

    public void studentLogin() {
        Welcome welcomeStudent = new Welcome() {
            @Override
            void welcome() {
                System.out.println(" - ".repeat(7) + " Student Login " + " - ".repeat(7));
            }
        };
        if (student.user.isEmpty()) {
            welcomeStudent.welcome();
            System.out.println("\t\tNo Student login yet.");
        } else {
            for (User u : student.user) {
                welcomeStudent.welcome();
                System.out.println("\t\tStudent Name: " + u.getG_suite());
                System.out.println("\t\tSr-Code: " + u.getSr_code());
                System.out.println("\t\tTime Login: " + u.getLocalTime());
                System.out.println("\t\tDate Login: " + u.getLocalDate());
                System.out.println(" - ".repeat(22));
            }
        }
    }

    public void borrowedBook() {
        Welcome welcomeBorrowed = new Welcome() {
            @Override
            void welcome() {
                System.out.println(" - ".repeat(8) + " BORROWED BOOK " + " - ".repeat(9));
            }
        };
        if (student.borrow.isEmpty()) {
            welcomeBorrowed.welcome();
            System.out.println("\tNo borrowed Book yet.");
        } else {
            welcomeBorrowed.welcome();
            for (Map.Entry<Integer, String> entry : student.borrow.entrySet()) {
                Integer id = entry.getKey();
                String title = entry.getValue();
                for (User u : student.user) {
                    System.out.println("\t\tStudent Name: " + u.getG_suite());
                    System.out.println("\t\tSr-Code: " + u.getSr_code());
                    System.out.println("\t\tBook ID: " + id);
                    System.out.println("\t\tBook Title: " + title);
                    System.out.println(" - ".repeat(22));
                }
            }
        }
    }
    public void returnedBook(){
        Welcome returnedWelcome = new Welcome() {
            @Override
            void welcome() {
                System.out.println(" - ".repeat(8) + " RETURNED BOOK " + " - ".repeat(9));
            }
        };
        if (student.return_book.isEmpty()){
            returnedWelcome.welcome();
            System.out.println("\t\tNo book has been return yet.");
            System.out.println(" - ".repeat(22));
        }else {
            for (Map.Entry<Integer, String> returned : student.return_book.entrySet()) {
                Integer id = returned.getKey();
                String title = returned.getValue();
                for (User u : student.user) {
                    returnedWelcome.welcome();
                    System.out.println("\t\tStudent Name: " + u.getG_suite());
                    System.out.println("\t\tSr-Code: " + u.getSr_code());
                    System.out.println("\t\tBook ID: " + id);
                    System.out.println("\t\tBook Title: " + title);
                    System.out.println(" - ".repeat(22));
                }
            }
        }
    }
}
