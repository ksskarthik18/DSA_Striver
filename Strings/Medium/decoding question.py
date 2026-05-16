def decode():
    n = int(input())
    msg = input().strip()

    if msg == "" or msg == "NULL":
        print("NULL")
    else:
        arr = msg.split()
        ans =""
        i = 0
        while i < len(arr):
            if arr[i] == "_":
                ans+=" "
            elif arr[i] == "@":
                ans += "@"
            elif arr[i] == "#":
                i += 1
                ans += arr[i]
            elif arr[i] == ".":
                ans += "."
            elif arr[i].isdigit():
                if int(arr[i])<=26:
                    ans += chr(int(arr[i])+64)
                else:
                    ans+=arr[i]
            i+=1
        print(ans.upper())
def main():
    decode()
main()