# Karnaugh map example

## The (made-up) story

We have founded our new startup with 16 people, and rent an office building with 4 rooms: two medium sized, one small and a large one.

[British scientists](https://en.wikipedia.org/wiki/British_scientists_(meme)) have shown that mixing chatty and extrovert people with introverts can significantly reduce productivity and increase worplace stress.
Thus, we hired a professional mentalist to sort our new employees into groups of 2,4,4 and 6, based on their extraversion personality trait, *how they solve problems*, hobbies, interests, etc., so all can truly become a 10x developer with the perfect environment.

Safety is also a huge concern of ours, so we don't want anyone to have access to any other office than his/hers. 
For that reason, we will have electronic locks installed on all of the office doors, that open only for the residents key cards.
Our job will be to program the mechanism inside the locks to allow access / open the door. 

## The data
The allocation of the employes suggested by the mentalist, and the 4-bit id stored on their key-cards:

**Blue (large) office**:
 - Fernando __Cortez__ - `0011` 
 - Daniel __Davidson__ - `0000`
 - Mariah Janet __Banner__ - `0111`
 - Sara __Manjo__ - `1000`
 - Elijah __Shop__ - `0001`
 - Mohamed __Velimar__ - `1001`

**Orange (medium-1) office**:
 - Matthäus __Galz__ - `0010`
 - Nicholas __Grosd__ - `1010`
 - Tom __Hayned__ - `1111`
 - Tuomas __Rappel__ - `1011`

**Purple (medium-2) office**:
 - Sofi __Brown__ - `1110`
 - Robin __Droubian__ - `1100`
 - Emma __Kocsis__ - `0110`
 - Aneta __Rajah__ - `0100`

**Green (small) office**:
 - Dominic __Bobec__ - `0101`
 - Raffael __Flating__ - `1101`

## Excercise

Prepare a logical circuit for each door lock, that receives the 4 bit key card code as input, and outputs `1` [iff](https://en.wikipedia.org/wiki/If_and_only_if) the person is registered for that room. 

> [!Tip]
> Try to solve the problem first without looking at the solution.

## Solution

We basically have 4 logic functions with 4 inputs (Card code, CC), having the truth table:

|Name | CC0 | CC1 | CC2 | CC3 | | **Blue** | **Orange** | **Purple** | **Green** | 
| ---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Daniel Davidson       | `0` | `0` | `0` | `0` | | ✅ | ❌ | ❌ | ❌ |
| Elijah Shop           | `0` | `0` | `0` | `1` | | ✅ | ❌ | ❌ | ❌ |
| Matthäus Galz         | `0` | `0` | `1` | `0` | | ❌ | ✅ | ❌ | ❌ |
| Fernando Cortez       | `0` | `0` | `1` | `1` | | ❌ | ❌ | ❌ | ❌ |
| Aneta Rajah           | `0` | `1` | `0` | `0` | | ✅ | ❌ | ✅ | ❌ |
| Dominic Bobec         | `0` | `1` | `0` | `1` | | ❌ | ❌ | ❌ | ✅ |
| Emma Kocsis           | `0` | `1` | `1` | `0` | | ❌ | ❌ | ✅ | ❌ |
| Mariah Janet Banner   | `0` | `1` | `1` | `1` | | ✅ | ❌ | ❌ | ❌ |
| Sara Manjo            | `1` | `0` | `0` | `0` | | ✅ | ❌ | ❌ | ❌ |
| Mohamed Velimar       | `1` | `0` | `0` | `1` | | ✅ | ❌ | ❌ | ❌ |
| Nicholas Grosd        | `1` | `0` | `1` | `0` | | ❌ | ✅ | ❌ | ❌ |
| Tuomas Rappel         | `1` | `0` | `1` | `1` | | ❌ | ✅ | ❌ | ❌ |
| Robin Droubian        | `1` | `1` | `0` | `0` | | ❌ | ❌ | ✅ | ❌ |
| Raffael Flating       | `1` | `1` | `0` | `1` | | ❌ | ❌ | ❌ | ✅ |
| Sofi Brown            | `1` | `1` | `1` | `0` | | ❌ | ❌ | ✅ | ❌ |
| Tom Hayned            | `1` | `1` | `1` | `1` | | ❌ | ✅ | ❌ | ❌ |

### Karnaugh map

The 16 possible values of the 4 inputs can be arranged like this in a Karnaugh map:

![Empty Karnaugh map](./map_blank.svg)

The bar next to CCX indicates the rows/columns where the Xth bit is 1. 

Breaking the identifiers like this shows which bits refer to *vertical* or *horizontal* positions:

![Empty Karnaugh map 2](./map_blank_2.svg)

Since the subsets are disjoint, we can actually visualize all 4 on one map:

![Combined Karnaugh map](./map_combined.svg)


### **Green** door

Let's start with the simplest room, the **green** office, which should only let 2 people in, whose position in the Karnaugh map is:

![Green room Karnaugh map](./map_green.svg)

These two positions can be combined simply:

![Green room Karnaugh map - minimized](./map_green_minimized.svg)

It can be read easily from the diagram that CC0 doesn't matter as long as 
 - CC1 is 1 <==> `CC1` <==> we are in the middle rows
 - CC2 is 0 <==> `¬CC2` <==> we are in the left two columns
 - CC3 is 1 <==> `CC3` <==> we are in the middle columns

So the formula is simply `CC1 ∧ ¬CC2 ∧ CC3`, having only one minterm / conjunctive clause (=block).

Which could have been found like this without the map too from the basic DNF form:

```
CC0 ∧ CC1 ∧ ¬CC2 ∧ CC3  ∨  ¬CC0 ∧ CC1 ∧ ¬CC2 ∧ CC3 = 
 (CC0 ∨ ¬CC0) ∧ CC1 ∧ ¬CC2 ∧ CC3 = 
 1 ∧ CC1 ∧ ¬CC2 ∧ CC3 = 
 CC1 ∧ ¬CC2 ∧ CC3
```
### **Purple** door

Let's look at the purple door now: 

![Purple room Karnaugh map](./map_purple.svg)

First, one would think that we will have two blocks of two:

![Purple room Karnaugh map - not fully minimized](./map_purple_not_fully_minimized.svg)

But we have to keep in mind, that the positions on opposite edges are also *neighbors*, one has to imagine this map being on a [torus](https://en.wikipedia.org/wiki/Torus), and thus, we can do better with a single block of 4:

![Purple room Karnaugh map - minimized](./map_purple_minimized.svg)

And we can read this as CC0 and CC2 does not matter, as long as CC1 is 1 and CC3 is 0, the person can enter the purple room. 

So, the formula is `CC1 ∧ ¬CC3`. 

> [!Tip]
> Try simplyfying the basic DNF form as above.

### **Orange** room

Let's look at the other medium sized office:

![Orange room Karnaugh map](./map_orange.svg)

The largest blocks we can have are of size 2, highlighted by gray, red and yellow colors here (for visibility reasons): 

![Orange room Karnaugh map - largest blocks](./map_orange_largest_blocks.svg)

We can cover everything with just the gray and the yellow one, where:
 - gray block: `CC0 ∧ CC2 ∧ CC3`
 - yellow block: `¬CC1 ∧ CC2 ∧ ¬CC3`

So, the minimal DNF form for the circuit of the orange door is: 
`CC0 ∧ CC2 ∧ CC3  ∨  ¬CC1 ∧ CC2 ∧ ¬CC3`.
The first time we need more than 1 minterms, and as such an OR gate.

### **Blue** office

Finally, the largest room:

![Blue room Karnaugh map](./map_blue.svg)

Here the largest blocks are these:

![Blue room Karnaugh map - largest blocks](./map_blue_largest_blocks.svg)

By largest we mean, that there all the other blocks are subsets of one of these, so definitely not needed in a minimal solution.
Just as before, the red block is unnecessary, so:
 - gray block: `¬CC0 ∧ CC2 ∧ CC3`
 - yellow block: `¬CC1 ∧ ¬CC2`

Resulting in the final solution: `¬CC0 ∧ CC2 ∧ CC3  ∨  ¬CC1 ∧ ¬CC2`.

Let's draw the circuit for this one time:

![Blue room circuit](./circuit_blue.svg)

## Notes

### No XOR in DNF

Let's have a look at this hypothetical situation:

![No XOR in DNF](./no_xor_in_dnf.svg)

Using the approach above, we would end up with 2 blocks/minterms of size one  and have the formula: `A∧B∧C∧¬D ∨ A∧¬B∧C∧D`. 
Which is, the minimal Disjunctive Normal Form in this case. 

However, one can have an eye of an eagle and spot that:

```
A∧B∧C∧¬D ∨ A∧¬B∧C∧D = 
 A∧C∧B∧¬D ∨ A∧C∧¬B∧D = 
 A∧C∧ (B∧¬D ∨ ¬B∧D) = 
 A∧C∧(B⊻D)
```

This is much simpler (less gates). 
**However**, this is not a DNF. 
A proper circuit for the task? YES. But NOT a DNF. 
So if the task in the exercise to give the (minimal) DNF, don't do such clever things.

### Overlaps

When this happens:

![Overlaps](./overlap.svg)

8 inputs on the left can be covered by simply `¬C`. 
The remaining two on the right by `B∧C∧D`. 
So `¬C ∨ B∧C∧D` is a proper DNF for this instance, but not minimal. 

Insted of covering the "remaining two" by `B∧C∧D`, we could cover the "middle" by just `B∧D`. 
Yes, the "inside" yellow inputs are covered twice then, but that is not a problem, and this way we can obtain a smaller DNF solution: `¬C ∨ B∧D`.

### Notations

There are several parallel notations. 
Just on one example:
 - `A AND B OR (C XOR NOT D)`
 - `A∧B ∨ (C ⊻ ¬D)`
 - $AB+(C\oplus\bar{D})$

It is not the end of the world if you mix them, but it is good to stay consistent.