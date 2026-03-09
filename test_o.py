# test.py

def example_function():
    x = 10  # Using the variable to avoid F841
    try:
        print(x)
    except Exception as e:  # Avoid bare except (E722)
        print(f"Error: {e}")


# Add 2 blank lines after function to satisfy E305


example_function()
