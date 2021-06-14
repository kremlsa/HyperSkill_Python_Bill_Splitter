# write your code here
import random


print("Enter the number of friends joining (including you):")
num_persons = int(input())
print()
if num_persons <= 0:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    persons = {}
    for _ in range(num_persons):
        persons.update({input(): 0})
    print()
    print("Enter the total bill value:")
    bill = input()
    print()
    # print(persons)
    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    choice = input()
    print()
    if choice == "Yes":
        lucky_name = random.choice(list(persons.keys()))
        print("{} is the lucky one!".format(lucky_name))
        bill = round(int(bill) / (num_persons - 1), 2)
        for key in persons:
            new_value = {key: bill}
            if key != lucky_name:
                persons.update(new_value)
    else:
        print("No one is going to be lucky")
        bill = round(int(bill) / num_persons, 2)
        for key in persons:
            new_value = {key: bill}
            persons.update(new_value)
    print(persons)
