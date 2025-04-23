<think>
Okay, let's see. The problem is about Valera wanting to buy fruits, and we need to calculate the minimum and maximum total prices based on how the price tags are assigned to the fruit types. So, the key here is that each fruit type in Valera's list must be assigned a unique price from the given list of prices, and we want to arrange them in such a way that the total sum is minimized or maximized.

First, I need to understand the input. The input gives n (number of price tags, which equals the number of different fruit types Ashot has), and m (the number of items in Valera's list). Then the prices of the n types. Then m lines of fruit names. The problem states that the distinct fruits in Valera's list are <= n, and all are available. So, the seller has all the needed types, and each of Valera's fruits (types) must be assigned a price from the given list, with each price used exactly once. Wait, no. Wait, the problem says that Ashot hasn't distributed the price tags yet. So, each price tag is assigned to a different kind of fruit (since there are n price tags and n different kinds of fruits in Ashot's stall). Valera's list may have multiple entries for the same fruit, but each fruit in his list is of a type that exists in Ashot's stall. So, each fruit in Valera's list is a type that has a unique price assigned. But when Valera buys, each occurrence in his list contributes the price of that type once.

So the problem reduces to: for each distinct fruit type in Valera's list, assign a price (each price is used exactly once, since Ashot will assign each price to a unique fruit type). Then the total sum is the sum for each occurrence in Valera's list of the price assigned to its type. We need to find the minimal and maximal possible total sum.

Wait, no. Wait, the price tags are assigned to the fruit types that Ashot sells. Since Valera's list's distinct fruits are <= n, but Ashot has exactly n different types. So, when Valera picks fruits from his list, each of those distinct fruits must be assigned a price from the list, and each price must be used exactly once for the Ashot's fruits. So for example, if Valera's list has k distinct fruits (k <= n), then those k must be assigned k distinct prices from the given list, and the remaining n -k prices are assigned to the other fruits Ashot has (which Valera isn't buying, so their prices don't affect the sum). Therefore, the sum depends only on the prices assigned to Valera's distinct fruits, multiplied by the count of each in his list.

So the steps to solve this problem are:

1. Read the list of prices (n elements) and the list of fruits (m elements).
2. For Valera's list, count the frequency of each distinct fruit. Let's call this a frequency dictionary, where each key is a fruit name, and the value is how many times it appears in the list.
3. Sort the prices in ascending order for the minimal sum. Because to minimize the total, the highest frequencies should be multiplied by the smallest prices. Similarly, for the maximum sum, the highest frequencies should be multiplied by the largest prices.

Wait, yes. For example, if a fruit appears 5 times in Valera's list, then assigning it a low price would contribute 5 * price, which is better to minimize the total. So the strategy is: sort the prices, sort the frequencies in descending order. Then, for the minimal sum, multiply each price (sorted ascending) with the corresponding frequency (sorted descending). For the maximum sum, multiply the highest prices with the highest frequencies.

So the approach is:

- Count the frequencies of each fruit in Valera's list. Then, sort these frequencies in descending order.
- Sort the price list in ascending order for the minimal sum. Then multiply the smallest prices with the largest frequencies. For example, if frequencies are [5,3,2], and prices are [1,2,3], then 5*1 +3*2 +2*3 = 5+6+6=17. For maximum sum, prices sorted descending: [3,2,1], so 5*3 +3*2 +2*1 =15+6+2=23.

So the algorithm steps:

1. Count the frequency of each fruit in Valera's list. Let's say the counts are stored in a list, say counts. For example, if Valera's list has 5 entries with 'apple' and 3 with 'orange', counts would be [5,3]. But the order depends on how we process them. So after counting, we sort the counts in descending order. Let's call this sorted_counts.

2. Sort the prices list in two ways: once ascending (for minimal sum) and once descending (for maximal sum). Wait, no. Wait, for minimal sum, we need to assign the smallest prices to the highest counts. So, sort the prices in ascending order. Then multiply the first (smallest) price with the first (largest) count, second price with second count, etc.

Similarly, for maximum sum, sort the prices in descending order, then multiply largest price with largest count.

But wait, the prices list has n elements. But Valera's list has k distinct fruits (k <=n). So the counts list will have k elements. The rest of the prices (n -k) are assigned to the other fruits not in Valera's list, which do not contribute to the sum. So, when considering the minimal and maximal sum, we only need to take the k highest elements in the counts (since the rest are zero). So, even if there are more prices than counts, we take the first k prices after sorting and apply them to the counts.

Wait, but the counts are sorted in descending order. Let's say there are k distinct fruits in Valera's list. So we need to take the k largest frequencies (since they are sorted) and assign them to the prices in a way that optimizes the sum.

So, for minimal sum, we take the first k prices (sorted in ascending order) and multiply each by the counts. For example, counts sorted as [5,3,2], prices sorted ascending [1,2,3,4,5]. Then take the first 3 prices (1,2,3) and multiply 5*1, 3*2, 2*3.

For maximum sum, take the largest k prices. So prices sorted descending: [5,4,3,2,1]. Take first 3 (5,4,3) and multiply 5*5,3*4,2*3.

So the steps are:

- Sort the counts in descending order.

For minimal sum:

- Sort prices in ascending order.

Take the first len(counts) elements of the sorted prices (since the rest are assigned to fruits not in Valera's list and thus their prices don't affect the sum).

Multiply each of these prices with the corresponding count (sorted in descending order) and sum.

For maximum sum:

- Sort prices in descending order.

Take the first len(counts) elements.

Multiply each with the sorted counts (descending), sum.

So the key here is that the counts are sorted in descending order, and the prices are sorted in the order that matches the sum we want (ascending for min, descending for max). Then multiply each pair and sum.

So, the code steps:

Read n and m.

Read the prices as a list of integers.

Read m lines, count the frequency of each fruit. So, use a dictionary to count frequencies.

Extract the counts (values of the dictionary) as a list. Sort this list in descending order.

Compute the minimal sum:

Sort the prices in ascending order. Take the first k elements (k is the length of counts). Multiply each price with the corresponding count, sum all.

Compute the maximal sum:

Sort the prices in descending order. Take first k elements. Multiply each with the counts, sum all.

So for example, in the first sample input:

n=5, m=3.

Prices are [4,2,1,10,5].

The fruits are apple, orange, mango. Each appears once. So counts list is [1,1,1], sorted as [1,1,1].

For minimal sum: sort prices in ascending: [1,2,4,5,10]. Take first 3: 1,2,4. Sum is 1*1 +2*1 +4*1 =7.

For maximum sum: sort prices in descending [10,5,4,2,1]. Take first 3:10,5,4. Sum 10+5+4=19. Which matches the sample output.

Another example: second input.

n=6, m=5.

prices are [3,5,1,6,8,1]

The fruits are peach (1), grapefruit (1), banana (1), orange (2). So counts list is [2,1,1,1]. Wait, no. Wait Valera's list has 5 entries: peach, grapefruit, banana, orange, orange. So the counts are {'peach':1, 'grapefruit':1, 'banana':1, 'orange':2}. So sorted counts are [2,1,1,1].

So len(counts) is 4.

For minimal sum: prices sorted ascending are [1,1,3,5,6,8]. Take first 4: 1,1,3,5. Multiply by counts [2,1,1,1]. So 1*2 +1*1 +3*1 +5*1 =2+1+3+5=11.

For max sum: prices sorted descending [8,6,5,3,1,1]. Take first 4:8,6,5,3. Multiply: 2*8 +1*6 +1*5 +1*3=16+6+5+3=30. Which matches the sample.

So the code needs to:

- Count the frequencies of each fruit in the list.

- Sort the counts in descending order.

- Sort the prices in ascending order, take first k, multiply and sum for min.

- Sort prices in descending order, take first k, multiply and sum for max.

Now, code steps:

Read n and m.

Then read the prices as a list of integers.

Then read m lines, each line is a fruit name. Count the frequency using a dictionary.

Extract the frequency values, sort them in reverse order (descending).

Compute k = len(frequencies).

Now, for min_sum:

sort_prices_asc = sorted(prices)

selected_prices = sort_prices_asc[:k]

sum the product of selected_prices[i] * sorted_counts[i] for i in 0..k-1.

Similarly for max_sum:

sort_prices_desc = sorted(prices, reverse=True)

selected_prices_max = sort_prices_desc[:k]

sum the product.

So the code should be straightforward.

Now, code in Python:

Read n and m.

prices = list(map(int, input().split()))

But wait, the second line is the prices. So the first line is two integers, the second is n integers.

Then m lines of fruit names.

So:

n, m = map(int, input().split())

prices = list(map(int, input().split()))

from collections import defaultdict

counts = defaultdict(int)

for _ in range(m):

    fruit = input().strip()

    counts[fruit] +=1

sorted_counts = sorted(counts.values(), reverse=True)

k = len(sorted_counts)

# Compute min sum

prices_sorted_asc = sorted(prices)

min_sum = 0

for i in range(k):

    min_sum += sorted_counts[i] * prices_sorted_asc[i]

# Compute max sum

prices_sorted_desc = sorted(prices, reverse=True)

max_sum = 0

for i in range(k):

    max_sum += sorted_counts[i] * prices_sorted_desc[i]

print(min_sum, max_sum)

Wait, but the prices list has n elements, and k can be up to n (since the problem says the number of distinct fruits in Valera's list is <=n). So when k is 5, and prices has 5 elements, the code takes the first 5 prices. Which is correct.

But wait, in the case where k is less than n, we have to take the first k elements of the sorted prices. Because the other prices are assigned to fruits not in Valera's list. So, yes. So the code is correct.

Testing the first sample:

prices [4,2,1,10,5]

sorted asc: [1,2,4,5,10]

sorted_counts is [1,1,1] (k=3)

selected_prices for min: 1,2,4.

sum is 7.

Yes.

Another example:

second sample:

prices [3,5,1,6,8,1]

sorted_asc is [1,1,3,5,6,8]

sorted_counts has 4 elements (2,1,1,1). So selected prices are first 4: 1,1,3,5.

sum is 2*1 (for the 2) + 1*1 (for first 1) +1*3 (third price) +1*5 (fourth price) = 2 +1 +3 +5=11.

Yes.

Similarly, sorted_desc for max: [8,6,5,3,1,1]. first four:8,6,5,3. 2*8=16, 1*6=6, 1*5=5, 1*3=3. Sum 30.

So the code works.

Now, considering the constraints:

n and m can be up to 100, which is very small. So even though sorting is O(n log n) and k can be up to 100, this is manageable. The code will run in O(n log n) + O(m) time, which is acceptable.

Memory-wise, the counts dictionary and the sorted lists are manageable. For 100 elements, it's trivial.

So this approach is correct and efficient.

Now, code:

We can use the code as written, but in Python, when reading the fruit names, input().strip() is necessary to avoid any leading or trailing whitespace (the problem says that each name is a non-empty string of lowercase letters). The problem states that the names are correct (existence in Ashot's stall is guaranteed). So no need to check for that.

So the code is as follows.
</think>

```python
n, m = map(int, input().split())
prices = list(map(int, input().split()))
from collections import defaultdict

count = defaultdict(int)
for _ in range(m):
    fruit = input().strip()
    count[fruit] += 1

sorted_counts = sorted(count.values(), reverse=True)
k = len(sorted_counts)

prices_sorted_asc = sorted(prices)
min_sum = sum(c * prices_sorted_asc[i] for i, c in enumerate(sorted_counts))

prices_sorted_desc = sorted(prices, reverse=True)
max_sum = sum(c * prices_sorted_desc[i] for i, c in enumerate(sorted_counts))

print(min_sum, max_sum)
```