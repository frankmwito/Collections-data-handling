# Count vowel in a string

class VowelCount:
    def __init__(self, word):
        self.word = word
        self.count = 0
        
    def calculate_vowels(self):
        for ch in self.word:
            if ch.lower() in 'aeiou':
                self.count += 1
                
                
def get_user_input():
    while True:
        try:
            word = input("Enter any choice of word: ")
            word.lower()
            if word != str:
                return word
            else:
                print("Please enter words or characters")
        except ValueError:
            print("Invalid input:")     
            
            
def main():
    word = get_user_input()
    vowel = VowelCount(word)
    vowel.calculate_vowels()
    print(f"The vowel count of {word} is: {vowel.count}")
    
    
if __name__=="__main__":
    main()