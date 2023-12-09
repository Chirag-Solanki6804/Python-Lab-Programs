import java.util.Scanner;

// 2. Convert number of days into year, week & days. [e.g. 375 days mean 1 year, 1 week and 3 days]

public class DayConvert {
    public static void main(String[] args) {
        System.out.println("Enter Total Days");
        Scanner sc=new Scanner(System.in);
        int days=sc.nextInt();

        int years=days/365;

        int months=(days-(years*365))/30;

        int weeks=(days-((years*365)+(months*30)))/7;

        days=days-((years*365)+(months*30)+(weeks*7));

        System.out.println(years+"-Year : "+months+"-Months : "+weeks+"-Weeks : "+days+"-Days");
    }
}
