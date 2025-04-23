<think>
Okay, let's tackle this problem. Hmm, the problem is about determining whether a girl and a boy can hold hands in a way that satisfies certain conditions. Let's try to understand the conditions first.

The girl has al fingers on her left and ar on the right. The boy has bl and br. They can switch positions, so the boy can be either to the left or right of the girl. Depending on that, they'll use different hands. For example, if the boy is to the left, the girl uses her left hand (al) and the boy uses his right (br). Wait, no. Let me recheck the problem statement. Oh right, when the boy is on the left of the girl, he takes her left hand with his right. So in that case, the girl's left hand (al) is held by the boy's right hand (br). Conversely, if the boy is on the right, the girl's right hand (ar) is held by the boy's left hand (bl).

So, there are two possible configurations to check:

1. Girl's left (al) and boy's right (br)
2. Girl's right (ar) and boy's left (bl)

For each configuration, we need to check if the conditions are met.

What are the conditions again?

The girl's fingers must be such that between any two of her fingers, there's a boy's finger. That implies that the boy's fingers must be exactly one more than the girl's, perhaps? Or maybe the arrangement is that the girl's fingers are separated by the boy's. Like, if the girl has x fingers, the boy must have x-1 to fit between each pair, but maybe not. Wait, the problem says "no pair of the girl's fingers will touch each other." So the girl's fingers are arranged in a way that between every two of her fingers, there's a boy's finger. So for a girl with x fingers, the boy must have at least x-1 fingers. But wait, maybe more?

Wait, the example given in the first input is:

Girl's left and right are 5 and 1. Boy's are 10 and 5. The output is YES. Let's see. So in one possible configuration, perhaps the girl uses her left (5) and the boy uses his right (5). Then the arrangement would be girl's 5 and boy's 5. How does that work? Wait, the condition for the girl's fingers is that between any two of hers, there's a boy's. So the girl's fingers must be interleaved with the boy's. That would require that the boy's count is exactly one less than the girl's, but that's not possible here. Wait, perhaps I'm misunderstanding the condition.

Wait, maybe the arrangement is such that the boy's fingers are placed between the girl's. For example, if the girl has x fingers, the boy must have at least x-1. But also, the boy's fingers can't have three in a row. So the boy's arrangement must not have three consecutive fingers.

Wait, the problem states two conditions:

1. For the girl's fingers, between any two there is a boy's finger. So the girl's fingers must be separated by at least one boy's finger. So the arrangement would have to be G B G B ... G. That would require that the boy's fingers are exactly one less than the girl's. Because for x girl's fingers, you need x-1 boy's fingers to separate them. But wait, in that case, the boy's count is x-1.

But the second condition is that the boy's fingers do not have three in a row. So the boy's arrangement can't have three consecutive fingers. So the boy's fingers must be arranged in such a way that between any three, there's at least one girl's finger. Wait, no. The problem says "no three fingers of the boy should touch each other." So the boy's fingers can't have three in a row. So the maximum number of consecutive boy's fingers allowed is two.

Wait, this is a bit confusing. Let me rephrase the conditions:

- When they hold hands, the girl's fingers must be such that between any two of her fingers, there's at least one of the boy's. So the girl's fingers are not adjacent; each pair is separated by a boy's. So for a girl's count of x, the boy's count must be >= x-1. Because for x girl's fingers, you need x-1 boy's fingers in between. But maybe the boy can have more than x-1 fingers, but how?

Wait, perhaps the arrangement is that the boy's fingers are placed around the girl's. For example, if the girl has x fingers, and the boy has y fingers, then the arrangement must start and end with the girl's fingers, and between each pair of girl's fingers, there is exactly one boy's finger. Then the boy's y must equal x-1. But that's only one possible scenario.

