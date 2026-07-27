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
        UnShot=f"""
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
        print(f"Response: {generateResponse(UnShot, temperature=0.3, maxToken=1024)}")
        print(70*"=")
        FwShot=f"""example1:
                    Category: Fruit
                    Item: Apple
                    Answer: Yes, a Apple is a Fruit

                    example2:
                    Category: City 
                    Item: New York City
                    Answer: Yes, New York City is a City

                    example3:
                    Category: Vehicle 
                    Item: Rose
                    Answer: No, a Rose is not a Vechicle

                    example4:
                    Category: Color 
                    Item: Magenta
                    Answer: Yes, Magenta is a Color

                    example5:
                    Category: Vegetable
                    Item: Strawberry
                    Answer: No, a Strawberry is not a Vegetable
                    
                    example6:
                    Category: Animal
                    Item: Lion
                    Answer: Yes, a Lion is not a Vegetable
                    
                    Now you try:
                    Category: {category}
                    Item: {item}
                    Answer:"""
        print(70*"=")
        print("Few-Shot Learning")
        print(f"Response: {generateResponse(FwShot, temperature=0.3, maxToken=1024)}")
        print(70*"=")
        CrPrompt=f"""Write a 1 Sentence story about the given word
        example1:
        Word: Computer
        Story: The Computer sighed as another cup of coffee was spilled on its keyboard.
        
        example2: 
        Word: Clock
        Story: The Clock ticked loudly, racing against the students as they frantically finished their exam.
        
        Word: {item}
        Story:"""
        print(70*"=")
        print("Creative-Shot Learning")
        print(f"Response: {generateResponse(CrPrompt, temperature=0.3, maxToken=1024)}")
        print(70*"=")
run()