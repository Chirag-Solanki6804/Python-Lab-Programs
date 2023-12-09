import java.util.Scanner;

public class SimpleInterest {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter Principal Amount:");
        double principal = scanner.nextDouble();

        System.out.println("Enter Rate of Interest:");
        double rateOfInterest = scanner.nextDouble();

        System.out.println("Enter Time Period (in years):");
        double timePeriod = scanner.nextDouble();

        double simpleInterest = (principal * rateOfInterest * timePeriod) / 100;

        System.out.println("Simple Interest: " + simpleInterest);
    }
}