Alternatively, the boy could have more fingers than that. For example, perhaps the girl's fingers are arranged in such a way that they are separated by the boy's, but the boy can have additional fingers at the ends. Wait, but the problem states that between any two of the girl's fingers there must be a boy's. So if the girl has x fingers, the minimal number of boy's fingers is x-1, but perhaps more is allowed as long as those are placed at the ends. For example, girl's arrangement is G B G, and the boy has 3 fingers, which would be B B G B. Wait, but that's not allowed because between the two girl's fingers, there's exactly one boy's finger. But then the boy's total is 3. So x=2 (girl's), y=3 (boy's). So the arrangement would be G B B B G. Wait, no. How does that fit?

Hmm, perhaps the problem requires that the girl's fingers are not adjacent, but the boy's can have some in the ends. So the girl's x fingers must be placed such that between any two there is at least one boy's, but the boy can have more fingers at the start or end.

Wait, but how would that arrangement look. Let's say girl has x=3 fingers. The boy has y=5. Then the arrangement could be B B G B G B B. Here, between each pair of G's (positions 2 and 4) there is a B. But the first two B's are before the first G, and the last two after the last G. So the condition is satisfied for the girl's fingers. But then the boy's fingers can have more than x-1 (3-1=2) as long as they are placed at the ends. But in this case, the boy's total is 5.

But then the boy's condition is that no three fingers are consecutive. In the arrangement above, the first two B's are consecutive (two), then a G, then a B, then a G, then two B's. So the boy's consecutive counts are 2, 1, 2. Which is okay. So in this case, it's allowed.

Wait, but the boy's fingers are arranged such that between any three of his, there's a girl's. Wait, no. The problem states that the boy's fingers cannot have three in a row. So in the arrangement, the boy's fingers must not have three consecutive. So, the boy's arrangement can have at most two in a row.

So the second condition is that the boy's fingers must be arranged such that there are no three consecutive in the combined sequence.

Putting it all together, the problem is to check for each possible configuration (two possibilities: girl's left and boy's right, or girl's right and boy's left) whether the following conditions are met:

1. The girl's fingers are arranged such that between any two, there's a boy's finger. So the minimal required is that the boy's count is >= (girl's count - 1). But also, the boy's count can't be so large that when arranged with the girl's, the boy's have three in a row.

Wait, perhaps the way to model this is:

For a configuration where the girl has x fingers and the boy has y fingers:

Condition 1: y >= x - 1. Because between x girl's fingers, there must be x-1 boy's.

Condition 2: The boy's fingers cannot have three in a row. So how does the arrangement look?

In this scenario, the girl's x fingers are interleaved with the boy's y fingers. The maximum possible consecutive boy's fingers would be in the case where the boy has y = (x-1) + a + b, where a is the number of boy's fingers at the start, and b is the number at the end. Each a and b can be up to 2, because adding more would create three consecutive.

So for the boy's fingers to not have three consecutive, the maximum possible y is (x-1) + 2 (from start) + 2 (from end) = x-1 +4.

Wait, maybe not. Let's think of the arrangement.

The minimal arrangement to satisfy the girl's condition is that the girl's fingers are separated by one boy's each. So, for x girl's fingers, the arrangement is G B G B ... G. This uses x-1 boy's fingers.

But if the boy has more than x-1, then we need to add the extra fingers either at the start, end, or both. However, each addition can be at most two in a row (since three is forbidden). So:

Suppose the girl's x fingers are arranged as G B G B ... G. Then, the boy can add up to two fingers before the first G, and up to two after the last G. Also, between the girl's fingers, the boy can't add any more because that would create consecutive B's in between. Wait, no. Wait, the initial arrangement has one B between each G. If we add more B's in between, that would create two B's between two G's. But the girl's condition is that between any two of her fingers, there's at least one B. So having two B's between two G's is allowed. But the boy's condition is that no three B's are consecutive. So adding one B between two G's would make two B's there. That's allowed. But adding two B's would make three in a row (the original B plus two added), which is not allowed.

Wait, no. Let's see: the original arrangement between two G's is one B. If we add one more B there, that makes two B's between two G's. So in the combined sequence, between the two G's, we have two B's. So the B's are consecutive. But in the entire sequence, there are two B's in a row. That's allowed. The boy's condition is that there are no three B's in a row.

So the maximum number of B's in the arrangement would be (x-1 + a + b), where a is the number of B's before the first G (a can be 0,1,2), and b is the number after the last G (0,1,2), and between each G, the B's can be up to 2 (since adding one more to the initial one gives two, which is allowed). But wait, in between G's, the initial B is already present (from the x-1 required). Adding another B between two G's would make two B's there. So between each pair of G's, you can have up to two B's. But then, the total B's would be:

a (0-2) + (x-1)*k (where k is the number of B's between each G pair) + b (0-2).

But that's getting complicated. Maybe there's a smarter way to model the constraints.

Let me think differently. For a configuration where the girl's count is x and the boy's is y:

Condition 1: y >= x-1 (since we need at least x-1 B's between the x G's).

Condition 2: y <= (x+1)*2. Because the maximum possible B's would be two before the first G, two after the last, and two between each pair of G's. For example, for x=3, the arrangement would be BB G BB G BB. Then the total B's is 2 (before) + 2*(x-1) (between) + 2 (after) = 2 + 2*(2) + 2 = 2+4+2=8. Wait, x=3, the total B's is 8. So y can be up to 2*(x+1) - 1? Hmm, maybe not. Let me see:

Wait, between each pair of G's, the maximum B's is 2. So for x G's, there are (x-1) gaps between them, each can have up to 2 B's. Plus up to 2 before and 2 after. So total maximum is 2*(x-1) + 2 + 2 = 2*(x+1). So y must be <= 2*(x+1).

But in this case, the boy's count y must satisfy x-1 <= y <= 2*(x+1). Because if y is larger than that, it's impossible to arrange the B's without having three in a row.

So combining these two conditions, for the configuration to be possible, the boy's count y must be between (x-1) and 2*(x+1), inclusive.

But wait, maybe that's the way to model it. So for the girl's x and the boy's y, the boy's y must be >= x-1 and y <= x+1 + x-1 = 2x. Wait, maybe I'm mixing up terms here.

Alternatively, the maximum possible y is (x-1) + 2*(number of possible gaps where B can be added). Let me re-express this:

Original required B's: x-1 (between each pair of G's). Then, in each of the (x-1) gaps between G's, we can add up to 1 more B (to make 2 per gap). So adding (x-1) B's there. Then, adding up to 2 before the first G, and up to 2 after the last G. So total maximum B's is (x-1)*2 + 2 + 2 = 2x + 2. Wait, 2*(x-1) is between G's, plus 2 before and 2 after. So 2x-2 +4 = 2x+2. So maximum possible y is 2x + 2? That doesn't seem right.

Wait, let's take x=3. The maximum arrangement would be BB G BB G BB G BB. So between the G's, two B's each. Then 2 before, 2 after. Total B's is 2 (before) + 2*2 (between two gaps) + 2 (after) = 2+4+2=8. Which is 2*(3) + 2 = 8. So the formula holds. So for x=3, the maximum y is 8.

So the condition is that y must be >= x-1 and y <= 2*(x+1).

Wait, but 2*(x+1) is the maximum possible.

So combining these two conditions, for a configuration where the girl's x and boy's y, the boy's count must be >=x-1 and <=2*(x+1).

But how does this account for the possibility of having different numbers of B's in the gaps? For example, if some gaps have 2 B's and others have 1.

But regardless, the maximum possible is when all gaps have 2 B's and there are 2 before and after.

So for the girl's x and boy's y, if x-1 <= y <= 2*(x+1), then it's possible to arrange the B's such that between any two G's there is at least one B (satisfying the girl's condition) and that there are no three B's in a row (since each gap has at most two B's, and the start and end have at most two).

