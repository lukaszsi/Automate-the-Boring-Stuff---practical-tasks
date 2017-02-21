class Collatz {
    Collatz(int number) {
        while (number != 1) {
            number = collatz(number);
            System.out.println(number); 
        }
    }
    int collatz(int num) {
        if (num % 2 == 0) {
            return num / 2;
        } else {
            return 3 * num + 1;
        }
    }
}
