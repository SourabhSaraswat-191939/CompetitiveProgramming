def find_palindromes_in_sub_string(input, j, k, palindromeSet):
    while j >= 0 and k < len(input):
        if (input[j] != input[k]):
            break

        palindromeSet.add(input[j: k + 1])

        j -= 1
        k += 1


def find_all_palindrome_substrings(input):
    palindromes = set()
    for i in range(0, len(input)):
        find_palindromes_in_sub_string(input, i - 1, i + 1,palindromes)
        find_palindromes_in_sub_string(input, i, i + 1,palindromes)

    print("Your required palindromes of length > 2 => ")
    count = 0
    for val in palindromes:
        if len(val)>2:
            print(val)
            count+=1
    return count


s = input("Enter the string to find the palindrome of => ")

print("Total palindrome substrings of length > 2 => ", find_all_palindrome_substrings(s))