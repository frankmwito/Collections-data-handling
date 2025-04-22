# sum of Squares
"""Write a program that uses a for loop to calculate the sum of squares of the first n natural numbers."""

class SumOfSquares:
    def __init__(self, n):
        self.n = n
        self.sum = 0
        
    def calculate_sum_of_squares(self):
        for i in range(1, self.n+1):
            self.sum += i ** 2
            
            
            
def get_user_input():
    while True:
        try:
            n = int(input("Enter a positive integer: "))
            if n > 0:
                return n
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. please enter a positive integer.")
            
            
def main():
    n = get_user_input()
    sum_of_squares = SumOfSquares(n)
    sum_of_squares.calculate_sum_of_squares()
    print(f"The sum of squares of the first {n} natural numbers is: {sum_of_squares.sum}")
    
    
    
if __name__ == "__main__":
    main()
    # This code is a simple program that calculates the sum of squares of the first n natural numbers using a for loop.
    
            
    

    