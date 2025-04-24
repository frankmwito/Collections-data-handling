import json

def create_file(filename, data):
    with open(filename, mode= 'w') as file:
       json.dump(data, file, indent=4)
   
              
       
def get_user_input():
    n = int(input("Enter the number of users you want: "))
    data = []
    for i in range(1, n + 1):
        username = input(f"Enter your name @{i}:")
        password = input(f"Enter your password @{i}:")
        final_grade = int(input(f"Enter your grade @{i}:"))
        
        person = {
            "username": username,
            "password": password,
            "final_grade": final_grade
        }
        
        data.append(person)
    return data

def main():
    get_user = get_user_input()
    create_file("test_data.json", get_user)
    print("file created successfully.")
    
if __name__ == "__main__":
    main()
    
           
                