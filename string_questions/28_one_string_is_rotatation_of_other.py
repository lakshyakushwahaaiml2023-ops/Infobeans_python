def check_rotation(str1, str2):
    return (str2 in (str1+str1)) and (len(str1) == len(str2))

str1 = "abab"
str2 = "babab"

print(f"{str2} is rotatation of {str1} : {check_rotation(str1, str2)}")