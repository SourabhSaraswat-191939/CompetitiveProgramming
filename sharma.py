
class Pair:
	def __init__(self,ch ,ctr):
		self.chr= ch
		self.ctr = ctr

def reduced_String(k , s):
    if (k == 1):
        return ""

    st = []
    for i in range(len(s)):
        if (len(st) == 0):
            st.append((Pair(s[i] , 1)))
            continue
            
        if (st[-1].chr == s[i]):
            pair = st.pop()
            pair.ctr +=1
            if (pair.ctr == k):
                continue				
            else:
                st.append(pair)

        else:
            st.append((Pair(s[i] , 1)))

    ans = ""
    while(len(st) > 0):
        
        c = st[-1].chr
        cnt = st[-1].ctr
        
        while(cnt >0):
            ans = c + ans
            cnt -= 1
        
        st.pop()
    
    return (ans)


s = input()
r = int(input())

print(reduced_String(r,s))