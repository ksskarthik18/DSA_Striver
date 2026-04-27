#Time Complexity : O(n)
from collections import Counter
def sort_char_freq(s):
    freq = Counter(s)
    buckets = [[] for _ in range(len(s)+1)]

    for ch,freq in freq.items():
        buckets[freq].append(ch)
    result = ""
    for i in range(len(s),0,-1):
        for ch in buckets[i]:
            result += ch * i
    return result

def main():
   s = "Aabb"
   print(sort_char_freq(s))
main()
