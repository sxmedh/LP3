def solve_knapsack():
    p = [1, 2, 6, 5]  # value array
    w = [2, 3, 5, 4]  # Weight array
    capacity = 8
    rows = len(p) + 1
    cols = capacity + 1

    # Initialize a 2D array filled with zeros
    array = [[0 for _ in range(cols)] for _ in range(rows)]

    items = sorted(zip(p, w), key=lambda x: x[1])

    for i in range(1, rows):
        for c in range(0, cols):
            if items[i - 1][1] <= c:
                array[i][c] = max(array[i - 1][c], array[i - 1][c - items[i - 1][1]] + items[i - 1][0])
            else:
                array[i][c] = array[i - 1][c]

    selected_items = []
    i, c = rows - 1, capacity
    while i > 0 and c > 0:
        if array[i][c] != array[i - 1][c]:
            selected_items.append(items[i - 1])
            c -= items[i - 1][1]
        i -= 1

    # Print the total value and weights of the selected items
    total_value = array[rows - 1][capacity]
    print("Total Value:", total_value)
    print("Weights of Items Taken:", [item[1] for item in selected_items])


if __name__ == "__main__":
    solve_knapsack()

