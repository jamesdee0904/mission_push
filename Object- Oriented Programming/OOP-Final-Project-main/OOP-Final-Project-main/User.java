package Methods;
import java.time.LocalDate;
import java.time.LocalTime;

public class User {
    private String g_suite;
    private String sr_code;
    private LocalTime localTime;
    private LocalDate localDate;

    public User(String g_suite, String sr_code, LocalTime localTime, LocalDate localDate){
        this.g_suite = g_suite;
        this.sr_code = sr_code;
        this.localTime = LocalTime.now();
        this.localDate = LocalDate.now();
    }

    public String getG_suite() {
        return g_suite;
    }

    public void setG_suite(String g_suite) {
        this.g_suite = g_suite;
    }

    public String getSr_code() {
        return sr_code;
    }

    public void setSr_code(String sr_code) {
        this.sr_code = sr_code;
    }

    public LocalTime getLocalTime() {
        return localTime;
    }

    public void setLocalTime(LocalTime localTime) {
        this.localTime = localTime;
    }

    public LocalDate getLocalDate() {
        return localDate;
    }

    public void setLocalDate(LocalDate localDate) {
        this.localDate = localDate;
    }
}
