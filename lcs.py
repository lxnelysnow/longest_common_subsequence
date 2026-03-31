def memoized(f):
    sol: dict = {}
    def wrapper(*args):
        if args not in sol:
            sol[args] = f(*args)
        return sol[args]
    return wrapper

@memoized
def lcs_length(x: str, y: str) -> int:
    if len(x) == 0 or len(y) == 0:    
        return 0
    elif x[-1] == y[-1]:                      
        return 1 + lcs_length(x[:-1], y[:-1])
    else:
        return max(lcs_length(x[:-1], y), lcs_length(x, y[:-1]))    

def lcs(x: str, y: str,) -> str:
    if len(x) == 0 or len(y) == 0:      
        return ""
    elif x[-1] == y[-1]:
        return lcs(x[:-1], y[:-1]) + x[-1]
    elif lcs_length(x[:-1], y) > lcs_length(x, y[:-1]):
        return lcs(x[:-1], y)
    else:
        return lcs(x, y[:-1])