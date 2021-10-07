# Metro

Alice has a birthday today, so she invited home her best friend Bob. Now Bob needs to find a way to commute to the Alice's home.

In the city in which Alice and Bob live, the first metro line is being built. This metro line contains nn stations numbered from 11 to nn. 
Bob lives near the station with number 11, while Alice lives near the station with number ss. The metro line has two tracks. 
Trains on the first track go from the station 11 to the station nn and trains on the second track go in reverse direction. 
Just after the train arrives to the end of its track, it goes to the depot immediately, so it is impossible to travel on it after that.

Some stations are not yet open at all and some are only partially open — for each station and for each track it is known whether the station is closed for that track or not. 
If a station is closed for some track, all trains going in this track's direction pass the station without stopping on it.

When the Bob got the information on opened and closed stations, he found that traveling by metro may be unexpectedly complicated. 
Help Bob determine whether he can travel to the Alice's home by metro or he should search for some other transport.

## Input

The first line contains two integers $$n$$ and $s$ ($$2 < s \leq n \leq 1000$$) — the number of stations in the metro and the number of the station where Alice's home is located. 
Bob lives at station 11.

Next lines describe information about closed and open stations.

The second line contains nn integers $a_1$, $a_2$, ..., $a_n$ ($a_i = 0$ or $a_i = 1$). If $$a_i = 1$$, then the i-th station is open on the first track 
(that is, in the direction of increasing station numbers). Otherwise the station is closed on the first track.

The third line contains $n$ integers $b_1, b_2, \ldots, b_n$ ($b_i = 0$ or $b_i = 1$). If $b_i = 1$, then the ii-th station is open on the second track 
(that is, in the direction of decreasing station numbers). Otherwise the station is closed on the second track.

## Output

Print "YES" (quotes for clarity) if Bob will be able to commute to the Alice's home by metro and "NO" (quotes for clarity) otherwise.

You can print each letter in any case (upper or lower).

## Examples

> Input

5 3

1 1 1 1 1

1 1 1 1 1

> Output

YES

> Input

5 4

1 0 0 0 1

0 1 1 1 1

> Output

YES

> Input

5 2

0 1 1 1 1

1 1 1 1 1

> Output

NO

## Note

In the first example, all stations are opened, so Bob can simply travel to the station with number 33.

In the second example, Bob should travel to the station 55 first, switch to the second track and travel to the station 44 then.

In the third example, Bob simply can't enter the train going in the direction of Alice's home.
