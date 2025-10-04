
s=input("ENTER STRING\n")

def Non_repeating_second_Char(s):
    for char in s:
        if s.count(char) == 1:
         print(char)
         break
    return None

Non_repeating_second_Char(s)