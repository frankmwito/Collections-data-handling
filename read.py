import csv

def read_file(filename):
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        data = list(reader)
        
    return data

def main():
    filename = "test_data.csv"
    data = read_file(filename)
    print(f"File conntents: {data}")
    
    
if __name__ == "__main__":
    main()