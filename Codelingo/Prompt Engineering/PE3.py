from groq import generateResponse

def run():
    print("Zero-Shot, One-Shot, and Multi-Shot Learning Activity")
    category=input("Enter a category (City, Food, Animals): ").strip()
    item=input(f"Enter a specific {category} to classify: ").strip()
    if not category or not item:
        print(f"Please fill in both fields to run the activity.")
        return
    else:
        ZrShot=f"Is {item} a {category}; answer yes or no"
        print(70*"=")
        print(f"Zero-Shot Learning: ")
        print(f"Response: {generateResponse(ZrShot, temperature=0.3, maxToken=1024)}")
        print(70*"=")
        OneShot=f"""
                example:
                Category: Fruit
                Item: Apple
                Answer: Yes, Apple is a Fruit
                
                Now you try:
                Category: {category}
                Item: {item}
                Answer:"""
        print(70*"=")
        print("One-Shot Learning")
        print(f"Response: {generateResponse(OneShot, temperature=0.3, maxToken=1024)}")
        print(70*"=")
        FewShot=f"""example1:
                    Category: Fruit
                    Item: Apple
                    Answer: Yes, Apple is a Fruit

                    example2:
                    Category: City 
                    Item: New York City
                    Answer: Yes, New York City is a City

                    example3:
                    Category: Vehicle 
                    Item: Rose
                    Answer: No, Rose is not a Vechicle

                    example4:
                    Category: Color 
                    Item: Magenta
                    Answer: Yes, Magenta is a Color

                    example5:
                    Category: Vegetable
                    Item: Strawberry
                    Answer: No, Strawberry is not a Vegetable
                    
                    Now you try:
                    Category: {category}
                    Item: {item}
                    Answer:"""
        print(70*"=")
        print("Few-Shot Learning")
        print(f"Response: {generateResponse(FewShot, temperature=0.3, maxToken=1024)}")
        print(70*"=")
        CrPrompt=f"""Write a 1 Sentence story about the given word
        example1:
        Word: Moon
        Story: The Moon winked at the lovers as they were together
        
        Word: {item}
        Story:"""
        print(70*"=")
        print("Creative-Shot Learning")
        print(f"Response: {generateResponse(CrPrompt, temperature=0.3, maxToken=1024)}")
        print(70*"=")
        FwShot=f"""Example1:
        Category: Devices
        Item: Laptop
        Answer: Yes, a Laptop is a Device

        Example2:
                Category: Devices
                Item: Headphones
                Answer: Yes, a Headphone is a Device

        Category: {category}
        Item: {item}
        Answer: """
        print(70*"=")
        print("Few1-Shot Learning")
        print(f"Response: {generateResponse(FwShot, temperature=0.3, maxToken=1024)}")
        print(70*"=")
run()