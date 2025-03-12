# Prison_Break
Discrete Structure Show and Tell Project of Prison Break

# Agenda
1. Introduction to Graph Theory
2. Prison Break Concept in Graph Theory
3. Logic and Propositions
4. Set theory
5. Combination and Permutations
6. Path Finding Algorithm (BFS and DFS)
7. Comparison of Algorithm
8. Live demo of Prison Break (Code)
9. Real-World Application
10. Thought Provoking Questions & Discussion

# Introduction to Graph Theory
Graph theory is a branch of mathematics that studies structures formed by nodes (vertices) and edges (connections). It allows us to represent and analyze relationships and pathways in a variety of systems, such as social networks, road maps, and communication networks. Graphs provide a way to visualize and solve problems involving connectivity and flow. In the context of our project, graph theory helps us model and understand the "Prison Break" setup.

## Directed Graph
A directed graph consists of nodes connected by edges, where each edge has a specific direction (from one node to another).

### Examples
1. "Cell A" → "Hallway" (one-way path)
2. "Hallway" → "Yard" (one-way path)
3. But no edge from "Yard" → "Hallway" (because you can’t go back)

## Undirected Graph
Undirected graph consists of nodes connected by edges that have no direction, meaning you can move freely in either direction between two connected nodes.

### Examples
1. "Cell A" ↔ "Hallway" (bidirectional path)
2. "Hallway" ↔ "Yard" (bidirectional path)

# Prison Break Concept in Graph Theory
The "Prison Break" concept uses graph theory to represent a prison layout, where cells, guards, and hallways become nodes, and possible escape routes are edges. This model helps us simulate escape strategies by visualizing the relationships and potential movements within the prison. By treating the prison as a graph, we can apply algorithms to find optimal paths, avoid obstacles, or even locate safe zones. This graphical representation is crucial in designing and analyzing escape plans.

# Set Theory
Set theory allows us to group related objects, such as different groups of cells, accessible paths, or guard positions, to manage them systematically. In the "Prison Break" model, sets can represent cells within guard sight, possible escape routes, or even restricted zones. Using unions, intersections, and differences between sets, we can refine our escape plans by determining areas that are safe, unsafe, or accessible. This mathematical foundation helps us define clear relationships between different parts of the prison layout.

## Sets and Elements
### Location
1. Let 𝐿 be the set of all locations in the prison.
2. 𝐿 = { Cell 1, Cell 2, Cell 3, Common Room, Enter, Exit, Watch Tower }

### Prisoners
1. Let P = { p₁, p₂, p₃ } where:
2. p₁ represents Prisoner A (in Cell 1).
3. p​₂ represents Prisoner B (in Cell 2).
4. p₃​ represents Prisoner C (in Cell 3).

### Guards
1. Let G = { g₁ ,g₂ ,g₃, g₄ } where:
2. g₁ monitors between Cell 2 → Enter repeatedly.
3. g₂ monitors between Cell 3 → Exit repeatedly.
4. g₃​ moves between Guard 1’s Location → Guard 2’s Location → Common Room.
5. g₄ alternates between Enter → Exit repeatedly from the Watchtower

### Edges (Connections)
1. Let E ⊆ 𝐿 × 𝐿 be the set of edges representing valid paths between locations:
2. E = { (Cell 1, Common Room), (Cell 2, Common Room), (Cell 3, Common Room), (Common Room, Enter), (Common Room, Exit), (Common Room, Watch Tower) }

### Time
1. Let T represent the set of all possible times:
2. T₁ = { Lunch Time, Play Time }

# Logics and Proposition in Prison Break
Logic involves reasoning through true or false statements, known as propositions, to build structured arguments or decisions. In "Prison Break," logical statements can model guard behaviors, alarm triggers, or safe passage conditions. Boolean logic helps us combine propositions to form complex conditions necessary for planning an escape. For instance, by combining propositions, we can decide if a particular escape route is feasible based on guard placements.

