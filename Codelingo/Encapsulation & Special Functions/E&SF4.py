class reverse:
    def __init__(self, s=""):
        self.s = s

    def reversed_string(self):
        return self.s[::-1]

word = input("Enter a word: ")
rev = reverse(word)

print("Reversed string:", rev.reversed_string())
