def longest_common_prefix(self, strs: List[str]) -> str:
    result  = ''
    min_len = min(len(s) for s in strs)
    for i in range(min_len):
        curr_ch = strs[0][i]
        is_match = True
        for j in range(1, len(strs)):
            if strs[j][i] != curr_ch:
                is_match = False
                break
        
        if is_match: 
            result+=curr_ch
        else:
            break
            
    return result