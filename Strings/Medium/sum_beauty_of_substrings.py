#Time Complexity :O(n**2)

def beauty_substrings(s):
    n = len(s)
    total = 0
    for i in range(n):
        freq = [0]*26
        for j in range(i,n):
            idx = ord(s[j]) - ord('a')
            freq[idx]+=1

            maxf=0
            minf=float('inf')
            for f in freq:
                if f > 0:
                    maxf=max(maxf,f)
                    minf=min(minf,f)
            total+= (maxf-minf)
    return total

def main():
    s = "aabcb"
    print(beauty_substrings(s))
main()