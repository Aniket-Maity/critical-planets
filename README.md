Critical Planets
Problem Description

War between Republic and Separatist is escalating. The Separatist are on a new offensive. They have started blocking the path between the republic planets (represented by integers), so that these planets surrender due to the shortage of food and supplies. The Jedi council has taken a note of the situation and they have assigned Jedi Knight Skywalker and his Padawan Ahsoka to save the critical planets from blockade (Those planets or system of planets which can be accessed by only one path and may be lost if that path is blocked by separatist).

Skywalker is preparing with the clone army to defend the critical paths. He has assigned Ahsoka to find the critical planets. Help Ahsoka to find the critical planets(C) in ascending order. You only need to specify those planets which have only one path between them and they cannot be accessed by any other alternative path if the only path is compromised.
Constraints

M <= 10000

N <= 7000
Input

First line contains two space separated integers M and N, where M denotes the number of paths between planets and N denotes the number of planets.

Next M lines, each contains two space separated integers, representing the planet numbers that have a path between them.
Output

C lines containing one integer representing the critical planet that they need to save in ascending order of the planet number if no planet is critical then print -1
Time Limit
1

Examples

Example 1

Input

3 4

0 1

1 2

2 3

Output

0

1

2

3

Explanation


 

Since all the planets are connected with one path and cannot be accessed by any alternative paths hence all the planets are critical.

Example 2

Input

7 6

0 2

0 1

1 2

2 3

4 5

3 4

3 5

Output

2

3

Explanation


 

If the republic loose the path between 2 and 3 then the two system of planets will not be able to communicate with each other. Hence 2 and 3 are critical planets.