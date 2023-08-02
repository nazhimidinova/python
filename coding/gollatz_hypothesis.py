c0 = int(input("Please provide any non-negative and non-zero integer number: "))

if c0 <= 0:
    print("Please provide a valid positive integer.")
else:
    steps = 0
    
    while c0 != 1:
        if c0 % 2 == 0:
            c0 = c0 // 2  # Integer division
        else:
            c0 = 3 * c0 + 1
        
        print(c0)
        steps += 1
    
    print("Steps =", steps)

