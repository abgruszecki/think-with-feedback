<think>
Okay, let's see. The problem is about determining whether we can get an infinite amount of gold starting from a finite amount of sand, using the three spells. So the question is to check if there's a cycle that allows us to generate more gold each time we loop through some spells.

The three spells are:

1. Convert a grams of sand to b grams of lead.
2. Convert c grams of lead to d grams of gold.
3. Convert e grams of gold to f grams of sand.

The key here is to find out if there's a way to loop these transformations such that each loop gives a net gain in gold. For example, after using spell 1, then 2, then 3, if the sand produced from 3 allows us to have more sand than we started with (after some steps), then we can repeat the process infinitely, generating more gold each time.

Wait, but how does the gold accumulate? Let's think. Suppose each cycle converts some sand into gold, and then part of that gold is converted back into sand. But if the sand after conversion is enough to start another cycle, and each time the total gold increases, then we can get infinite gold.

Alternatively, perhaps there's a way to directly generate gold infinitely. For instance, if converting lead to gold (spell 2) can be done with zero lead (c=0). Because if c is zero, then we can convert zero lead into d grams of gold. So each time we use that spell, we get d gold for free. Which would mean infinite gold. But according to the problem statement, the initial state has some finite sand, and no gold or lead.

Wait, but for the second spell, if c is zero and d is positive, then we can generate gold out of nothing. So in that case, the answer is "Ron". So first, we need to check if any of the spells allow us to generate something from nothing.

But wait, the constraints say that the input can have values 0. So let's look for these cases.

The problem is to output "Ron" if we can get an infinite amount of gold. So the conditions under which that's possible.

Let's think of possible scenarios where this is possible.

Case 1: There's a way to create gold from nothing.

That can happen if spell 2 can be used with c=0 (so no lead needed) and d>0. Then, each time we use the spell, we get d grams of gold. So we can generate as much as we want. But how do we start?

Wait, the initial state is some finite amount of sand, but no lead or gold. So if spell 2 requires lead to create gold, but c is 0, then even without any lead, we can use the spell. Because 0 grams of lead can be converted into d grams of gold. So, for example, if c=0 and d>0, then we can generate infinite gold, even if we start with zero lead. So that's a possible scenario.

So first, check if spell 2 can be used with c=0 and d>0. If yes, then output Ron.

But wait, in this case, when you use spell 2, you take c grams of lead and produce d grams of gold. So if c is zero, then you can produce d grams even if you have zero lead. So that's a key point.

Another case: If we can generate more sand than we started with, allowing us to loop and generate more gold each time.

For example, the first example: after converting sand to lead, lead to gold, and gold back to sand, the sand produced is more than the original. So each cycle leaves us with more sand, allowing us to generate more gold each time. But the net sand may not even need to be more; perhaps the cycle creates a surplus in some way.

Alternatively, the problem can be modeled as a system where each cycle produces a certain amount of gold and leaves enough sand to continue the process. So the idea is to check if there's a way to generate a loop where the sand after conversion is sufficient to start the next loop, and each loop contributes a positive amount of gold.

Let's break down the steps.

The process can be thought of as:

1. Use spell 1 to convert sand to lead. So for a grams of sand, you get b grams of lead.

But if a is zero, then you can't use spell 1. Wait, if a is zero, then converting zero sand gives you b grams of lead. So if a=0 and b>0, then you can generate lead from nothing, which would help in getting more gold.

Similarly, if e is zero and f>0, then converting zero gold gives you f grams of sand, which can be used again.

So, the presence of any spell that can generate something from nothing (i.e., when the input is zero, but the output is positive) can lead to infinite resources, which in turn can generate infinite gold.

So the first thing to check is whether any of the following conditions are true:

- Spell 2 can be used to generate gold from nothing: c=0 and d>0. Then, each application gives d gold. So as long as we can use spell 2 once, we can generate infinite gold. But how do we use it once? Because initially, there's sand but no lead. Wait, but if c=0, then you can convert 0 lead into d gold. So even if you have zero lead, you can use spell 2. So in that case, you can generate infinite gold. So this is a primary condition.

