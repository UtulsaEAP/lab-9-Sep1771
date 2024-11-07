def fibonacci(n):
    
    #write your code here
    
    list_fib = [0,1]

    fib_counter = 0 
    while fib_counter <= n:

        list_fib.append(list_fib[fib_counter] + list_fib[fib_counter + 1])

        fib_counter += 1



    return list_fib[n]

if __name__ == '__main__':
    start_num = int(input())

    print(f'fibonacci({start_num}) is {fibonacci(start_num)}')