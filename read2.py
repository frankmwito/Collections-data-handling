# read a json file
import json


def readfile(filename):
    with open(filename, mode = 'r') as file:
        data1 = json.load(file)
        
        for info in data1:
            print(info["username"], info["password"], info["final_grade"])
        return data1
    
if __name__ == "__main__":
    readfile("test_data.json")