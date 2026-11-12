print("1. Add Two Matrices")
print("2. Subtract Two Matrices")
print("3. Compare Two Matrices")
print("4. Exit")
choice=int(input("Enter your choice (1-4): "))
match choice:
    case 1:
       rows=int(input("Enter number of rows:"))
       cols=int(input("Enter number of columns:"))  
       matrix1=[]
       print("Enter elements of first matrix:")
       for i in range(rows):
              row=[]
              for j in range(cols):
                row.append(int(input()))
              matrix1.append(row)
       print("Enter elements of second matrix:")
       matrix2=[]
       for i in range(rows):
                row=[]
                for j in range(cols):
                    row.append(int(input()))
                matrix2.append(row)
       result=[]
       for i in range(rows):
                row=[]
                for j in range(cols):
                    row.append(matrix1[i][j]+matrix2[i][j])
                result.append(row)
       print("Resultant Matrix:")
       for row in result:
                print(row)
    case 2:
        rows=int(input("Enter number of rows:"))
        cols=int(input("Enter number of columns:"))  
        matrix1=[]
        print("Enter elements of first matrix:")
        for i in range(rows):
                row=[]
                for j in range(cols):
                    row.append(int(input()))
                matrix1.append(row)
        print("Enter elements of second matrix:")
        matrix2=[]
        for i in range(rows):
                row=[]
                for j in range(cols):
                    row.append(int(input()))
                matrix2.append(row)
        result=[]
        for i in range(rows):
                row=[]
                for j in range(cols):
                    row.append(matrix1[i][j]-matrix2[i][j])
                result.append(row)
        print("Resultant Matrix:")
        for row in result:
                print(row)
    case 3:
        rows=int(input("Enter number of rows:"))
        cols=int(input("Enter number of columns:"))  
        matrix1=[]
        print("Enter elements of first matrix:")
        for i in range(rows):
                row=[]
                for j in range(cols):
                    row.append(int(input()))
                matrix1.append(row)
        print("Enter elements of second matrix:")
        matrix2=[]
        for i in range(rows):
                row=[]
                for j in range(cols):
                    row.append(int(input()))
                matrix2.append(row)
        if matrix1==matrix2:
            print("Matrices are equal")
        else:
            print("Matrices are not equal")
    case 4:
        exit()
    




             