But wait, let's look at the fifth example input:

1 1 0 1 1 1

The output is Ron. Because spell 2 here has c=0, d=1. So every time you use spell 2, you get 1 gram of gold. So you can generate as much as you want. So yes, this is a case where spell 2 allows infinite gold.

So the first condition to check is whether c == 0 and d > 0. If so, then output Ron.

But there's a catch. What if using spell 2 requires lead, but if you have some way to generate lead (like spell 1 with a=0 and b>0). Wait, no. Because if spell 1 has a=0, then you can generate lead from nothing, then use spell 2 (even if c>0) as long as you can get enough lead from spell 1.

But perhaps that's a more complex scenario. Let's think.

Suppose spell 1 has a=0 and b=5. Then, you can generate 5 grams of lead from nothing. Then, spell 2 requires c=5, d=10. So each time you use spell 1 once, get 5 lead, then convert that to 10 gold. Then, if spell 3 converts e grams of gold to f sand. Suppose e is 10, f is 100. Then converting 10 gold gives 100 sand. Then, spell 1 can convert 0 sand to 5 lead. So again, you can generate lead and gold. So each loop gives 10 gold, but perhaps you can do this infinitely. So the presence of a spell that can generate resources from nothing (like a=0 and b>0) is also a possible way.

But the problem is to check whether there's a way to get infinite gold. So any scenario that allows generating gold infinitely, regardless of other steps, would result in "Ron".

So the approach here is to check for all possible ways that lead to infinite gold.

So let's think of the possible conditions where the answer is "Ron".

Condition 1: Spell 2 can generate gold from nothing (c=0 and d>0). Because even without any lead, you can apply spell 2 infinitely.

But there's another case: if you can generate lead from nothing (a=0 and b>0) and then use spell 2 (even with c>0) to generate gold, but if the net result is that each loop gives a positive amount of gold. Wait, but if you can generate lead from nothing (spell 1 with a=0), then you can use spell 1 to get as much lead as you need, then use spell 2 (with c>0) to get gold. Then, the total gold would be (b/c) *d per application. But if you can generate lead infinitely, then you can generate gold infinitely. So that's another condition.

For example, if a=0 and b>0 (spell 1 gives lead from nothing), and spell 2 can convert lead to gold (c>0 and d>0). Then, you can generate infinite lead, then infinite gold.

Similarly, if spell 3 gives sand from nothing (e=0 and f>0), then you can generate sand, which can be used in spell 1, then spell 2, etc.

So the possible conditions for infinite gold are:

- Spell 2 can generate gold from nothing (c=0 and d>0). Then, output Ron.

OR

- There's a cycle that allows converting a certain amount of sand into more sand than before, and in each cycle, generate some positive amount of gold. So that each cycle adds more gold and allows the process to continue.

So the first condition is straightforward. Let's check that first.

The second part is more complex. We need to see if there's a way to loop through the spells such that the sand after conversion is >= the sand used, and during the loop, a positive amount of gold is generated.

But how to model this.

Alternatively, the problem can be modeled as checking if the product of the conversion ratios allows for a net gain.

Wait, the three steps are:

1. Sand → Lead: a sand to b lead. So the ratio is b/a per sand. But if a=0, then it's a special case.

2. Lead → Gold: c lead to d gold. Ratio d/c per lead.

3. Gold → Sand: e gold to f sand. Ratio f/e per gold.

If you go through all three steps, starting with S sand:

- After step 1: you need a grams of sand to make b lead. So if you have S >= a, you can convert a sand into b lead. But the remaining sand is S -a. Then, you have b lead.

But for the purpose of generating a loop that can be repeated infinitely, perhaps we need that after the entire cycle, the sand increases. For example:

After using all three spells (convert sand to lead, lead to gold, gold to sand), the net sand is (S -a) + (f * (d/(c)) * (b/a) ) ? Not sure.

