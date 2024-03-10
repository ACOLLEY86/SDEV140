"""
Pizza Ordering App
Anthony Colley's Final Version 3/9/2024
This program is a simple pizza ordering system built using Tkinter in Python. 
It allows users to place orders for pizzas, customize them with various toppings, 
    and optionally add breadsticks. The program calculates the total price of the order, 
    including tax, and displays a receipt with the order summary. 
Users can choose between dine-in and take-out options, select pizza sizes, toppings, 
    and finalize their orders through the intuitive graphical user interface.
"""

# Importing the tkinter module and the messagebox submodule
import tkinter as tk
from tkinter import messagebox

# Defining the PizzaOrderApp class
class PizzaOrderApp:
    # Constructor method to initialize the application
    def __init__(self, root):
        # Initializing the root window
        self.root = root
        # Setting the title of the window
        self.root.title("Pizza Order System")
        # Loading the background image for the application with alternate text
        self.background_image = tk.PhotoImage(file="ingredients.png").subsample(2)
        # Variable to hold the total price of the order
        self.total_price_var = tk.StringVar()
        # Variable to hold the selected pizza size
        self.selected_size = tk.StringVar()
        # List to hold the selected toppings
        self.selected_toppings = []
        # Variable to hold the selection of breadsticks
        self.breadsticks_var = tk.IntVar()
        # Creating the home screen for the application
        self.create_home_screen()
    
    # Method to create the home screen
    def create_home_screen(self):
        # Clearing all widgets from the screen
        self.clear_widgets()
        # Resetting the total price to zero
        self.total_price_var.set("$0.00")
        # Displaying the background image covering the full screen
        bg_label = tk.Label(self.root, image=self.background_image)
        bg_label.place(relx=0, rely=0, relwidth=1, relheight=1)
        # Displaying the title label
        title_label = tk.Label(self.root, text="Welcome to Colley's Pizzeria!", font=("Arial", 24), bg="white")
        title_label.pack(pady=20)
        # Button to start a dine-in order
        dine_in_button = tk.Button(self.root, text="Dine-In", command=self.start_order_dine_in, font=("Arial", 18))
        dine_in_button.pack(pady=10)
        # Button to start a take-out order
        take_out_button = tk.Button(self.root, text="Take-Out", command=self.start_order_take_out, font=("Arial", 18))
        take_out_button.pack(pady=10)

    # Method to start a dine-in order
    def start_order_dine_in(self):
        # Clearing all widgets from the screen
        self.clear_widgets()
        # Resetting the total price to zero
        self.total_price_var.set("$0.00")
        # Displaying the background image covering the full screen
        bg_label = tk.Label(self.root, image=self.background_image)
        bg_label.place(relx=0, rely=0, relwidth=1, relheight=1)
        # Displaying the title label for a dine-in order
        title_label = tk.Label(self.root, text="Dine-In Order", font=("Arial", 24), bg="white")
        title_label.pack(pady=20)
        # Starting the pizza order process
        self.start_order()

    # Method to start a take-out order
    def start_order_take_out(self):
        # Clearing all widgets from the screen
        self.clear_widgets()
        # Resetting the total price to zero
        self.total_price_var.set("$0.00")
        # Displaying the background image covering the full screen
        bg_label = tk.Label(self.root, image=self.background_image)
        bg_label.place(relx=0, rely=0, relwidth=1, relheight=1)
        # Displaying the title label for a take-out order
        title_label = tk.Label(self.root, text="Take-Out Order", font=("Arial", 24), bg="white")
        title_label.pack(pady=20)
        # Starting the pizza order process
        self.start_order()

    # Method to start the pizza order process
    def start_order(self):
        # Clearing previous order selections
        self.selected_size.set("")  # Clear pizza size selection
        self.selected_toppings.clear()  # Clear selected toppings
        self.breadsticks_var.set(0)  # Clear breadsticks selection
        self.calculate_total_price()  # Recalculate total price
        # Creating a frame for pizza sizes selection
        size_frame = tk.Frame(self.root, bg="white")
        size_frame.pack(pady=10)
        # Displaying pizza sizes and their prices
        for size, price in self.sizes.items():
            size_label = tk.Label(size_frame, text=f"{size} (${price:.2f})", font=("Arial", 18), bg="white")
            size_label.grid(row=0, column=len(size_frame.winfo_children()))
            size_image = tk.PhotoImage(file=f"pizza.png").subsample(2)  # Resize the image with alternate text
            size_button = tk.Button(size_frame, image=size_image, command=lambda s=size: self.select_size(s))
            size_button.image = size_image
            size_button.grid(row=1, column=len(size_frame.winfo_children())-1)
        # Label for selecting toppings
        toppings_label = tk.Label(self.root, text="Select Toppings:", font=("Arial", 18))
        toppings_label.pack()
        # Creating two rows of topping checkboxes
        toppings_frame = tk.Frame(self.root, bg="white")
        toppings_frame.pack()
        row = 0
        column = 0
        for topping, price in self.toppings.items():
            topping_check = tk.Checkbutton(toppings_frame, text=f"{topping} (${price:.2f})", font=("Arial", 14), variable=tk.BooleanVar(), command=lambda t=topping: self.toggle_topping(t))
            topping_check.grid(row=row, column=column, sticky="w", padx=10, pady=5)
            column += 1
            if column == 2:
                column = 0
                row += 1
        # Checkbox for adding breadsticks option
        breadsticks_check = tk.Checkbutton(self.root, variable=self.breadsticks_var, text="Add 6 Breadsticks ($3.99)", font=("Arial", 14), command=self.toggle_breadsticks)
        breadsticks_check.pack()
        # Label to display the total price of the order
        total_price_display = tk.Label(self.root, textvariable=self.total_price_var, font=("Arial", 18), fg="green")  # Total price in green
        total_price_display.pack(pady=20)
        # Button to proceed to checkout
        checkout_button = tk.Button(self.root, text="Checkout", command=self.checkout, font=("Arial", 18))
        checkout_button.pack(pady=10)
        # Button to reset and go back to the main screen
        reset_button = tk.Button(self.root, text="Reset", command=self.create_home_screen, font=("Arial", 18))
        reset_button.place(relx=0.05, rely=0.05, anchor="nw")

    # Method to select the pizza size
    def select_size(self, size):
        self.selected_size.set(size)
        self.calculate_total_price()
    
    # Method to toggle topping selection
    def toggle_topping(self, topping):
        # Check if the topping is already selected
        if topping in self.selected_toppings:
            # If it is selected, remove it
            self.selected_toppings.remove(topping)
        else:
            # If it is not selected, add it
            self.selected_toppings.append(topping)
        # Recalculate the total price after toggling topping selection
        self.calculate_total_price()

    # Method to toggle breadsticks selection
    def toggle_breadsticks(self):
        # Recalculate the total price after toggling breadsticks selection
        self.calculate_total_price()

    # Method to calculate the total price of the order
    def calculate_total_price(self):
        # Initialize total price
        total_price = 0
        # Get the price of the selected pizza size, default to 0 if not found
        size_price = self.sizes.get(self.selected_size.get(), 0)
        # Add the price of the pizza size to the total price
        total_price += size_price
        # Add the price of each selected topping to the total price
        for topping in self.selected_toppings:
            total_price += self.toppings.get(topping, 0)
        # Add the price of breadsticks if selected
        if self.breadsticks_var.get():
            total_price += 3.99
        # Update the total price variable with the calculated value
        self.total_price_var.set(f"${total_price:.2f}")

    # Method to handle checkout process
    def checkout(self):
        # Validate if a pizza size is selected before checkout
        if not self.selected_size.get():
            # If no pizza size is selected, show an error message
            tk.messagebox.showerror("Error", "Please select a pizza size before checkout.")
        else:
            # If a pizza size is selected, proceed to display the receipt
            self.display_receipt()

    # Method to display the receipt
    def display_receipt(self):
        # Extract the total price from the total price variable
        total_price = float(self.total_price_var.get()[1:])
        # Calculate the tax amount (7%)
        tax = total_price * 0.07
        # Calculate the total price including tax
        total_price_with_tax = total_price + tax
        
        # Construct the receipt text
        receipt_text = f"Order Summary\n\n"
        receipt_text += f"Size: {self.selected_size.get()}\n"
        receipt_text += f"Toppings: {', '.join(self.selected_toppings)}\n"
        if self.breadsticks_var.get():
            receipt_text += "Breadsticks: Yes\n"
        receipt_text += f"Total Price: ${total_price:.2f}\n"
        receipt_text += f"Tax (7%): ${tax:.2f}\n"
        receipt_text += f"Total Price with Tax: ${total_price_with_tax:.2f}\n\n"
        receipt_text += "Thank you for your order!"

        # Show the receipt message box with the constructed text
        tk.messagebox.showinfo("Receipt", receipt_text)

        # Reset to the main screen after displaying the receipt
        self.create_home_screen()

    # Method to clear all widgets from the screen
    def clear_widgets(self):
        # Destroy all widgets in the root window
        for widget in self.root.winfo_children():
            widget.destroy()

    # Pizza sizes and their prices
    sizes = {"Small": 8.99, "Medium": 10.99, "Large": 12.99}
    # Pizza toppings and their prices
    toppings = {"Pepperoni": 1.50, "Mushrooms": 1.00, "Onions": 1.00, "Sausage": 1.50, "Bacon": 1.50, "Extra Cheese": 1.00}

# Main function to initialize the application
def main():
    # Create a Tkinter root window
    root = tk.Tk()
    # Set window size to 1200x800
    root.geometry("1200x800")
    # Initialize the PizzaOrderApp instance with the root window
    app = PizzaOrderApp(root)
    # Start the Tkinter event loop
    root.mainloop()

# Check if the script is being run directly
if __name__ == "__main__":
    # If so, call the main function to start the application
    main()