
def generate_binary_string(n):
    result =[]

    def backTrack(current):
        if len(current) == n:
            result.append(current)
            return
        
        backTrack(current + "0")
        if len(current) == 0 or current[-1] != '1':
            backTrack(current + "1") 
    
    backTrack("")

    return result


def main():
    print(generate_binary_string(3))
main()

        




