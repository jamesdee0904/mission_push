package Methods;

import java.util.Map;

public class View {
    Welcome viewWelcome = new Welcome() {
        @Override
        void welcome() {
            System.out.println(" - ".repeat(8) + " AVAILABLE BOOKS " + " - ".repeat(9));
        }
    };

    public void showAvailableBooks() {
        Book book = new Book();
        book.availableBooks();

        if (book.book.isEmpty()) {
            viewWelcome.welcome();
            System.out.println("\t\tNo available books in the library.");
        } else {
            viewWelcome.welcome();
            for (Map.Entry<Integer, String> entry : book.book.entrySet()) {
                Integer id = entry.getKey();
                String title = entry.getValue();
                System.out.println("\t\tBook ID: " + id);
                System.out.println("\t\tBook Title: " + title);
                System.out.println(" - ".repeat(22));
            }
        }
    }
}