So the condition is:

y >= x-1 and y <= 2*(x +1) ?

But wait, let's test some examples.

First example:

Input is 5 1 and 10 5. So the possible configurations are:

Case 1: Girl's left (5) and boy's right (5). So x=5, y=5.

Check if 5 >=5-1 (5 >=4 → yes) and 5 <= 2*(5+1) → 5 <=12 → yes. So this is possible.

So the answer is YES.

Another example:

In the second sample input:

4 5 and 3 3.

So possible configurations:

Case 1: girl's left (4) and boy's right (3). So x=4, y=3. Check 3 >=3? 4-1=3. So 3>=3 → yes. Then y=3 <= 2*(4+1) =10 → yes. So this is valid. So in this case, maybe this configuration is possible. So output is YES.

Third example:

1 2 and 11 6. Let's see. Possible configurations:

Girl's left (1) and boy's right (6). x=1, y=6. The conditions are y >=1-1=0 → yes. y <=2*(1+1)=4 → 6 <=4 → no. So this is invalid.

Other configuration: girl's right (2) and boy's left (11). x=2, y=11. Check y >=2-1=1 → 11≥1 yes. y <=2*(2+1)=6 → 11>6 → no. So both configurations are invalid. Hence output is NO.

So this seems to fit.

So the approach is: for each of the two possible configurations (girl's x and boy's y), check whether the boy's y satisfies:

