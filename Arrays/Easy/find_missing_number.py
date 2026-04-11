def find_missing_number(nums):
    n = len(nums)
    expected = (n * (n+1))//2
    actual = sum(nums)
    return expected-actual

def main():
    nums = [0, 1, 2, 4, 5, 6]
    print(find_missing_number(nums))
main()