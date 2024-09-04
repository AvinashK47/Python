def divide_numbers():
    try:
        # Ask the user for two numbers
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))

        # Perform division
        result = num1 / num2

    except ValueError:
        # Handle ValueError if the input cannot be converted to an integer
        print("Error: Please enter valid integers.")

    except ZeroDivisionError:
        # Handle ZeroDivisionError if the second number is zero
        print("Error: Division by zero is not allowed.")

    except Exception as e:
        # Handle any other unexpected exceptions
        print(f"Unexpected Error: {e}")

    else:
        # Executes if no exceptions occurred
        print(f"Result of {num1} / {num2} = {result:.2f}")

    finally:
        # Executes regardless of whether an exception occurred or not
        print("Execution completed.")

# Call the function to execute the code
divide_numbers()
