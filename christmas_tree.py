# christmas tree

# """For a given number n, print a christmas tree made of stars (*) with n rows.""""

class ChristmasTree:
    def __init__(self, n):
        self.n = n
        
    def print_tree(self):
        # print the top part of the tree
        for i in range(1, self.n + 1):
            print('' * (self.n - i) + '*' * (2 * i - 1))
          

def get_user_input():
    while True:
        try:
            n = int(input("Enter the number of rows for the christmas tree: "))
            if n > 0:
                return n
            else:
                print("please enter a positive integer.")
        except ValueError:
            print("Invalid input. please enter a positive integer.")
        
        
        
def main():
    n = get_user_input()
    tree = ChristmasTree(n)
    tree.print_tree()
    
    
    
if __name__ == "__main__":
    main()