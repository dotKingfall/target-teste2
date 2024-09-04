def main():
    fibonacci = [0, 1]
    
    n = input("Choose a number: ")
    if not n.isnumeric():
        print("Invalid input")
        return False
    
    n = int(n)  ## Passing Python's default string input to int  
    if n <= 1:
        print("The number", n, "does indeed takes part in the Fibonacci sequence!")
        return True
    
    for i in range(1, n+1):
        tmp = fibonacci[i-1] + fibonacci[i]  ## Sum previous and current numbers to make the next element
        fibonacci.append(tmp)
        
        if tmp > n:
            break
    
    if n not in fibonacci:
        print("The number", n, "does not exist in the Fibonacci sequence!")

    else:
        print("The number", n, "does indeed takes part in the Fibonacci sequence!")
    
    
    print("Your complete sequence is:", fibonacci[:-1])    
    return True


main()