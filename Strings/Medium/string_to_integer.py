#Time Complexity : O(n)
def string_to_integer(s):
    n = len(s)
    i=0
    while i < n and s[i]==' ':
        i+=1
    sign = 1
    if i < n and (s[i]=='+' or s[i]=='-'):
        if s[i]== '-':
            sign = -1
        i+=1
    num=0
    while i<n and s[i].isdigit():
        num = num*10 + int(s[i])

        if sign * num <= -2**31:
            return -2**31
        if sign * num >= 2**31-1:
            return 2**31 - 1
        i+=1
    return sign * num

def main():

    s = "1337c0d3"
    print(string_to_integer(s))
main()


    
