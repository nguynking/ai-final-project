def backtracking(values, weights, max_weight): 
    """Returns the best set of items that maximize the total values within weight constraint.
    Each item in the set is represented by either 1 (the item is chosen) or 0 (the item is not chosen).
    (Model)

    Args:
    values (list[float]): List of values
    weights (list[float]): List of weights
    max_weight (float): The weight constraint

    Returns: 
    max_val (float): The total values of the best set
    best_set (list[int]): The best set of items
    """
    values = split(values)
    weights = split(weights)
    max_weight = split(max_weight)
    
    total_items = len(values)
    max_val = 0
    best_set = None
    # Initialize all items to be 0 (not in knapsack)
    current_option = [0] * total_items
    
    def backtrack(i, current_value, current_weight):
        nonlocal max_val, best_set
        if current_weight > max_weight: 
            return
        if i == total_items:
            if current_value > max_val:
                max_val = current_value
                best_set = current_option[:]
        else:
            # Set the current item to be 1 (in knapsack) and continue to recurse
            current_option[i] = 1
            backtrack(i + 1, current_value + values[i], current_weight + weights[i])
            # Set the current item to be 0 (not in knapsack) and continue to recurse
            current_option[i] = 0
            backtrack(i + 1, current_value, current_weight)
            
    backtrack(0, 0, 0)
    return max_val, best_set
