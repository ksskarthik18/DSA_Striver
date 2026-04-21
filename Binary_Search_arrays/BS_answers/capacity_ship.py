def find_days(weights,capacity):
    day=1
    total_weight_day=0
    for num in weights:
        total_weight_day+=num
        if total_weight_day>capacity:
            total_weight_day=num
            day+=1
    
    return day


def find_capacity(weights,days):
    low = max(weights)
    high = sum(weights)
    while low<=high:
        mid = (low + high)//2
        day=find_days(weights,mid)
        if day <= days:
            high = mid -1
        else:
            low = mid + 1
    return low

def main():
    weights = [1,2,3,1,1]
    days = 4
    print(find_capacity(weights,days))
main()