Alternatively, let's model each step as:

Let’s say you have S sand, L lead, G gold.

Each step of spell 1 converts x*a sand into x*b lead. So x is the number of times you apply spell 1. But x can be any integer as long as you have enough sand. Similarly for the other spells.

But for the loop to generate more sand than you started with, perhaps after converting some amount of sand through all three steps, the sand produced is more than the original.

But how to model this.

Alternatively, consider the entire cycle: sand → lead → gold → sand. Let's compute the net sand gain from this cycle.

Assume that:

- For every a sand, you get b lead. Then, for that b lead, you can convert c lead into d gold. So the amount of gold you get from b lead is (b / c) * d. Then, convert that gold into sand: ( (b d)/(c) ) / e * f. Because each e gold gives f sand. So per cycle (using a sand), the sand obtained from the cycle is ( (b d f) / (c e) ). So if this value is greater than a, then each cycle gives a net gain of ( (b d f)/(c e) ) - a sand. So if (b d f) > (a c e), then each cycle gives more sand than it took. Thus, each time you can convert the same a sand, but the sand increases each time, allowing infinite cycles, and thus infinite gold.

Wait, but in this scenario, the initial sand is used for a, and then you get (b d f)/(c e) sand. So the net sand is ( (b d f)/(c e) - a ) per cycle. If this is positive, then each cycle gives a net gain in sand. Thus, you can repeat the process, each time using a sand (but maybe you can use more), and each cycle contributes more sand. Then, the sand can grow infinitely, which allows for generating more gold each time.

But how does this generate infinite gold?

Because in each cycle, you can take a sand, convert to lead, then to gold. So each cycle gives (b/c)*d gold. Then, if after converting some of that gold back into sand, the sand increases. So as sand grows, you can do more cycles, each time producing a fixed amount of gold. So the total gold would be (b d / (c)) * (number of cycles), which increases as cycles increase. So if the number of cycles is unbounded (because sand grows each time), then the gold can be infinite.

Wait, but in this case, each cycle uses a sand and produces some gold. So the gold accumulated is (b d / c) per cycle. But the sand after conversion is (b d f)/(c e) - a. If that's positive, then each cycle leaves us with more sand than we started with. So after each cycle, we can run the same steps again, each time adding (b d / c) gold to the total. So as the number of cycles approaches infinity, the total gold would approach infinity.

Therefore, the condition for this scenario is:

(b * d * f) > (a * c * e) → the sand produced from the cycle is more than the a used. And also, that all the necessary steps are possible (i.e., none of the denominators are zero when needed).

But this needs to be checked only if certain conditions are met. For example, each of a, c, e must be non-zero. Because if a is zero, then you can't use a sand (since spell 1 requires a grams of sand). Wait, no. If a is zero, then spell 1 converts 0 sand into b lead. So you can generate lead from nothing. So that's another possible scenario.

So the condition (b*d*f) > (a*c*e) would be part of the check when a, c, e are all positive. Otherwise, we have to handle cases where some steps can be done with zero inputs.

This is getting complicated. Let's structure the possible scenarios.

The overall approach is to check for the following conditions in order:

1. If spell 2 can generate gold from nothing (c=0 and d>0). Then, output Ron. Because you can apply spell 2 infinitely, generating d gold each time.

But wait, there's a catch here. What if spell 2 has c=0 and d>0, but you can't use spell 2 at all because you need lead to cast it? No. Because spell 2 requires c grams of lead. If c is 0, then you can use spell 2 even if you have zero lead. Because 0 grams of lead can be converted into d grams of gold.

So in this case, even with no lead, you can apply spell 2. So you can generate infinite gold. So condition 1 is:

if c == 0 and d > 0 → Ron.

But also, this must be possible to do given the other spells. For example, if you have no lead, can you generate lead from sand to use spell 2? No, because spell 2 can be used with zero lead. So even if you can't generate any lead, you can use spell 2.