y >= x-1 AND y <= 2*(x +1).

If either configuration satisfies this, then output YES. Else, NO.

Wait, but perhaps there's more to it. Because in some cases, even if y is within this range, the arrangement may not be possible. Let me think.

Let's take x=2, y=3. Then x-1=1, 2*(x+1)=6. So 3 is within the range. But how to arrange 3 B's.

Possible arrangements:

B B G B → then the girl's G's are separated by a B, and the B's in between. But the B B at the start: that's two, which is allowed. Then between G and B, there's one B. Then after that, one B. Wait, no. x=2, so two G's. The arrangement must be something like B B G B G B. But in that case, between the two G's, there's one B (so the girl's condition is satisfied). The B's are arranged as two, then one, then one. But the boy's count is 4 (B B, B, B). Wait, no. Wait, x=2, the girl has two fingers. So the arrangement is G followed by G, separated by at least one B. So the minimal arrangement is G B G. So the boy's count is 1. But if y=3, how?

Let me see: possible arrangement could be B B G B B G. Then, the boy's count is 4. No, that's more than 3. Hmm, maybe I'm misunderstanding the possible arrangements.

Wait, perhaps the initial model is incorrect, and the correct conditions are:

For a configuration to be possible, the boy's y must be >= x-1 and also y <= 2*(x+1). But how do these conditions ensure that the boy's fingers can be arranged without three in a row?

Alternatively, perhaps the correct model is that the boy's y must be >= x-1 and y <= 2*(x+1). But also, the arrangement must not have three consecutive B's.

But how can that be ensured?

Let's take x=2 and y=3. x-1 is 1, 2*(x+1)=6. So y=3 is within the range. So can we arrange 3 B's with x=2?

Possible arrangement:

G B G B B. But wait, the girl's fingers are G and G. Between them is B, which satisfies the condition. Then the B's after the last G are two. So in the entire sequence, the B's are 1 (between the two G's) plus two after. So total 3 B's. So the sequence is G B G B B. The boy's B's are 3. Now, check for consecutive B's: the B B at the end is two, which is allowed. So this arrangement is valid.

Another example: x=3, y=5. x-1=2, 2*(3+1)=8. 5 is within range. How to arrange 5 B's?

The arrangement could be B B G B B G B G B. Wait, but between the G's, the B's are two, two, and one? Let me see:

Wait, the girl has three G's: G, G, G. The minimal arrangement is G B G B G (using two B's). To get 5 B's, add one B before, and two after. So B G B G B G BB → but that's 2 B's before (but no, B's can be added as per the maximum allowed). Or perhaps:

B B G B G B G B B. The B's are two before, then between the first and second G, one B, between second and third G, one B, and two after. Total B's: 2 +1 +1 +2 =6. That's more than 5. Hmm.

