import module_1

name = input("Type in your name: ")
name_length = len(name)
print("The length of your name is %s"%name_length)
def vowel(character):
    a = name.count(character)
    print(character,"appears",a,"times")
    return
vowel("a")
vowel("e")
vowel("i")
vowel("o")
vowel("u")

