# Load the electoral college data
states = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "District of Columbia", "Florida",
          "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts",
          "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico",
          "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina",
          "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]

votes_1964 = [10,3,5,6,40,6,8,3,3,14,12,4,4,26,13,9,7,9,10,4,10,14,21,10,7,12,4,5,3,4,17,4,43,13,4,26,8,6,29,4,8,4,11,25,4,3,12,9,7,12,3]
votes_1972 = [9,3,6,6,45,7,8,3,3,17,12,4,4,26,13,8,7,9,10,4,10,14,21,10,7,12,4,5,3,4,17,4,41,13,3,25,8,6,27,4,8,4,10,26,4,3,12,9,6,11,3]
votes_1984 = [9,3,7,6,47,8,8,3,3,21,12,4,4,24,12,8,7,9,10,4,10,13,20,10,7,11,4,5,4,4,16,5,36,13,3,23,8,7,25,4,8,3,11,29,5,3,12,10,6,11,3]
votes_1992 = [9,3,8,6,54,8,8,3,3,25,13,4,4,22,12,7,6,8,9,4,10,12,18,10,7,11,3,5,4,4,15,5,33,14,3,21,8,7,23,4,8,3,11,32,5,3,13,11,5,11,3]
votes_2004 = [9,3,10,6,55,9,7,3,3,27,15,4,4,21,11,7,6,8,9,4,10,12,17,10,6,11,3,5,5,4,15,5,31,15,3,20,7,7,21,4,8,3,11,34,5,3,13,11,5,10,3]
votes_2012 = [9,3,11,6,55,9,7,3,3,29,16,4,4,20,11,6,6,8,8,4,10,11,16,10,6,10,3,5,6,4,14,5,29,15,3,18,7,7,20,4,9,3,11,38,6,3,13,12,5,10,3]
votes_2024 = [9,3,11,6,54,10,7,3,3,30,16,4,4,19,11,6,6,8,8,4,10,11,15,10,6,10,4,5,6,4,14,5,28,16,3,17,7,8,19,4,9,3,11,40,6,3,13,12,4,10,3]
all_votes = [(votes_1964, 1964), (votes_1972, 1972), (votes_1984, 1984), (votes_1992, 1992), (votes_2004, 2004), (votes_2012, 2012), (votes_2024, 2024)]


def calc_votes(votes):
    n = len(votes)
    # Initialize a 2D array to store the solutions
    dp = [[0 for j in range(538 + 1)] for i in range(n + 1)]
    # Base case: if the target is 0, there is exactly one way to achieve it (by selecting an empty subset)
    for i in range(n + 1):
        dp[i][0] = 1
    # Fill in the rest of the array using the recurrence relation
    for i in range(1, n + 1):
        for j in range(1, 538 + 1):
            # If the i-th element is greater than the target j, exclude it
            if votes[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                # Otherwise, consider both including and excluding the i-th element
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - votes[i - 1]]
    # Count the number of ways to get a 269-269 tie
    count = 0
    for i in range(1, n + 1):
        if votes[i - 1] <= 269:
            count += dp[i - 1][269 - votes[i - 1]]
        if votes[i - 1] >= 269:
            count += dp[i - 1][269 + 538 - votes[i - 1]]
    return count


for votes, year in all_votes:
    print(f'{year}: {calc_votes(votes)}')