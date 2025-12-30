# Importing necessary libraries for GUI, message boxes, and image handling
# - tkinter: for creating the GUI components
# - messagebox: to show alert popups
# - PIL (Python Imaging Library): to handle image loading and resizing

# Setting up the Main Window (root window)
# - Define window title
# - Set background color
# - Define window size (width x height)

# Adding Image and Labels in the Main Window
# - Open the image file
# - Resize the image to fit within the window
# - Convert the image for Tkinter display
# - Create a label to hold the image and place it on the window
# - Add a text label welcoming the user and position it at the bottom center

# Function to display a messagebox when the user clicks the button
# - Displays an alert asking if the user wants to calculate denominations
# - If the user clicks OK, it calls the function to open the top window

# Adding a button to the main window
# - The button text says "Let's get started!"
# - When clicked, it triggers the messagebox function
# - The button is styled with background and foreground colors
# - Positioned near the bottom of the main window

# Function for opening a new Top-Level Window
# - This acts as a secondary window where calculations happen
# - Set title, background color, and size for the new window

# Adding labels and entry fields in the top window
# - A label asking the user to enter the total amount
# - An entry box where the user types the total amount
# - A label explaining that the next section will show the number of notes
# - Labels and text fields for ₹2000, ₹500, and ₹100 notes

# Nested function to perform the denomination calculation
# - Fetch the entered amount and convert it to an integer
# - Divide the amount to find how many ₹2000 notes are needed
# - Use modulus (%) to find the remaining amount
# - Repeat for ₹500 and ₹100 notes
# - Clear previous results in the text boxes
# - Display the calculated results in the respective entry boxes
# - If input is invalid (non-numeric), show an error message

# Adding a "Calculate" button
# - Triggers the calculator function
# - Styled with brown background and white text

# Placing all widgets (labels, buttons, and entries) at specific coordinates
# - Arranging components neatly for readability and usability

# Starting the Tkinter main event loop for both windows
# - Ensures the GUI remains open and responsive
