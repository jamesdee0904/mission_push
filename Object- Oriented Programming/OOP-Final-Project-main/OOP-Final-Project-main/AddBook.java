package Methods;

import java.util.Scanner;

public class AddBook {
    Scanner sc = new Scanner(System.in);

    public void addNewBook() {
        Welcome addWelcome = new Welcome() {
            @Override
            void welcome() {
                System.out.println(" - ".repeat(8) + " ADD NEW BOOK " + " - ".repeat(9));
            }
        };

        addWelcome.welcome();

        Book defaultBooks = new Book();
        defaultBooks.availableBooks();

        System.out.print("\tEnter Book Title: ");
        String title = sc.nextLine();

        int nextId = Book.book.size() + 1;

        if (Book.book.containsValue(title)) {
            System.out.println("\tThat book already exists in the library.");
        } else {
            Book.book.put(nextId, title);
            System.out.println(" - ".repeat(22));
            System.out.println("\t\tSuccessfully added new book:");
            System.out.println("\t\tBook ID: " + nextId);
            System.out.println("\t\tBook Title: " + title);
            System.out.println(" - ".repeat(22));
        }
    }
}
