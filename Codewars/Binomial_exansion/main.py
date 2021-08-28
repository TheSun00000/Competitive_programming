exp ="(2f+4)^6"

x = exp.split("^")

p = int(x[1])

a = x[0].split("")


a = "2f"
b = "4"

res = ""
for i in range(p):
    #calcule a
    if ( "-" in a):
        if i % 2 == 0:res += "+"
        else:res += "-"

    #calcule b

    #sign


def get_digits(s):
    res = ""
    for i in range(len(s)):
        if (!isdigit(s[i])):
            break

    return s[0:i], s[i+1:]
