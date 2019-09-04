# Script to output a centered header
# Prompts for both total desired length
# and the title to be centered.

desired_title = input("Enter the desired title: ")
desired_length = int(input("Enter the desired length of the header: "))

if desired_length <= len(desired_title):
    print("The line length must be longer than the length of the desired title!")
else
    title_length = len(desired_title)
    num_of_dashes = (desired_length - title_length - 2)  # -2 to account for space on either side of title

    # Constructing the number of dashes before the title (half of them with integer division)
   before = "-" * num_of_dashes // 2

    # Getting the string after. Need to be careful to get the length right in case the title can't be PERFECTLY centered
    after = "-" * (desired_length - title_length - 2 - len(before)

    # Constructing our full message (before, middle, and after)
    fullmessage = before + " " + desired_title + " "

    print(fullmessage)
