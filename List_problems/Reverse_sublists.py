# Reverse Sublists
"""Given a list nums = [1, 2, 3, 4, 5, 6, 7, 8], reverse every sublist of size k=3
Output: [3, 2, 1, 6, 5, 4, 8, 7]"""

def reverse_list():
    l1 = [1, 2, 3, 4, 5, 6, 7, 8]
    l2 = []
    k = 3
    for i in range(0, len(l1), k):
        l2.extend(l1[i:i+k][::-1])
        print(l2)

if __name__=="__main__":
    reverse_list()