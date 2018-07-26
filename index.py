def to_camel_case(string):
    if "-" in string:
        word = string.split('-')
        return word[0] + ''.join(x.title() for x in word[1:])
    if "_" in string:
        word = string.split('_')
        return word[0] + ''.join(x.title() for x in word[1:])

print ("The case of Camel-----------------------------------:")
print to_camel_case("ashton-knoblock")
print to_camel_case("Kenzie_academy_rocks")


# def find_nth_occurrence(word, string, occurrence_number):
#     print(string)
# find_nth_occurrence("example", "This is an example. Return the nth occurrence of example in this example string.", 1)


def rollin(string):
    bumps = 0
    for letter in string:
        if letter is "n":
            bumps += 1
    if bumps >= 15: 
        return "Car Dead"
    else:
        return "Woohoo!"
print ("Keep it Rollin-----------------------------------:")
print rollin("__n__nnn_nn_nn_nn_nnnnnn")
print rollin("__n_n__nnn_nnn_n")


def backwards(string):
    return string[::-1]

print ("Reverse the Words-----------------------------------:")
print backwards("Hopefully this shows up backwards!")
print backwards("Hannah's Racecar is wow")
