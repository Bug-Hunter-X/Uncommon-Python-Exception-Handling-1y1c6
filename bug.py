def function_with_uncommon_error(x):
    try:
        result = 10 / x
    except ZeroDivisionError:
        print("Caught ZeroDivisionError")
        return None
    except TypeError:
        print("Caught TypeError")
        return None
    except Exception as e:
        print(f"Caught an unexpected error: {e}")
        return None
    return result

# Example usage:
print(function_with_uncommon_error(2))  # Output: 5.0
print(function_with_uncommon_error(0))  # Output: Caught ZeroDivisionError
None
print(function_with_uncommon_error("abc")) # Output: Caught TypeError
None
print(function_with_uncommon_error(1)) #Output: 10.0