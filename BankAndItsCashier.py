# Bank and its Cashier
# A customer comes to withdraw money from a bank. Unfortunately, that day the bank only has two types of currency notes to give: 1 unit and 2 unit. The manager, being amused by the incident, tried to have some fun and decided to create a challenge for the cashier team. She asked the team to minimize the difference between the number of the two types of currency notes. The manager also asked you to give her your solution. You decided to use computational power.What would be your solution?

# Constraints
# Only 1 and 2 unit currency notes are used.
# 0 <= input integer < 109
# Input Format
# Integer (possibly very large): Amount customer wants to withdraw

# Output Format
# Single integer: Total number of notes
# Do not print Debug Statements while submitting the solution.

# Examples
# Input            |   Output [num1+num2]
# 1000             |   667           Explanation : 1*334 + 2*333 = 1000
# 1                |   1
# 32               |   21



def sol(n):
    two = n/4
    one = int(n/2)
    if two%1==0:
        two = int(two)
    elif two%1>=0.5:
        two = int(two) + 1
        # one -= 1
    else:
        two = int(two)
        one = one+1
    
    diff = (one-two)/3
    # two += diff/3
    if diff%1==0:
        two += diff
        one += diff*2
    elif diff%1>=0.5:
        two += int(diff) + 1
        one -= (int(diff) + 1)*2
    else:
        two += int(diff)
        one -= (int(diff))*2

    return one + two
   

# do not edit below code
def main():
    n=int(input())
    print(sol(n))

if __name__ == '__main__':
    main()