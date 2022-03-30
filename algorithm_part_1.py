# Number 1:

# def first_and_last(word):
#     first_letter = word[0]
#     last_letter = word[-1]
#     together = first_letter + last_letter
#     print(together)
#     return together

# first_and_last(input("What would you like for the example?"))


# Number 2:

# def pbj():
#     for number in range(0,101):
 
#         if number % 5 == 0 and number % 3 == 0:
#             print('Peanutbutter and Jelly')
#         elif number % 3 ==0:
#             print('Peanutbutter')
#         elif number % 5 ==0:
#             print('Jelly')
#         else:
#             print(number)


# pbj()


# Number 3:
# def scrambler(word):
#     for letter in word:
#         letter
    
#     for letter in word:
#         letter_list = [letter]
#         print(letter_list)
#         indexes = len(word)
#         print(indexes)
# pass

# scrambler("devCodeCamp")



#Number 4:

def search_ingredient(ingredients):
    search = input("What would you like to find today?")
    for item in ingredients:
             print(search)
             print(item)
             if search == item:
                 print("Hooray!")
                 return item
    else:
        try_again = input("Sorry, we couldn't find what you were looking for.  Would you like to try again?")
        if try_again == "Y":
            search_ingredient(["Eggs", "Butter", "Onions", "Cream", "Ketchup"])
        if try_again != "Y":
            print("Thank you for shopping with us!")
            


print(search_ingredient(["Eggs", "Butter", "Onions", "Cream", "Ketchup"]))