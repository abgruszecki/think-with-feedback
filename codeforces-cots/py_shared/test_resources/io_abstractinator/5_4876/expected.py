def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))
    a = list(map(int, input_stream.readline().rstrip("\n").split()))
    a.sort()
    total = 0
    for i in range(n):
        total += abs(a[i] - (i+1))
    print(total, file=output_stream)

