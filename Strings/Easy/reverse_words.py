#Time Complexity : O(n)
def reverse_Words(s):
   words=[]
   word=""

   for ch in s:
      if ch != " " :
         word+=ch
      else:
         if word:
            words.append(word)
            word=""
   if word:
        words.append(word)

   return " ".join(words[::-1])

def main():
   s = "the sky is blue"
   print(reverse_Words(s))
main()

'''
    def reverseWords(s):
    return " ".join(s.split()[::-1])
'''

        
      
        
            