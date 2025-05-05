import math


def main(input_stream, output_stream):
    import sys
    input = input_stream.read().split()
    idx = 0
    n = int(input[idx]); idx +=1
    m = int(input[idx]); idx +=1
    k = int(input[idx]); idx +=1
    T = (n * m) // math.gcd(n, m)
    for _ in range(k):
        xi = int(input[idx]); idx +=1
        yi = int(input[idx]); idx +=1
        candidates = []
        # Case 1: even x, even y
        x1 = xi
        y1 = yi
        if x1 == y1:
            t = x1
            # Check a and b
            a = (t - xi) // n
            if (t - xi) % n == 0 and a >=0 and a % 2 == 0:
                b = (t - yi) // m
                if (t - yi) % m ==0 and b >=0 and b %2 ==0:
                    candidates.append(t)
        # Case 2: even x, odd y
        x2 = xi
        y2 = m - yi
        if x2 == y2:
            t = x2
            a = (t - xi) // n
            if (t - xi) % n ==0 and a >=0 and a %2 ==0:
                b_val = t - (m - yi)
                if b_val <0:
                    continue
                b = b_val // m
                if b_val % m ==0 and b >=0 and b %2 ==1:
                    candidates.append(t)
        # Case 3: odd x, even y
        x3 = n - xi
        y3 = yi
        if x3 == y3:
            t = x3
            a_val = t - (n - xi)
            if a_val <0:
                continue
            a = a_val // n
            if a_val %n ==0 and a >=0 and a %2 ==1:
                b_val = t - yi
                if b_val <0:
                    continue
                b = b_val // m
                if b_val %m ==0 and b >=0 and b %2 ==0:
                    candidates.append(t)
        # Case4: odd x, odd y
        x4 = n - xi
        y4 = m - yi
        if x4 == y4:
            t = x4
            a_val = t - (n - xi)
            if a_val <0:
                continue
            a = a_val // n
            if a_val %n ==0 and a >=0 and a %2 ==1:
                b_val = t - (m - yi)
                if b_val <0:
                    continue
                b = b_val // m
                if b_val %m ==0 and b >=0 and b %2 ==1:
                    candidates.append(t)
        # Find minimal valid t < T
        valid = [t for t in candidates if t < T]
        if valid:
            print(min(valid), file=output_stream)
        else:
            print(-1, file=output_stream)
