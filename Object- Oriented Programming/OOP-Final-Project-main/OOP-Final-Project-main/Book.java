package Methods;

import java.util.HashMap;
import java.util.Map;

public class Book {
    public static HashMap<Integer, String> book = new HashMap<>();

    Welcome welcome = new Welcome() {
        @Override
        void welcome() {
            System.out.println(" - ".repeat(7) + " Welcome to Library " + " - ".repeat(7));
        }
    };

    public void availableBooks() {
        if (book.isEmpty()) {
            book.put(1, "Computer Programming");
            book.put(2, "Advance Computer Programming");
            book.put(3, "Database Management");
            book.put(4, "Networking 1");
            book.put(5, "Physics-Calculus");
            book.put(6, "Discrete Mathematics");
        }
    }

    public void showBooks() {
        for (Map.Entry<Integer, String> entry : book.entrySet()) {
            Integer id = entry.getKey();
            String title = entry.getValue();
            System.out.println("\tID: " + id + " Title: " + title);
        }
    }
}
