import sys


def main(input_stream, output_stream):
    input = input_stream.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    for _ in range(t):
        n, k, x, y = map(int, data[idx:idx+4])
        idx +=4
        a = list(map(int, data[idx:idx+n]))
        idx +=n

        cnt = sum(1 for num in a if num >k)
        option1 = cnt * x

        sum_a = sum(a)
        if sum_a <= n * k:
            option2 = y
        else:
            option2 = float('inf')

        option3 = float('inf')
        if sum_a > n * k:
            sum_needed = sum_a - n * k
            sorted_a = sorted(a, reverse=True)
            current_sum = 0
            m = 0
            for num in sorted_a:
                current_sum += num
                m +=1
                if current_sum >= sum_needed:
                    break
            option3 = m * x + y

        res = min(option1, option2, option3)
        results.append(res)

    output_stream.write('\n'.join(map(str, results)) + '\n')

