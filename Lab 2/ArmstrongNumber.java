public class ArmstrongNumber {
    public static void main(String[] args) {
        //  1,153,370,371,407
        System.out.println(isArmstrong(18));
    }

    static boolean isArmstrong(int number){
        int temp=number;
        int totalDigit=0;

        while (temp>0) {
            totalDigit++;
            temp=temp/10;
        }

        temp=number;

        int result=0;
        while (temp>0) {
            int digit=temp%10;
            result+=numberPower(digit, totalDigit);
            temp=temp/10;
        }

        return result==number;
    }

    static int numberPower(int number,int power){
        int result=1;
        for(int i=0;i<power;i++){
            result=result*number;
        }
        return result;
    }
}
