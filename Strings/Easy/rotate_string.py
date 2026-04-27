def rotate_String(s,goal):
    if len(s) != len(goal):
        return False
    new_s = s + s
    if len(s) == len(goal):
        if goal in new_s:
            return True
        return False

def main():
    s = "abcde"
    goal = "cdeab"
    print(rotate_String(s,goal))
main()