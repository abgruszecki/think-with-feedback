def main(input_stream, output_stream):
    n, m = map(int, input_stream.readline().rstrip("\n").split())

    a = list(map(int, input_stream.readline().rstrip("\n").split()))

    if m <n:

        print(0, file=output_stream)

    else:

        from collections import Counter

        counts = Counter(a)

        max_d = m //n

        for d in range(max_d, 0, -1):

            total = 0

            for c in counts.values():

                total += c //d

                if total >=n:  # early exit

                    break

            if total >=n:

                print(d, file=output_stream)

                return

        print(0, file=output_stream)

