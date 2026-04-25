class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        Time = O(n+m)
        Space = O(m)
        - Where n is the length of the string s and m is the total number of unique characters in the strings t and s.
        """
        if t == "":
            return "" 
        wnd_start = 0
        s_dict = dict()
        t_dict= dict()
        for t_c in t:
            t_dict[t_c] = t_dict.get(t_c, 0)+1
        
        have, need = 0, len(t_dict)
        res = [-1,-1]
        reslen = float("inf")

        for wnd_end in range(len(s)):
            ch = s[wnd_end]
            #add curr character to the window as its part of the window and then we check if this is a valid character worth checking:
            s_dict[ch] = s_dict.get(ch,0)+1
            #check if this is a concerened character and if their counts match, if it does only then increment the have:
            if ch in t_dict and t_dict[ch] == s_dict[ch]:
                have+=1
            #Window shrink condition (as we need the minimum window):
            while have == need:
                #if condition is met then record this window and the window size:
                if (wnd_end-wnd_start+1) < reslen:
                    res = [wnd_start, wnd_end]
                    reslen = wnd_end-wnd_start+1
                #Now we shrink the window and we have recorded the current window:
                start_ch = s[wnd_start]
                s_dict[start_ch]-=1
                if start_ch in t_dict and s_dict[start_ch] < t_dict[start_ch]:
                    have -=1
                wnd_start+=1
        l,r = res
        return s[l:r+1] if reslen!=float("inf") else ""