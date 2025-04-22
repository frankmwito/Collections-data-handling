
import csv


def create_file(filename, data):
    # create a new file and write the data to it
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        writer.writerow(["username", "password", "final_grade"])
        writer.writerows(data)
        
        
        
def get_user_input():
    n = int(input("Enter the number of users you want: "))
    data = []
    for i in range(1, n+1):
        username = input(f"Enter your name: {i}") 
        password = input(f"Enter your password: {i} ")   
        final_grade = int(input(f"Enter your grade @ {i}"))
        
        person = [username, password, final_grade]
        data.append(person)
        
    return data
        
def main():
    get_user = get_user_input()
    create_file("test_data.csv", get_user)
    print("File created successfully.")
    
    
if __name__ == "__main__":
    main()