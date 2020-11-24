def fact(n):
    if n == 0:
        return 1
    return n*fact(n-1)

def reverse_string(str):
    letters = len(str)
    if(letters==0):
        return

    last_letter = str[letters-1]
    print(last_letter,end = "")
    reverse_string(str[0:letters-1])

reverse_string("drahffutssiht")