import java.util.Arrays;
import java.util.Scanner;

public class TriangleTypes {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter triangle Side1");
        double side1=sc.nextDouble();

        System.out.println("Enter triangle Side2");
        double side2=sc.nextDouble();

        System.out.println("Enter triangle Side3");
        double side3 = sc.nextDouble();

        if(side1==side2 && side2==side3){
            System.out.println("Equilateral Triangle");
        }else if(side1 == side2 || side2==side3 || side1==side3){
            System.out.println("Isosceles Triangle");
        }else if(isRightAngledTriangle(side1,side2,side3)){
            System.out.println("Right Angled Triangle");
        }else{
            System.out.println("Scalene Triangle");
        }
    }
    
    static boolean isRightAngledTriangle(double side1,double side2,double side3){
        double[] sides={side1,side2,side3};

        Arrays.sort(sides);

        return Math.pow(sides[0], 2)+Math.pow(sides[1],2)==Math.pow(sides[2],2);
    }
}