Alternatively, the arrangement could be B G B B G B G. Then between the first and second G, there is one B (satisfies girl's condition), between second and third G, one B. Then, the B's before first G is 1, between first and second G is one, between second and third is one, and after third is zero. But then the B's total is 1 +1 +1 =3. Not 5.

Wait, maybe adding two B's between some G's. For example, between the first and second G, two B's. Then the arrangement is G B B G B G. Then between first and second G's, two B's. So the B's count is 2 (between first two G) +1 (between second and third) =3. Then adding one B before and one after gives 3+2=5. So arrangement is B G B B G B G B. Wait, that's total B's: 1 (before) +2 (between 1st and 2nd G) +1 (between 2nd and 3rd) +1 (after) =5. The sequence is B G B B G B G B. Now, check for three B's in a row. The B B between the first two G's is allowed (two). The rest are single B's. So this is valid.

So yes, for x=3 and y=5, it's possible.

So the model seems to hold.

So the approach is:

Check all possible combinations (two possibilities) where the girl's x is either al or ar, and the boy's y is either br or bl.

For each of these two possibilities, check if the boy's y is >= x-1 and <= 2*(x+1). If any of these possibilities satisfies this condition, then output YES, else NO.

So the code would read the girl's al and ar, and the boy's bl and br.

Then, check the two possible configurations:

1. Girl's al (x) and boy's br (y). Check x-1 <= y <= 2*(x+1)
2. Girl's ar (x) and boy's bl (y). Check x-1 <= y <= 2*(x+1)

If either configuration satisfies, output YES.

Wait, but also, the configuration could be swapped. For example, maybe the girl's ar is paired with the boy's bl, and vice versa. Because the boy can be on either side.

Yes, according to the problem statement, the boy can be on the left or right of the girl. So there are two possibilities:

Case 1: girl uses left hand (al) and boy uses right hand (br). So x = al, y = br.

Case 2: girl uses right hand (ar) and boy uses left hand (bl). So x = ar, y = bl.

So for each of these two cases, check if y is >=x-1 and <= 2*(x+1). If either is true, output YES.

That's the approach.

Now, let's test this against the examples.

First example:

Input:
5 1
10 5

So cases:

Case 1: x=5 (al), y=5 (br). Check 5 >=5-1 → 5 >=4 → yes. 5 <=2*(5+1)=12 → yes. So this case is valid. Output YES.

Second example:

Input:
4 5
3 3

Case 1: x=4 (al), y=3 (br). 3 >=4-1=3 → yes. 3 <=2*(5) =10 → yes. So valid. Output YES.

Third example:

Input:
1 2
11 6

Check the two cases:

Case1: x=1 (al), y=6 (br). x-1=0 <=6. 6 <=2*(1+1)=4 → 6>4 → no.

Case2: x=2 (ar), y=11 (bl). 11 >=2-1=1 → yes. 11 <=2*(2+1)=6 → no. So both cases fail. Output NO.

So the model works.

Another test case:

Input 2 in the examples:

4 5 → girl's left is 4, right 5.

Boy's bl=3, br=3.

So cases:

Case1: x=4 (al), y=3 (br). 3 >=4-1=3 → yes. 3 <= 2*(5) =10 → yes. So valid.

Hence output YES.

So this approach seems to work.

So the code would be:

Read al, ar.

Read bl, br.

Check if any of the two conditions is met:

Either:

al and br:

x = al, y = br.

y >= x-1 and y <= 2*(x+1)

OR

ar and bl:

x = ar, y = bl.

y >= x-1 and y <= 2*(x+1)

If either is true, output YES, else NO.

So now, code this.

So the code:

Read al, ar = map(int, input().split())

Read bl, br = map(int, input().split())

Check:

if (br >= al -1 and br <= 2*(al +1)) or (bl >= ar -1 and bl <= 2*(ar +1)):

    print("YES")

else:

    print("NO")

Wait, but wait. The code checks for each of the two cases. For example, in case 1, the girl's x is al, and the boy's y is br. Then check if y is >=x-1 and <=2*(x+1).

Yes.

So the code is straightforward.

Let's test the first example:

al=5, ar=1. bl=10, br=5.

Check case1: x=5, y=5. 5 >=5-1=4 → yes. 5 <= 2*(6)=12 → yes. So condition met. Output YES.

Second example: al=4, ar=5. bl=3, br=3.

Case1: x=4, y=3. 3 >=3 → yes. 3 <= 10 → yes. So condition met.

Third example: al=1, ar=2. bl=11, br=6.

Case1: x=1, y=6. 6 >=0 → yes. 6 <=4 → no. So no.

Case2: x=2, y=11. 11 >=1 → yes. 11 <=6 → no. So no. Output NO.

Thus, code works.

Another test case: input 1 2 and 3 3.

Girl's ar=2, boy's bl=3. So case2: x=2, y=3. 3 >=1 → yes. 3 <= 2*(3)=6 → yes. So yes.

Thus, code returns yes.

So the code seems correct.
</think>

```python
al, ar = map(int, input().split())
bl, br = map(int, input().split())
condition1 = (br >= al - 1) and (br <= 2 * (al + 1))
condition2 = (bl >= ar - 1) and (bl <= 2 * (ar + 1))
print("YES" if condition1 or condition2 else "NO")
```