## Rule 1: 
### Movement Constraint
1. A prisoner Pᵢ can move from location x to location y at time t if:
2. There is a direct edge between x and y: E(x,y)
3. y is not monitored by any guard at that time: ¬∃kGₖ​(y,t)
4. Formal Representation: ∀t ∈ T, ∀Pᵢ ∈ P, ∀x,y ∈ L, (Pᵢ (x,t) ∧ E(x,y) ∧ ¬∃kGₖ(y,t)) → Pᵢ(y, t+1)

## Rule 2: 
### Cell Gate Access
1. A prisoner can leave their cell Cellᵢ only if the cell gate is open at time t
2. Formal Representation: ∀t∈T,∀Pᵢ∈P,(Pᵢ​(Cellᵢ​,t)∧O꜀ₑₗₗᵢ​​(t))→Pᵢ​(Common Room,t+1)

# Combination and Permutations
Combinations and permutations help calculate the different ways of arranging or selecting escape routes and movements, taking order and grouping into account. In "Prison Break," they allow us to examine multiple possible sequences of moves or select the optimal paths considering various conditions. For example, by calculating permutations of movements, we can simulate different escape routes and assess their success probabilities. This combinatorial approach provides a structured way to explore all possible actions for effective escape planning.

# Probability
Probability measures the likelihood of an event occurring, ranging from 0 to 1. It is crucial in fields like statistics, science, and economics for making predictions under uncertainty. Key concepts include events, outcomes, and probability distributions.

## A Bit More Explanation
Formula for permutations:
P(n,r)=n!/(n-r)!
Where:
- n = total number of objects,
- r = number of objects selected,
- ! represents factorial (e.g., 5!=5×4×3×2×1).

Formula for combinations:
C(n,r)=n!/r!(n-r)!
Where:
- n = total number of objects,
- r = number of objects selected.

Suppose I have 1 prisoner that will escape and 3 escape routes, then combination will be better to use. Hence I have:
C(3,1)=3!/1!(3-1)!
C(3,1)=3
Hence, 3 possible combinations of escape. Now I will use more routes and guards and walls and traps, etc.

# Path Finding Algorithm (BFS and DFS)
Breadth-First Search (BFS) and Depth-First Search (DFS) are foundational graph algorithms that explore possible paths through a network of nodes. BFS systematically explores each level, ideal for finding the shortest path in an unweighted graph, while DFS dives deep into each branch, useful for exhaustive exploration. In "Prison Break," these algorithms help identify viable escape routes, prioritize paths, and navigate around obstacles like guards or locked doors. By applying BFS or DFS, we can determine the quickest or safest escape plan.

# Live Demo of Prison Break (Code)
1. Finding the shortest escape route from the start (S) to the exit (E) while avoiding walls (#) and guards (G) using Breadth-First Search (BFS).
2. S: Start (Prisoner's initial position)
3. E: Exit (Escape point)
4. #: Wall (Impassable area)
5. G: Guard (Guarded area)
6. .: Free Space (Path)
7. Prison Grid: The layout of the prison is represented as a 2D list, with each cell containing a character representing walls, guards, or free space.

# Real-World Application
1. Navigation and Routing Systems
   - Example: Google Maps, Uber
   - Use: Graphs represent locations (nodes) and roads (edges) for optimal routing.
   - Impact: Saves time and reduces fuel by providing the fastest routes.

2. Computer Networks
   - Example: Internet traffic
   - Use: Algorithms find the fastest paths for data packets.
   - Impact: Ensures quick and reliable data transmission.

3. Social Network Analysis
   - Example: Facebook, LinkedIn
   - Use: Graphs connect users (nodes) and relationships (edges) for friend recommendations.
   - Impact: Enhances user engagement and community building.

4. Traffic Signal Control Systems
   - Example: Smart city traffic management
   - Use: Optimizes traffic light timings using graph-based algorithms.
   - Impact: Reduces congestion and improves traffic flow.

# Conclusion
By using ideas from discrete mathematics, inmates can plan a prison break in an organized way. This presentation showed how graph theory, set theory, logics, and combinations and permutations can help find and use weak points in the prison system.
