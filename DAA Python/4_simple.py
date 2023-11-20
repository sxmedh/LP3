def solve_knapsack():
    profit = [1, 2, 5, 6]  # value array
    weight = [2, 3, 4, 5]  # Weight array
    capacity = 8
    rows = 5
    cols = 9

    # Initialize a 2D array filled with zeros
    array = [[0 for _ in range(cols)] for _ in range(rows)]


    for i in range(1, rows):
        for j in range(0, cols):
            if j - weight[i-1] >= 0:
                array[i][j] = max(array[i - 1][j], array[i - 1][j - weight[i - 1]] + profit[i - 1])
            else:
                array[i][j] = array[i - 1][j]

    selected_items = []
    i, j = rows - 1, capacity
    while i > 0 and j > 0:
        if array[i][j] != array[i - 1][j]:
            selected_items.append(weight[i - 1])
            j -= weight[i - 1]
        i -= 1

    # Print the total value and weights of the selected items
    total_value = array[rows - 1][capacity]
    print("Total Value:", total_value)
    print("Weights of Items Taken:", selected_items)


if __name__ == "__main__":
    solve_knapsack()