But how do you start? The initial state is S sand (which could be any finite amount), 0 lead, 0 gold.

So if c=0 and d>0, you can use spell 2 once, getting d gold. Then, you can use spell 3 (if possible) to convert that gold into sand. But even if you can't, the problem allows us to have a finite amount of sand. So the initial sand can be zero. Wait, the problem says "starting with a finite amount of sand".

Wait, the problem statement says: "from some finite amount of sand". So if the initial sand is zero, but we can generate gold via spell 2 (c=0 and d>0), then the answer is Ron. Because you can generate infinite gold even without any sand. So the initial sand is finite (zero is finite), and you can generate infinite gold.

So condition 1: if c=0 and d>0, then output Ron.

Another condition: if spell 2 can be used to generate gold, but you need to generate the lead first. For example, if spell 1 allows generating lead from nothing (a=0 and b>0), and spell 2 requires c grams of lead (but c is not zero). Then, you can generate infinite lead, then convert that into gold via spell 2. So in this case, infinite gold is possible.

So condition 2: if (a == 0 and b > 0) and (c > 0 and d > 0) → then infinite lead can be generated, leading to infinite gold.

But how?

If a=0 and b>0, then each application of spell 1 gives b grams of lead. So even if you have no sand, you can use spell 1 to generate lead. Then, spell 2 can be applied as long as you have enough lead. For example, with a=0, b=5, c=5, d=10. So each spell 1 gives 5 lead. Then, each spell 2 converts 5 lead to 10 gold. So each cycle (spell 1 once, spell 2 once) gives 10 gold. But you can do this infinitely. So this would generate infinite gold. So even if the initial sand is zero, you can generate lead (since a=0) and then convert it to gold.

So condition 2a: a == 0 and b>0 and c>0 and d>0 → output Ron.

Another scenario: spell 3 can generate sand from nothing (e=0 and f>0). Then, spell 3 can be used to generate infinite sand, which can then be converted into lead, then into gold. So if e=0 and f>0, then you can generate infinite sand. Then, if a>0 and b>0, and c>0 and d>0, then each cycle of spell 3 → spell 1 → spell 2 gives gold. So the sand is generated from nothing, then converted into lead, then into gold. So infinite gold.

So condition 3: e ==0 and f>0, and the other spells allow converting sand to gold.

But how to check that.

Alternatively, any of the spells that can generate a resource from nothing (like a=0 and b>0, c=0 and d>0, e=0 and f>0) can lead to infinite gold if there's a path to convert that resource into gold.

So let's outline all possible conditions:

We can generate infinite gold if:

1. Spell 2 can be used to generate gold from nothing (c=0 and d>0). → Ron.

OR

2. Spell 1 can generate lead from nothing (a=0 and b>0) and spell 2 can generate gold from lead (c>0 and d>0). → So infinite lead can be generated, leading to infinite gold.

OR

3. Spell 3 can generate sand from nothing (e=0 and f>0), and the process of converting that sand into lead (spell 1) and then into gold (spell 2) is possible (a>0 and b>0, c>0 and d>0). → So infinite sand leads to infinite gold.

OR

4. There's a cycle where converting sand → lead → gold → sand gives a net gain in sand. So (b*d*f) > (a*c*e). This allows the sand to be used in a loop, each time generating some gold. So even if each loop produces a fixed amount of gold, but the loops can be repeated infinitely, then the total gold is unbounded.

Additionally, we need to check if any of the intermediate steps are possible. For example, in the cycle scenario (condition 4), the steps are:

- Convert a sand to b lead (spell 1). But for this to be possible, a must be >0. Because if a is zero, then you can generate lead from nothing, but that's covered in other conditions. Wait, no. If a is zero, then spell 1 can be used to generate lead even without sand. So that's a different scenario.

Wait, in condition 4, the idea is that you start with some sand, convert it to lead (spell 1), then to gold (spell 2), then to sand (spell 3). If the total sand after this cycle is greater than the initial sand, then you can repeat the cycle, each time increasing the sand and generating some gold. So each cycle contributes gold, leading to infinite total.

