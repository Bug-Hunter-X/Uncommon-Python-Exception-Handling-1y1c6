def function_with_uncommon_error(x):
    try:
        result = 10 / x
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: Cannot divide by zero.")
        return 0 # Or raise a custom exception
    except TypeError:
        print("Caught TypeError: Invalid input type.")
        return None
    except Exception as e:
        print(f"Caught an unexpected error: {type(e).__name__} - {e}")
        return None
    return result

# Example usage:
print(function_with_uncommon_error(2))  # Output: 5.0
print(function_with_uncommon_error(0))  # Output: Caught ZeroDivisionError: Cannot divide by zero.
0
print(function_with_uncommon_error("abc")) # Output: Caught TypeError: Invalid input type.
None
print(function_with_uncommon_error(1)) #Output: 10.0