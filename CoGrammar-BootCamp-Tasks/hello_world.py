# My name is Gower Campbell and this is based on my first submission using VCS as 
# part of getting started with the bootcamp!!!

# I learned that you can store information that the user inputs into 
# my code as a string. Made sure to cast the 'age' as an integer.

# I can then output that information alongside the 'print' command.
# Using the format ".format()" function, which will add 'age' as part of my 
# string's message.

def get_user_info():
    """Get the user's name and age."""
    name = input("\nPlease can I have your name: ")

    # Handle invalid age input
    while True:
        try:
            age = int(input("And your age: "))
            break  # Exit the loop if age is valid
        except ValueError:
            print("Oops! That doesn't look like a valid age. Please enter a number.")

    return name, age


def display_welcome_message(name, age):
    """Display a welcome message using the user's name and age."""
    print("\nHello, World!")
    print(f"\nYou've written some awesome code, {name}! It's nice to meet you...")
    print(f"\nYour age is... {age} I was only just coded now!!")
    print("\nWelcome to Cogrammar's Bootcamp!!")


def ask_favorite_language():
    """Ask the user for their favorite programming language."""
    favorite_language = input("\nWhat's your favorite programming language? ")
    print(f"\nWow, {favorite_language} is a great choice!")


def main():
    """Main function to run the program."""
    print("Welcome to Gower's Python Script!\n")

    # Get user info
    name, age = get_user_info()

    # Display welcome message
    display_welcome_message(name, age)

    # Ask about favorite programming language
    ask_favorite_language()

    print("\nThank you for using this program. Code well!\n")


# Run the program
if __name__ == "__main__":
    main()
