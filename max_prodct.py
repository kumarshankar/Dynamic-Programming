#%%
def cut_rope(n):
    if n%2 ==0:
        return n/2 * n/2
    else:
        return (n-1)/2 * ((n-1)/2+1)


# %%

def cut_rope_answer(n):
    if n <= 3:
        return n
    num_threes = n//3
    if n % 3 == 1:
        num_threes -= 1
        num_twos = 2
    elif n % 3 == 2:
        num_twos = 1
    else:
        num_twos = 0
    return 3**num_threes * 2**num_twos
    
# %%