But for this cycle to be possible:

- a must be >0 (to use spell 1, because you have to convert a sand into lead. If a is zero, then you can generate lead from nothing, but that's part of other conditions).

Wait, but if a is zero, then you can generate lead without spending any sand. So in that case, you can generate infinite lead, then convert to gold. So condition 4 is not applicable here.

So condition 4 is applicable only when a, c, e are all non-zero.

So, for condition 4:

If (a >0 and c>0 and e>0) and (b*d*f > a*c*e) → then the cycle produces more sand than it started with, leading to infinite loops and infinite gold.

So the steps would be:

Start with X sand.

Convert X sand into (X/a)*b lead (assuming X >= a, but perhaps even if X is less than a, but that's unclear. But for the cycle to be possible, you need to have at least a sand to convert once. So for the initial cycle, you need to have a sand. But once the cycle starts, each loop gives more sand, so you can do it multiple times.)

Wait, but if you start with S sand, and after converting a sand into b lead, the remaining is S -a. Then you convert b lead into (b//c)*d gold. Then, convert that gold into f sand per e gold. The total sand after the cycle is (S -a) + (f * (d * (b//c)) // e). But this is getting complicated.

Alternatively, considering the ratios. If (b*d*f) > (a*c*e), then each full cycle (convert a sand, then the resulting lead to gold, then that gold to sand) produces more sand than the a that was used. So if after each cycle, the sand increases, then you can loop infinitely, generating a fixed amount of gold per cycle. Thus, the total gold would be unbounded.

But this requires that all the steps in the cycle are possible. So:

- a must be >0: because you need to use a grams of sand in spell 1.

- c must be >0: because spell 2 requires c grams of lead.

- e must be >0: because spell 3 requires e grams of gold.

If any of these are zero, then the cycle can't be completed. So condition 4 is only applicable when a, c, e are all positive.

So, putting all conditions together:

The answer is "Ron" if any of the following is true:

1. c == 0 and d > 0.

OR

2. a == 0 and b > 0 and c > 0 and d > 0.

OR

3. e == 0 and f > 0 and a > 0 and b > 0 and c > 0 and d > 0.

OR

4. a > 0 and c > 0 and e > 0 and (b*d*f) > (a*c*e).

But wait, condition 3: if e is zero and f>0, then spell 3 can generate sand from nothing. So even if you have zero gold, you can use spell 3 to get f sand. Then, use spell 1 to convert that sand into lead, then spell 2 into gold. So the process would be: generate sand (from nothing) via spell 3, then convert to lead, then to gold. Each iteration of this process gives more gold, but how?

Wait, let's see:

If e=0 and f>0:

- Using spell 3 with zero gold (since initial gold is zero) gives f sand. So after spell 3, you have f sand.

- Then, use spell 1 to convert a sand into b lead (if a is positive). But if a is zero, then spell 1 can generate lead from nothing, which is covered in condition 2.

So for condition 3 to hold, perhaps a must be positive. Let me think.

Condition 3 says: e == 0 and f >0 and a>0 and b>0 and c>0 and d>0.

In this case:

- Spell 3 can generate f sand from 0 gold.

- So you start with zero sand. But wait, the initial state is some finite sand. So perhaps the initial sand can be zero. Because the problem says "starting with some finite amount of sand".

So even if the initial sand is zero, but we can generate sand via spell 3 (e=0 and f>0), then we can start the process.

For example:

e=0, f=5. Then, using spell 3 with 0 gold gives 5 sand. Then, convert that to lead (spell 1: a=5, b=10). Then, convert lead to gold (spell 2: c=10, d=20). So each loop gives 20 gold. Then, after that, you can again use spell 3 (with 0 gold again) to get 5 sand. Wait, but after converting the lead to gold, you have 20 gold. So why not use spell 3 again?

But the idea is that in each cycle, you generate sand from nothing (since e=0), then use that sand to make lead and gold.

But if you can generate sand from nothing (e=0 and f>0), then you can generate infinite sand, which can be converted into lead and gold as long as the other spells are functional.

So condition 3 is when e=0 and f>0, and a>0 (so can convert sand to lead), and c>0 (can convert lead to gold), and d>0 (so each conversion gives gold). So even if you start with zero sand, you can generate sand via spell 3, then convert to lead and gold.

So each cycle (spell 3 → spell 1 → spell 2) would generate some gold. And since the sand is generated from nothing (e=0), you can do this infinitely.

But wait, if e is zero, then converting zero gold gives f sand. So even if you have zero gold, you can use spell 3. So in the initial state, with zero gold, you can use spell 3 to get f sand. Then, use spell 1 to convert a grams of sand to b lead, and then spell 2 to convert c grams of lead to d gold.

So the steps would be:

- Use spell 3 (e=0, f>0) → get f sand.

- Use spell 1: convert a sand to b lead. So you need a <= f.

- Use spell 2: convert c lead to d gold. Need c <= b.

But if a=0, then spell 1 converts 0 sand to b lead, which is covered in condition 2.

So for condition 3 to apply, e=0 and f>0, and a>0, and b>0, and c>0, and d>0.

But perhaps even if a is zero, but e=0 and f>0, and other conditions are met.

Wait, no. If a=0, then spell 1 can generate lead from nothing, which is covered in condition 2. So condition 3 is for when you need to generate sand from nothing, then convert to lead and then gold.

So conditions 2 and 3 are separate.

So putting it all together, the code needs to check:

if any of the conditions 1-4 are met → output Ron.

Else, output Hermione.

Now, the problem is to code all these conditions correctly, considering all possible edge cases.

Now, let's think about some test cases.

Sample Input 5:

1 1 0 1 1 1 → output Ron. Because condition 1 is met: c=0 and d=1>0.

Sample Input 7:

100 1 100 1 0 1 → output Ron.

Wait, in this case, e=0 and f=1. So spell 3 can generate 1 sand from 0 gold. So condition 3 would be e=0 and f>0. Then, a=100>0, b=1>0. c=100>0, d=1>0. So condition 3 is satisfied. So the answer is Ron.

But according to the note in the problem, in this case, you can start with zero sand. Use spell 3 to get 10000 grams of sand (by applying it multiple times?), then use spell 1 to generate lead, then convert to gold. Wait, but how?

Wait, for spell 3 (e=0, f=1). So each time you use spell 3, you can take 0 gold and convert to 1 sand. So you can generate 1 sand each time. So you can generate as much sand as you want. For example, use spell 3 once → 1 sand. Then use spell 1: convert 100 sand (but you have 1, which is less than 100. So can't do that). So how does this work?

Wait, in sample input 7: a=100, b=1, c=100, d=1, e=0, f=1.

The note says that you can generate sand from nothing (spell 3). So how? Because e=0, spell 3 allows you to convert 0 grams of gold into 1 gram of sand. So even if you have zero gold, you can use spell 3. So each application of spell 3 gives 1 sand. So if you do this 100 times, you have 100 sand. Then, use spell 1 once to convert 100 sand into 1 lead. Then, use spell 2 to convert 100 lead (but you have 1, which is not enough). Wait, this seems like a problem.

Wait, the note says that in sample 7:

We start with zero sand. Use spell 3 (e=0, f=1) to get 1 sand. Then apply spell 3 again, but you need e=0 and convert 0 gold again. So each application of spell 3 gives 1 sand, but we can apply it as many times as needed. So after applying spell 3 100 times, we have 100 sand. Then, use spell 1 (a=100) to convert 100 sand into 1 lead. Then, use spell 2 (c=100) to convert 100 lead into 1 gold. But we have only 1 lead. So we can't do that. But the note says:

"In the seventh sample, We can also start with a zero amount of sand there. With the aid of the third spell you can get sand out of nothing. We get 10000 grams of sand in this manner. Let's get 100 grams of lead using the first spell 100 times. Then make 1 gram of gold from them. We managed to receive 1 gram of gold, starting with a zero amount of sand! Clearly, in this manner you can get an infinitely large amount of gold."

Ah, right. Because spell 1 requires 100 sand to make 1 lead. So if you have 10000 sand, you can do spell 1 100 times (each time using 100 sand) to get 100*1 = 100 lead. Then, use spell 2 once (c=100) to convert 100 lead into 1 gold. Then, you have 1 gold. But how to generate more gold?

After getting 1 gold, you can use spell 3 again. But spell 3 requires e=0, but you have 1 gold. Wait, spell 3's input is e grams of gold. So if e=0, then you can convert 0 gold into 1 sand. So even after you have 1 gold, you can still apply spell 3 to convert 0 gold into 1 sand. Then, you can generate 10000 sand again, and repeat the process. Each time, you generate 1 gold.

So each full cycle (generate 10000 sand, convert to 100 lead, then 1 gold) gives 1 gold, and the process can be repeated infinitely. So the total gold increases by 1 each cycle. Thus, you can generate as much as you want.

So in this case, the key is that spell 3 allows generating sand from nothing. So even after you have some gold, you can ignore it and keep using spell 3 with 0 gold to generate sand. So each cycle generates 1 gold. So infinite gold is possible.

But according to the conditions we outlined earlier, sample 7 meets condition 3:

e=0, f=1>0. a=100>0, b=1>0. c=100>0, d=1>0. So all parts of condition 3 are met → output Ron.

So in code, we need to check condition 3: e ==0 and f>0, and a>0 and b>0 and c>0 and d>0.

So, code-wise, we need to:

Check all four conditions in order.

Now, let's code these conditions.

Let's break down each condition:

Condition 1: c == 0 and d > 0 → Ron.

But wait, there's a catch. If c=0 and d>0, but it's impossible to cast spell 2. For example, if you need lead to cast spell 2. But if c=0, then you can cast spell 2 with zero lead, giving d gold. So even if you have no lead, you can cast it. So in any case, condition 1 holds.

So code for condition 1:

if c == 0 and d > 0:

   return Ron

Condition 2: a == 0 and b >0 → spell 1 can generate lead from nothing. Then, as long as spell 2 can convert lead to gold (c>0 and d>0), then infinite lead can be converted to infinite gold.

So condition 2 is:

if a ==0 and b >0 and c>0 and d>0:

   return Ron

Condition 3: e ==0 and f>0 → spell 3 can generate sand from nothing. Then, as long as a>0 (so can convert sand to lead), b>0 (so the conversion is positive), c>0 and d>0 (so lead can be converted to gold), then infinite gold can be generated.

So condition 3 is:

if e ==0 and f>0 and a>0 and b>0 and c>0 and d>0:

   return Ron

Condition 4: a>0 and c>0 and e>0 and (b*d*f) > (a*c*e).

In this case, each cycle produces a net gain in sand, leading to infinite loops and infinite gold.

So code:

if a>0 and c>0 and e>0 and (b*d*f) > (a*c*e):

   return Ron

If any of these conditions are true, output Ron. Otherwise, Hermione.

But wait, what about when spell 3 can generate sand from nothing, but a=0 (so spell 1 can generate lead from nothing), and other conditions.

For example:

a=0, b=5, c=5, d=10, e=0, f=10.

In this case, condition 2 is met (a=0, b>0, c>0, d>0), so output Ron. So even though e=0, f>0, but condition 2 is already met.

So the code must check the conditions in order. So the order is important.

So the code should check condition 1 first, then condition 2, then 3, then 4.

Because if any of the earlier conditions are met, the subsequent ones are not needed.

Now, let's handle edge cases.

Edge case 1: All zeros. Output Hermione.

Edge case 2: c=0, d=0 → condition 1 not met.

Edge case 3: a=0, b=5, c=0, d=10. Then condition 1 is met (c=0 and d>0) → output Ron.

Another edge case: a=0, b=0. Then spell 1 can't generate lead. So condition 2 is not met.

Now, code:

Read a, b, c, d, e, f.

Check the four conditions in order.

So, code:

a, b, c, d, e, f = map(int, input().split())

if c == 0 and d > 0:
    print("Ron")
elif a == 0 and b > 0 and c > 0 and d > 0:
    print("Ron")
elif e == 0 and f >0 and a>0 and b>0 and c>0 and d>0:
    print("Ron")
elif a>0 and c>0 and e>0 and (b*d*f) > (a*c*e):
    print("Ron")
else:
    print("Hermione")

Wait, but what about the case where spell 2 can generate gold from nothing (c=0, d>0), but also other conditions are true. For example, c=0 and d>0, and a=0, etc. But the code checks condition 1 first, so it will output Ron correctly.

Testing sample input 5:

Input: 1 1 0 1 1 1 → c=0, d=1 → condition 1 is met → output Ron.

Sample input 7:

100 1 100 1 0 1 → e=0, f=1. a=100>0, b=1>0, c=100>0, d=1>0 → condition 3 is met → output Ron.

Sample input 4 (all zeros) → all conditions fail → output Hermione.

Sample input 6: 1 0 1 2 1 2 → conditions:

c=1 !=0, a=1 !=0. So condition 1 not met.

Condition 2: a=1 !=0 → no.

Condition3: e=1 !=0 → no.

Condition4: a>0, c>0, e>0. Check (0 * 2 * 2) > (1*1*1) → 0>1 → no. So output Hermione.

Sample input 2:

100 50 50 200 200 100 → check conditions:

c=50 !=0 → condition1 no.

Condition2: a=100 !=0 → no.

Condition3: e=200 !=0 → no.

Condition4: a>0, c>0, e>0. Check (50 * 200 * 100) > (100 *50 *200) → 50*200*100 = 1,000,000. 100*50*200 = 1,000,000. So 1e6 is not greater than 1e6 → false. So output Hermione.

Another sample: input 1 (sample 1):

100 200 250 150 200 250.

Check condition4:

a=100>0, c=250>0, e=200>0.

Check 200 * 150 * 250 = 200*150=30000 *250=7,500,000.

a*c*e =100*250*200 =5,000,000.

7.5e6>5e6 → true. So condition4 met → output Ron.

Another edge case: a=0, b=0, c=0, d=5 → condition1 is met (c=0 and d>0) → output Ron.

Another case: a=0, b=5, c=0, d=5 → condition1 is met (c=0 and d>0), so output Ron.

Another case: a=0, b=5, c=3, d=10 → condition2 is met (a=0 and b>0, c>0 and d>0) → output Ron.

Now, code seems to cover all conditions.

But wait, what about when a=0, but spell2 has c=0. For example:

a=0, b=5, c=0, d=10 → condition1 is met (c=0 and d>0) → output Ron.

But according to condition1, it is sufficient.

So the code is correct.

Another edge case: when e=0 and f>0, but a=0. Then, condition3 is not met because a>0 is required. So for example, e=0, f=5, a=0, b=5, c=5, d=10. Then, condition3's a>0 is false. But condition2 is met (a=0, b>0, c>0, d>0) → output Ron.

So code correctly outputs Ron.

Another case: e=0, f=5, a=5>0, b=0 → condition3 not met because b>0 is required. So no.

Now, the code seems to handle all cases.

So the code will check each condition in order and output accordingly.
</think>

```python
a, b, c, d, e, f = map(int, input().split())

if c == 0 and d > 0:
    print("Ron")
elif a == 0 and b > 0 and c > 0 and d > 0:
    print("Ron")
elif e == 0 and f > 0 and a > 0 and b > 0 and c > 0 and d > 0:
    print("Ron")
elif a > 0 and c > 0 and e > 0 and (b * d * f) > (a * c * e):
    print("Ron")
else:
    print("Hermione")
```