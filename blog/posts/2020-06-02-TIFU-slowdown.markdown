---
layout: post
title:  "Today I Fucked Up - Slowdown"
date:   2020-06-02 00:00:00 +0000
categories: Softskils TIFU Retrospec
---
# Today I Fucked Up - Slowdown
So today I made a stupid statement "set intersection is not a [commutative operation](https://en.wikipedia.org/wiki/Commutative_property)", which is completely **incorrect!**
$$
\{1,2,3\} \cap \{2\} = \{2\} \newline
\{2\} \cap \{1,2,3\} = \{2\}
$$

So how did we get here! What did I do wrong and what factors contributed to me making a mistake:
 - I was dealing with a complicated multifaceted problem
 - I had oversimplified the problem to a peer
 - I was behind on my work and frustrated
 - I'd received a code review that my code was to complicated which added to my frustration
This lead to the final bad chose: I hastily discarded a suggestion on the first sign of a problem with the given solution.
 
What was implicitly saying is 'Your solution won't work because it doesn't give me the answer I want' and explicitly I was saying *blah blah comunitative blah* this is why it doesn't work. But this is not the right way of thinking! How can anyone who has been only exposed to the problem domain you are dealing with fully understand and grasp all the complexities you have been dealing with for the last $X$ hours or more. They simply can't, they can only give suggestions or things to consider. 

So here is the problem as I explained it: 

> 'We have a vector of sets we want to know if we consider all the sets
> do any of them share at least one element with any other set'.

    vector<set> data;
    
What was described to me was that I should use the intersect of all the sets. Now I thought about this and to me this would not work. *Although it had nothing to do with commutativity, and I'm still quite embarrassed by that brain fart.* But because of many misunderstandings,  this is how I heard the solutions:

    def intersection(a,b):
	    return a.intersection(b)
    collisions = reduce(intersection, data)

What I _now_ think the review meant was something more like:

    def has_collision()
	    for i_set in data:
	        for j_set in data:
		        if i_set is j_set:
				    continue
			    if intersection(i_set, j_set):
			        return true
		return false
	
Now this would work for the problem I described and this is the second mistake I made. It was that I'd oversimplified the problem when explaining it. What I should have said was 

> 'We have a vector of sets, we want to consider each of the sets and
> discover the elements that appear in any other set'.

I had been blinded by my understanding and I had mislead my peers about the actual problem. After some more thought I can still take on his suggestion. The code would look something like and it would be correct.
 
    collisions = set(chain(map(intersection, combination(data, 2))))

# What can be learnt
 
 **listen to the answers peers give.** They will reflect two things their:
 
 1. knowledge and experience and
 2. understanding of your description of the problem. 
 
If there answer doesn't seem correct stop, think, ask questions, and consider that you might not have explained the problem well at all.

**Seek to understand before seeking to be understood** I rushed back to the reviewer and said it doesn't work because of *'blah'*. This was so stupid! I hadn't taken any time to understand even why it didn't work, I just made up some stupid reason in my head convinced myself I was right and replied to the reviewer. 

> Better to be thought a fool than to speak and confirm it beyond doubt

**Take time to rest and recover and review.** As you can see this mistake has taken quite a toll on me. I've written ~609 words at this point on something I think most people would discard and say "I was having a bad day". Well I think I was having a bad day for a number of reasons. But we must look at each of our mistakes and aim to not repeat them. I was not thinking well, I was frustrated, stressed and tired. Get Sleep, Eat healthy, think, and Run.

Thanks for reading,
1upcoder
