"""Q. Program implement Knapsack Algorithm using Greedy Algorithm."""

def Knapsack(s_a: list, W: int) -> tuple:  # function to implement knapsack problem

    total_profit = 0  # a variable to calculate total profit.
    # sorting the passed list of tuples on the basis of profits.
    s_a = sorted(s_a, key=lambda i: i[1], reverse=True)
    result = []

    for item in s_a:  # iterating list.
        if item[0] > W:  # if weight is greater than knapsack size then break.
            break
        # else add total profit.
        total_profit += item[1]
        W -= item[0]   # decreasing knapsack size with weights.
        result.append(item)  # appending the resultant item.

    return (result, total_profit)


# Main code

weights = [10, 19, 3, 5]  # weights
profits = [300,100, 200, 150]  # profits
knapsacksize = 10  # knapsack capacity
# a data model s_a to store list of tuples of weights and profits
s_a = [(weights[i], profits[i]) for i in range(len(weights))]

print(Knapsack(s_a, knapsacksize))