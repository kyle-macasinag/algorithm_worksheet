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
    for item in ingredients:
             search = input("What would you like to find today?")
             print(search)
             print(item)
             if search == item:
                 return item
             elif search != item:
                 feedback = input("Apologies, nothing came up. Would you like to try agin? Y/N:")
                 if feedback == "Y":
                     print("Let's try again!")

                 elif feedback != "Y":
                     print("Have a nice day!")
                     quit


   
search_ingredient()