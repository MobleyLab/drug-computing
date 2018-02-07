# A little more info on making enrichment plots

This provides a little more info on constructing an enrichment plot.

Imagine you have computationally screened compounds A-Z, and you know compounds A, D, E, G, W, and Z are active, and you can assume the rest are inactive. You want to make an enrichment plot to see how much your screening is helping or hurting relative to picking compounds at random.

Let's assume you have run a shape search on your compounds, and you sort the output compounds by score. So you end up with, say, a list which has your final compounds (sorted by score, best to worst) ordered as `[A, X, R, T, Z, P, S, H, J, G, ...]`, where the left is best scoring and the right is worst scoring.

Our next step is to track how many active compounds we found at each point in the list; ideally, all of the active compounds would be early in the final list. So our next step is to determine how many active compounds you found at each point in the list, starting from the left (best scoring) to right (worst scoring).
So you start by looking at the first entry, `A`, and check it against the list of actives.
You have found one active, so you store the value 1.
Then you look at the second entry, `X`, and it is not active. So you still have still only found one active, so you store the value 1 again. Now your list of "actives found" contains the entries `[1, 1]`. Similarly, R is not active, so you have STILL only found 1; and likewise for `T`. So you store the value 1 for `R`, and the value 1 for `T`, so now your list contains `[1, 1, 1, 1]`. Then you look at `Z`. `Z` is on the list of actives, so now you’ve found two actives (`A` and `Z`). So you add 2 to the list, and now have `[1, 1, 1, 1, 2]``.
Then you keep going; `P, S, H, J` are inactive, so you’ve still only found two actives... so you add four more 2's to the list: `[1, 1, 1, 1, 2, 2, 2, 2, 2]`. Then finally you look at `G`, which is active, so now you’ve found three actives. So you add a 3 to the list:  `[1, 1, 1, 1, 2, 2, 2, 2, 2, 3]`

Once you've done all that, if you wanted to proceed to an enrichment plot, you would divide each entry in your final list by the total number of actives. That then gives the FRACTION of actives found at each point in the list, which is exactly what you want for an enrichment plot.
