// 5. Convert temperature from Fahrenheit to Celsius. (Formula: c=(((f-32)\*5))/9)

import java.util.Scanner;

public class TempConvert {
    public static void main(String[] args) {
        System.out.println("Enter Temp in Fahrenheit :");
        Scanner sc=new Scanner(System.in);
        double fahrenheit = sc.nextDouble();

        double celsius=((fahrenheit-32)*5)/9;

        System.out.println(fahrenheit+" fahrenheit ="+celsius+" celsius");

    }
}
