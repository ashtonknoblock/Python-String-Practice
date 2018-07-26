def to_camel_case(string):
    if "-" in string:
        word = string.split('-')
        return word[0] + ''.join(x.title() for x in word[1:])
    if "_" in string:
        word = string.split('_')
        return word[0] + ''.join(x.title() for x in word[1:])

to_camel_case("ashton-knoblock")


def find_nth_occurrence(word, string, occurrence_number):
    print(string)

find_nth_occurrence("example", "This is an example. Return the nth occurrence of example in this example string.", 1)