"""Q. Program implement Knapsack Algorithm using Greedy Algorithm."""

def Knapsack(sorted_array: list, W: int) -> tuple:  # function to implement knapsack problem

    total_profit = 0  # a variable to calculate total profit.
    # sorting the passed list of tuples on the basis of profits.
    sorted_array = sorted(sorted_array, key=lambda i: i[1], reverse=True)
    result = []

    for item in sorted_array:  # iterating list.
        if item[0] > W:  # if weight is greater than knapsack size then break.
            break
        # else add total profit.
        total_profit += item[1]
        W -= item[0]   # decreasing knapsack size with weights.
        result.append(item)  # appending the resultant item.

    return (total_profit)


# Main code

weights = [10,20,30]  # weights
profits = [60,100,120]  # profits
knapsacksize = 50  # knapsack capacity
# a data model s_a to store list of tuples of weights and profits
sorted_array = [(weights[i], profits[i]) for i in range(len(weights))]

print(Knapsack(sorted_array, knapsacksize))