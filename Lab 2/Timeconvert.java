import java.util.Scanner;

/**
 * 1. Convert seconds into hours, minutes & seconds and print in HH: MM: SS. 
 * [e.g. 10000 seconds = 02:46:40)]
 */

public class Timeconvert{
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter Time Seconds");
        int seconds=sc.nextInt();

        int minutes=seconds/60;

        int hours=minutes/60;

        minutes=minutes-hours*60;

        seconds=seconds-((hours*3600)+(minutes*60));

        System.out.println(hours+":"+minutes+":"+seconds);
    }
}