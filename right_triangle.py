# Print a Right angled Triangle
"""For a given number n, print a right triangle made of stars (*) with n rows."""

class RightTriangle:
    def __init__(self, n):
        self.n = n
        
    def print_triangle(self):
        for i in range(1, self.n + 1):
            print('*'  * i)
            # print ('*' * i) will print the star in a single line
            # Each row will have i stars, where i is the current row number
            # The outer loop iterates through each row, and the inner loop prints the stars
            # The print statement prints the stars in each row
def get_user_input():
    while True:
        try:
            n = int(input("Enter the number of rows for each triangle: "))
            if n > 0:
                return n
            else:
                print("please enter a positive integer.")
        except ValueError:
            print("Invalid input. please enter a positive integer.")

def main():
    n = get_user_input()
    tree = RightTriangle(n)
    tree.print_triangle()
    print(f"The right triangle with {n} rows is printred above.")
    
    
if __name__ == "__main__":
    main()