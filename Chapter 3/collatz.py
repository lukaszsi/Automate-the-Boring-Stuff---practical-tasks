def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1
    
while True:
    print('Input number')
    n = input()
    try:
        n = int(n)
    except:
        print('Please enter an integer')
        continue
    while n != 1:
        n = collatz(n)
        print(n)
    break



