# Python3 code to demonstrate working of
# Get matching substrings in string
# Using lambda and filter()
  
# initializing string 
test_str = "GfG is good website"
  
# initializing potential substrings
test_list = {"Gf", "site", "CS", "Geeks", "Tutorial" }
  
# printing original string 
print("The original string is : " + test_str)
  
# printing potential strings list
print("The original list is : " + str(test_list))
  
# using lambda and filter()
# Get matching substrings in string
res = list(filter(lambda x:  x in test_str, test_list))
  
# printing result 
print("G" in test_list)