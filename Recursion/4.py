"""Assignment 4:
 Lottery Ticket Verification (Count Occurrences Using Recursion)

A lottery company assigns a unique ticket number to every participant. Before announcing the results, the company wants to determine how many times a lucky digit appears in a ticket number. This helps identify tickets eligible for special bonus rewards.

As a software developer, your task is to write a recursive Python program that counts the number of times a given digit appears in the ticket number.

Task

Write a recursive function to count the occurrences of a given digit in a ticket number.

Input Format
The first line contains an integer representing the Ticket Number.
The second line contains an integer representing the Lucky Digit.
Output Format

Display the number of times the lucky digit appears in the ticket number using the format:

Digit <Lucky Digit> appears <Count> times.
Sample Input
Enter Ticket Number:
1122334412

Enter Lucky Digit:
2
Sample Output
Digit 2 appears 3 times.
Sample Input 2
Enter Ticket Number:
987654321

Enter Lucky Digit:
5
Sample Output 2
Digit 5 appears 1 time.
Sample Input 3
Enter Ticket Number:
11111111

Enter Lucky Digit:
2
Sample Output 3
Digit 2 appears 0 times."""
num=int(input("Enter Ticket Number:\n"))
digit=int(input("Enter Lucky Digit:\n"))
if digit<0 or digit>9:
    print("Invalid Lucky Digit. Please enter a digit between 0 and 9.")
else:
    def count_occurrences(ticket_number, lucky_digit):
        if ticket_number == 0:
            return 0
        else:
            last_digit = ticket_number % 10
            if last_digit == lucky_digit:
                return 1 + count_occurrences(ticket_number // 10, lucky_digit)
            else:
                return count_occurrences(ticket_number // 10, lucky_digit)

    count = count_occurrences(num, digit)
    print(f"Digit {digit} appears {count} times.")