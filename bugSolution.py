def function_with_uncommon_error_solution(a, b):
    if a == 0 or b == 0:
        return 0 # Handle the case of division by zero gracefully
    else:
        return a / b