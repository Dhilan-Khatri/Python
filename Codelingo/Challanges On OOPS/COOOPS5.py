class RoConvert:
    def __init__(self, number):
        self.number = number

    def roman(self):
        values = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]
        num = self.number
        roman = ""
        for value, symbol in values:
            while num >= value:
                roman += symbol
                num -= value
        return roman

x = int(input("Enter an integer: "))

converter = RoConvert(x)
print(f"The Roman Numeral is {converter.roman()}")