print("1. Count Prime Numbers Row-wise")
print("2. Count Perfect Numbers Column-wise")
print("3. Display Row-wise Sum")
print("4. Exit")
choice = int(input("Enter your choice: "))
match choice:
    case 1:
        row=int(input("Enter the number of rows: "))
        col=int(input("Enter the number of columns: "))
        matrix = []
        print("Enter the elements of the matrix:")
        for i in range(row):
            row=[]
            for j in range(col):
                row.append(int(input()))
            matrix.append(row)
        if row==col:
            # Implementation for counting prime numbers row-wise
            count = 0
            for i in range(row):
                for j in range(col):
                    num = matrix[i][j]
                    if num%2!=0:
                        for k in range(2,num):
                            if num%k==0:
                                break
                        else:
                            count += 1
                    else:
                            count += 1
            print("Number of prime numbers in the matrix:", count)
        
    case 2:
        row=int(input("Enter the number of rows: "))
        col=int(input("Enter the number of columns: "))
        matrix = []
        print("Enter the elements of the matrix:")
        for i in range(row):
            row=[]
            for j in range(col):
                row.append(int(input()))
            matrix.append(row)
        if row==col:
            # Implementation for counting perfect numbers column-wise
            count = 0
            for j in range(col):
                for i in range(row):
                    num = matrix[i][j]
                    if num > 0:
                        sum_of_divisors = sum(k for k in range(1, num) if num % k == 0)
                        if sum_of_divisors == num:
                            count += 1
            print("Number of perfect numbers in the matrix:", count)

        
    case 3:
        # Implementation for displaying row-wise sum
        row=int(input("Enter the number of rows: "))
        col=int(input("Enter the number of columns: "))
        matrix = []
        print("Enter the elements of the matrix:")      
        for i in range(row):
            row=[]
            for j in range(col):
                row.append(int(input()))
            matrix.append(row)
        row_sums = [sum(row) for row in matrix]
        print("Row-wise sums of the matrix:", row_sums)
            
    case 4:
        exit()
   