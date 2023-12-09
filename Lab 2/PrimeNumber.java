public class PrimeNumber {
    public static void main(String[] args) {
        System.out.println(isPrime(13));
    }

    static boolean isPrime(int number){
        if(number<2){
            return false;
        }
        for(int i=2;i<=number/2;i++){
            if(number%i==0){
                return false;
            }
        }
        return true;
    }
}
