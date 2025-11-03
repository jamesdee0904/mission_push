package Methods;

import java.time.LocalDate;
import java.time.LocalTime;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Student extends Book {
    private Scanner sc = new Scanner(System.in);
    ArrayList<User> user = new ArrayList<>();
    HashMap<Integer, String> borrow = new HashMap<>();
    HashMap<Integer, String> return_book = new HashMap<>();

    Welcome welcome = new Welcome() {
        @Override
        void welcome() {
            System.out.println(" - ".repeat(7) + " Welcome Student! " + " - ".repeat(7));
        }
    };

    public void getInfo() {
        System.out.println(" - ".repeat(7) + " Student Login " + (" - ".repeat(7)));
        System.out.print("\tEnter G-Suite: ");
        String g_suite = sc.nextLine();
        System.out.print("\tSr-Code: ");
        String sr_code = sc.nextLine();
        if (sr_code.matches("\\d{2}-\\d{5}")) {
            LocalTime localTime = LocalTime.now();
            LocalDate localDate = LocalDate.now();
            User newLogin = new User(g_suite, sr_code, localTime, localDate);
            user.add(newLogin);
            welcome.welcome();
            System.out.println();
            while (true) {
                System.out.println("[1] Borrow Book\n[2] Return Book\n[3] Exit");
                System.out.print("Enter number: ");
                int enter = sc.nextInt();
                if (enter == 1) {
                    borrowBook();
                } else if (enter == 2) {
                    returnBook();
                } else if (enter == 3) {
                    break;
                } else {
                    System.out.println("Invalid input. Please try again.");
                }
            }
        }
    }

    public void borrowBook() {
        Welcome borrowedWelcome = new Welcome() {
            @Override
            void welcome() {
            }
        };
        borrowedWelcome.welcome();
        availableBooks();
        showBooks();
        System.out.print("\t\tBook id: ");
        int book_id = sc.nextInt();
        if (book.containsKey(book_id)){
            String title = book.get(book_id);
            borrow.put(book_id, title);
            System.out.println(" - ".repeat(22));
            System.out.println("\t\t Successfully borrowed title: " + title);
            System.out.println(" - ".repeat(22));
        }else{
            System.out.println("No book id like that.");
        }
    }

    public void returnBook(){
        Welcome returnWelcome = new Welcome() {
            @Override
            void welcome() {
                System.out.println(" - ".repeat(7) + " Return Book " + " - ".repeat(7));
            }
        };
        if (borrow.isEmpty()){
            System.out.println("No book to return yet.");
        }else{
            returnWelcome.welcome();
            for (Map.Entry<Integer, String> returnbook : borrow.entrySet()){
                Integer id = returnbook.getKey();
                String title = returnbook.getValue();
                System.out.println("\tID: " + id + " Title: " + title);
            }
            System.out.print("\t\tReturn Book id: ");
            int bookID = sc.nextInt();
            if (borrow.containsKey(bookID)){
                String title = borrow.get(bookID);
                return_book.put(bookID, title);
                borrow.remove(bookID, title);
                System.out.println(" - ".repeat(22));
                System.out.println("\t\t Successfully return the book: " + title);
                System.out.println(" - ".repeat(22));
            }
        }
    }
}
