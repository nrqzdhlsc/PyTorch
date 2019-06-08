----

原文链接：https://www.geeksforgeeks.org/how-to-prepare-for-acm-icpc/

时间：20190608

译者：BING

----

ACM-ICPC(计算机协会-国际大学生编程比赛)是世界范围内一年一次的多层次的编程比赛，已经举办了13年。比赛由IBM赞助。

本文关注点在哪些话题是在比赛编程中重要的，以及哪些尤其需要关注，以便训练自己为ACM-ICPC比赛做准备。

**比赛规则** – 2017世界总决赛规则点击[这里](https://icpc.baylor.edu/worldfinals/rules)

**ICPC问题样例:** 通常ICPC问题有下面的特征：

1. **问题陈述**：描述问题以及应当得到的输出
2. **输入**：确保全神贯注阅读了这个部分，以免错过任何细小的细节导致走向错误的方向。
3. **输出**：和上面一样，这部分也需要仔细阅读。
4. **限制**：包含输入，时间，内存，代码大小等。
5. **时间上限**：看看你的算法能否在固定的范围内完成，不行的话，就需要换算法
6. **内存限制**：如果你喜欢为每个小事分配内存，最好改变这个习惯。

**为ACM-ICPC做好准备**

**首先也是最重要的步骤：练习**。下面的资源可以作为练习ACM-ICPC相似的比赛题目的参考。对于这些OJ，从最多提交的问题开始，并查看解决方案，你又是如何提升这些方案的。参加阅读比赛，保持水平。

- ACM-ICPC过往问题 – [ICPC集合](https://icpc.baylor.edu/worldfinals/problems)，在[Codechef](https://www.codechef.com/IPC15P3C)练习
- [TopCoder](http://community.topcoder.com/tc) – 逐渐增加问题难度的方式
- [Codeforces](http://www.codeforces.com/) -[问题列表](http://codeforces.com/problemset)
- [Codechef](http://www.codechef.com/) –初学者可以从[Codechef Beginners](https://www.codechef.com/problems/school?sort_by=SuccessfulSubmission&sorting_order=desc) 开始，然后逐步成长
- [SPOJ](http://www.spoj.com/) –从简单到困难问题
- [USACO](http://www.usaco.org/) – 非常好的训练资源
- [uvaOnline Judge](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8) – 巨量的问题库
- [Hackerrank](http://www.hackerank.com/) – 聪明的练习问题主题并可参加预备赛
- [Hackerearth](http://www.hackerearth.com/) – 参加预备赛
- [Practice](https://practice.geeksforgeeks.org/) – 适合初学者，问题从困难到艰难
- [List](https://www.quora.com/What-are-the-various-online-programming-contests) 年度比赛列表

**学什么？**

仅仅知道编程基础对于有志于ACM-ICPC的人来说是不够的。你需要全面了解高级算法知识。下面的主题列表是必需的主题和算法，你必须知道在真实比赛中如何提升和抓住机会。

![competitive-programming](assets/Competitive-Programming-2.jpg)

**基础数据结构**：从编程比赛开始，你必须掌握数据结构，下面是常用的数据结构列表。

- [数组](https://www.geeksforgeeks.org/array/)
- [栈](https://www.geeksforgeeks.org/stack/)
- [队列](https://www.geeksforgeeks.org/queue/)
- [字符串](https://www.geeksforgeeks.org/category/c-strings/)
- [堆](https://www.geeksforgeeks.org/category/heap/)
- [哈希](https://www.geeksforgeeks.org/hashing/)
- [数据结构扩展列表](https://www.geeksforgeeks.org/data-structures/)

**高级数据结构**
[优先队列](https://www.geeksforgeeks.org/why-is-binary-heap-preferred-over-bst-for-priority-queue/)，并查集，(增强) 区间树，(增强) 平衡二叉搜索树和二叉索引树。

- [二叉索引树或Fenwick树](https://www.geeksforgeeks.org/binary-indexed-tree-or-fenwick-tree-2/)
- [线段树](https://www.geeksforgeeks.org/segment-tree-set-1-range-minimum-query/) ([RMQ](https://www.geeksforgeeks.org/segment-tree-set-1-range-minimum-query/), [Range Sum ](https://www.geeksforgeeks.org/segment-tree-set-1-sum-of-given-range/)和[ Lazy Propagation](https://www.geeksforgeeks.org/lazy-propagation-in-segment-tree/))
- [K-D树](https://www.geeksforgeeks.org/k-dimensional-tree/) (See [insert](https://www.geeksforgeeks.org/k-dimensional-tree/), [minimum](https://www.geeksforgeeks.org/k-dimensional-tree-set-2-find-minimum/) and [delete](https://www.geeksforgeeks.org/k-dimensional-tree-set-3-delete/))
- [并查不相交集](https://www.geeksforgeeks.org/union-find/) ([Cycle Detection](https://www.geeksforgeeks.org/union-find-algorithm-set-2-union-by-rank/) and [By Rank and Path Compression](https://www.geeksforgeeks.org/union-find-algorithm-set-2-union-by-rank/))
- [Tries](https://www.geeksforgeeks.org/trie-insert-and-search/)
- [区间树](https://www.geeksforgeeks.org/interval-tree/)

[更多高级数据结构](https://www.geeksforgeeks.org/category/advanced-data-structure/)

**排序和搜索**：集中学习基础概念以及熟悉可用的库函数。

- [二叉搜索](http://geeksquiz.com/binary-search/)
- [快排](http://geeksquiz.com/quick-sort/)
- [归并排序](http://geeksquiz.com/merge-sort/)
- [顺序统计](https://www.geeksforgeeks.org/kth-smallestlargest-element-unsorted-array-set-2-expected-linear-time/)

**String manipulation :** Strings make programming problems interesting and difficult too and probably thats the reason they are used extensively in such contests. Learning library functions for String actually proves very helpful (C++ : See [this](https://www.geeksforgeeks.org/c-string-class-and-its-applications/) and [this](https://www.geeksforgeeks.org/stdstring-class-in-c/), [String in Java](http://quiz.geeksforgeeks.org/string-class-in-java/)).

**字符串操作**：字符串使得编程问题变得有趣和困难了，或许这也是为什么它们常常用在这类比赛中。学习字符串的库函数实际中很有用(C++：参考 [这篇](https://www.geeksforgeeks.org/c-string-class-and-its-applications/)和 [这篇](https://www.geeksforgeeks.org/stdstring-class-in-c/)， [Java中的字符串](http://quiz.geeksforgeeks.org/string-class-in-java/))

- [KMP算法](https://www.geeksforgeeks.org/searching-for-patterns-set-2-kmp-algorithm/)
- [Rabin karp](https://www.geeksforgeeks.org/searching-for-patterns-set-3-rabin-karp-algorithm/)
- [Z’s algorithm](https://www.geeksforgeeks.org/z-algorithm-linear-time-pattern-searching-algorithm/)
- [Aho Corasick String Matching](https://www.geeksforgeeks.org/aho-corasick-algorithm-pattern-searching/)

**选择正确的语言**：C++仍然是现今为止最好的竞赛语言，其次是Java，但是你需要选择一个你最舒服的语言。对任意一门语言很自信非常重要。

**Standard Template Library** : A quintessential especially for those using C++ as a language for coding

**标准模板库STL**：一个典型库，尤其是使用C++作为编程语言的人来说：

- Power up C++ STL by Topcoder – [Part 1](https://www.topcoder.com/community/data-science/data-science-tutorials/power-up-c-with-the-standard-template-library-part-1/), [Part 2](https://www.topcoder.com/community/data-science/data-science-tutorials/power-up-c-with-the-standard-template-library-part-2/)
- [C++ Magicians – STL Algorithms](https://www.geeksforgeeks.org/c-magicians-stl-algorithms/)

**动态规划**

- [Longest Common Subsequence](https://www.geeksforgeeks.org/dynamic-programming-set-4-longest-common-subsequence/)
- [Longest Increasing Subsequence](https://www.geeksforgeeks.org/dynamic-programming-set-3-longest-increasing-subsequence/)
- [Edit Distance](https://www.geeksforgeeks.org/dynamic-programming-set-5-edit-distance/)
- [Minimum Partition](https://www.geeksforgeeks.org/partition-a-set-into-two-subsets-such-that-the-difference-of-subset-sums-is-minimum/)
- [Ways to Cover a Distance](https://www.geeksforgeeks.org/count-number-of-ways-to-cover-a-distance/)
- [Longest Path In Matrix](https://www.geeksforgeeks.org/find-the-longest-path-in-a-matrix-with-given-constraints/)
- [Subset Sum Problem](https://www.geeksforgeeks.org/dynamic-programming-subset-sum-problem/)
- [Optimal Strategy for a Game](https://www.geeksforgeeks.org/dynamic-programming-set-31-optimal-strategy-for-a-game/)
- [0-1 Knapsack Problem](https://www.geeksforgeeks.org/dynamic-programming-set-10-0-1-knapsack-problem/)
- [Assembly Line Scheduling](https://www.geeksforgeeks.org/dynamic-programming-set-34-assembly-line-scheduling/)
- [Optimal Binary Search Tree](https://www.geeksforgeeks.org/dynamic-programming-set-24-optimal-binary-search-tree/)

[所有DP算法](https://www.geeksforgeeks.org/tag/dynamic-programming/)

**回溯**

- [Rat in a Maze](https://www.geeksforgeeks.org/backttracking-set-2-rat-in-a-maze/)
- [N Queen Problem](https://www.geeksforgeeks.org/backtracking-set-3-n-queen-problem/)
- [Subset Sum](https://www.geeksforgeeks.org/backttracking-set-4-subset-sum/)
- [m Coloring Problem](https://www.geeksforgeeks.org/backttracking-set-5-m-coloring-problem/)
- [Hamiltonian Cycle](https://www.geeksforgeeks.org/backtracking-set-7-hamiltonian-cycle/)

[更多回溯问题](https://www.geeksforgeeks.org/fundamentals-of-algorithms/#Backtracking)

**贪心算法**

- [Activity Selection Problem](https://www.geeksforgeeks.org/greedy-algorithms-set-1-activity-selection-problem/)
- [Kruskal’s Minimum Spanning Tree Algorithm](https://www.geeksforgeeks.org/greedy-algorithms-set-2-kruskals-minimum-spanning-tree-mst/)
- [Huffman Coding](https://www.geeksforgeeks.org/greedy-algorithms-set-3-huffman-coding/)
- [Efficient Huffman Coding for Sorted Input](https://www.geeksforgeeks.org/greedy-algorithms-set-3-huffman-coding-set-2/)
- [Prim’s Minimum Spanning Tree Algorithm](https://www.geeksforgeeks.org/greedy-algorithms-set-5-prims-minimum-spanning-tree-mst-2/)

[More articles on Greedy Algorithms](https://www.geeksforgeeks.org/fundamentals-of-algorithms/#GreedyAlgorithms)

**图算法 :** One of the most important topic which you can not ignore if preparing for ACM – ICPC.

- [Breadth First Search (BFS)](https://www.geeksforgeeks.org/breadth-first-traversal-for-a-graph/)
- [Depth First Search (DFS)](https://www.geeksforgeeks.org/depth-first-traversal-for-a-graph/)
- [Shortest Path from source to all vertices **Dijkstra**](https://www.geeksforgeeks.org/greedy-algorithms-set-6-dijkstras-shortest-path-algorithm/)
- [Shortest Path from every vertex to every other vertex **Floyd Warshall**](https://www.geeksforgeeks.org/dynamic-programming-set-16-floyd-warshall-algorithm/)
- [Minimum Spanning tree **Prim**](https://www.geeksforgeeks.org/greedy-algorithms-set-5-prims-minimum-spanning-tree-mst-2/)
- [Minimum Spanning tree **Kruskal**](https://www.geeksforgeeks.org/greedy-algorithms-set-2-kruskals-minimum-spanning-tree-mst/)
- [Topological Sort](https://www.geeksforgeeks.org/topological-sorting/)
- [Johnson’s algorithm](https://www.geeksforgeeks.org/johnsons-algorithm/)
- [Articulation Points (or Cut Vertices) in a Graph](http://www.test.geeksforgeeks.org/articulation-points-or-cut-vertices-in-a-graph/)
- [Bridges in a graph](http://www.test.geeksforgeeks.org/bridge-in-a-graph/)

[All Graph Algorithms](http://www.test.geeksforgeeks.org/category/graph/)

**基础数学**

**Arithmetic** **:** Programmers must know how integers and real numbers are represented internally and should be able to code high-precision numbers. Bit manipulation tricks and knowing library functions for number basic arithmetic would be very helpful.

**Number theory :** Knowing some of these concepts would save a lot of time and efforts while programming in the contests.

- [Modular Exponentiation](https://www.geeksforgeeks.org/modular-exponentiation-power-in-modular-arithmetic/)
- [Modular multiplicative inverse](https://www.geeksforgeeks.org/multiplicative-inverse-under-modulo-m/)
- [Primality Test | Set 2 (Fermat Method)](https://www.geeksforgeeks.org/primality-test-set-2-fermet-method/)
- [Euler’s Totient Function](https://www.geeksforgeeks.org/eulers-totient-function/)
- [Sieve of Eratosthenes](https://www.geeksforgeeks.org/sieve-of-eratosthenes/)
- [Convex Hull](https://www.geeksforgeeks.org/convex-hull-set-1-jarviss-algorithm-or-wrapping/)
- [Basic and Extended Euclidean algorithms](https://www.geeksforgeeks.org/basic-and-extended-euclidean-algorithms/)
- [Segmented Sieve](https://www.geeksforgeeks.org/segmented-sieve/)
- [Chinese remainder theorem](https://www.geeksforgeeks.org/chinese-remainder-theorem-set-1-introduction/)
- [Lucas Theorem](https://www.geeksforgeeks.org/compute-ncr-p-set-2-lucas-theorem/)

**Combinatorics :** Although directly might not seam to be important, Combinatorics is important to estimate asymptotic complexity of algorithms.

- [Analysis of Algorithms](https://www.geeksforgeeks.org/fundamentals-of-algorithms/#AnalysisofAlgorithms)
- [Combinatorial Game Theory | Set 1 (Introduction)](https://www.geeksforgeeks.org/introduction-to-combinatorial-game-theory/)

**Geometrical Algorithms**

- [Convex Hull](https://www.geeksforgeeks.org/convex-hull-set-1-jarviss-algorithm-or-wrapping/)
- [Graham Scan](https://www.geeksforgeeks.org/convex-hull-set-2-graham-scan/)
- [Line Intersection](https://www.geeksforgeeks.org/check-if-two-given-line-segments-intersect/)
- [Matrix Exponentiation](https://www.geeksforgeeks.org/matrix-exponentiation/) and [this](http://zobayer.blogspot.in/2010/11/matrix-exponentiation.html)
- [Online construction of 3-D convex hull](http://thomasdiewald.com/blog/?p=1888)
- [Bentley Ottmann algorithm to list all intersection points of n line segments](https://en.wikipedia.org/wiki/Bentley–Ottmann_algorithm)
- [Rotating Calipers Technique](https://en.wikipedia.org/wiki/Rotating_calipers)
- [Area/Perimeter of Union of Rectangles](http://stackoverflow.com/questions/14505668/calculate-the-perimeter-and-area-of-intersecting-rectangles)
- [Closest pair of points](https://www.geeksforgeeks.org/closest-pair-of-points-onlogn-implementation/)
- [Area of Union of Circles](http://stackoverflow.com/questions/1667310/combined-area-of-overlapping-circles)
- [Delaunay Triangulation of n points](https://en.wikipedia.org/wiki/Delaunay_triangulation)
- [Voronoi Diagrams of n points using Fortune’s algorithm](https://en.wikipedia.org/wiki/Fortune's_algorithm)
- [Point in a polygon problem](https://www.geeksforgeeks.org/how-to-check-if-a-given-point-lies-inside-a-polygon/)

**Network Flow Algorithms**

- [Maxflow Ford Furkerson Algo and Edmond Karp Implementation](https://www.geeksforgeeks.org/ford-fulkerson-algorithm-for-maximum-flow-problem/)
- [Min cut](https://www.geeksforgeeks.org/minimum-cut-in-a-directed-graph/)
- [Stable Marriage Problem](https://www.geeksforgeeks.org/stable-marriage-problem/)
- [Dinic’s Algorithm for Maximum Flow](https://www.geeksforgeeks.org/dinics-algorithm-maximum-flow/) and [Wiki](https://en.wikipedia.org/wiki/Dinic's_algorithm)
- [Minimum Cost Flow Problem](https://en.wikipedia.org/wiki/Minimum-cost_flow_problem)
- [Successive Shortest path Algorithm](http://www.columbia.edu/~cs2035/courses/ieor6614.S12/mcf-sp.pdf)
- [Cycle Cancelling algorithm](http://mirror.mit-ocw.sbu.ac.ir/courses/sloan-school-of-management/15-082j-network-optimization-spring-2003/animations/cycle_canceling_algorithm.pdf)
- Maximum weighted Bipartite Matching (Kuhn Munkres algorithm/Hungarian Method)
    - [Hungarian Algorithm Wiki](https://en.wikipedia.org/wiki/Hungarian_algorithm)
    - [Hungarian Algorithm for Assignment Problem](https://www.geeksforgeeks.org/hungarian-algorithm-assignment-problem-set-1-introduction/)
    - [Maximum Bipartite Matching](https://www.geeksforgeeks.org/maximum-bipartite-matching/)
- [Stoer Wagner min-cut algorithm](http://www.diss.fu-berlin.de/docs/servlets/MCRFileNodeServlet/FUDOCS_derivate_000000000270/1994_12.pdf)
- [Maximum matching in general graph (Blossom Shrinking)](https://en.wikipedia.org/wiki/Blossom_algorithm)
- [Gomory-Hu Trees](https://www.geeksforgeeks.org/gomory-hu-tree-introduction/)
- [Chinese Postman problem](https://en.wikipedia.org/wiki/Route_inspection_problem)(Please see [this](http://www.suffolkmaths.co.uk/pages/Maths Projects/Projects/Topology and Graph Theory/Chinese Postman Problem.pdf) too)
- [Hopcroft–Karp Algorithm for Maximum Matching](https://www.geeksforgeeks.org/hopcroft-karp-algorithm-for-maximum-matching-set-1-introduction/)

[All Articles on Geometric Algorithms](https://www.geeksforgeeks.org/tag/geometric-algorithms/)

**More Advanced Stuff**

[Bit Algorithms](https://www.geeksforgeeks.org/fundamentals-of-algorithms/#BitAlgorithms) , [Randomized Algorithms](https://www.geeksforgeeks.org/fundamentals-of-algorithms/#RandomizedAlgorithms) , [Branch and Bound](https://www.geeksforgeeks.org/fundamentals-of-algorithms/#BranchandBound) , [Mathematical Algorithms](https://www.geeksforgeeks.org/fundamentals-of-algorithms/#MathematicalAlgorithms) , [Heavy Light Decomposition](https://www.geeksforgeeks.org/heavy-light-decomposition-set-1-introduction/), [A* Search](https://www.geeksforgeeks.org/a-search-algorithm/)

**Informative Articles that you may like to read**

- [An Awesome list for Competitive Programming](http://codeforces.com/blog/entry/23054) – Codeforces
- [What are the algorithms required to solve all C++ problems in Contests ?](https://www.quora.com/What-are-the-algorithms-required-to-solve-all-problems-using-C++-in-any-competitive-coding-contest) – Quora
- [Best books and sites to prepare for ACM-ICPC](https://www.quora.com/What-are-the-best-websites-online-resources-books-etc-to-prepare-for-the-ACM-ICPC) – Quora
- [Introduction to Programming Contest](http://web.stanford.edu/class/cs97si/) – Stanford.edu
- [World Final Problems of ACM-ICPC](https://icpc.kattis.com/problems) – icpc.kattis

**References:**
[Programming Camp Syllabus](https://docs.google.com/document/d/1_dc3Ifg7Gg1LxhiqMMmE9UbTsXpdRiYh4pKILYG2eA4/edit)

This article is contributed by **Vishwesh Shrimali in association with Team GeeksforGeeks**. If you like GeeksforGeeks and would like to contribute, you can also write an article and mail your article to contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks main page and help other Geeks.

Please write comments if you find anything incorrect, missing or you want to share more information about the topic discussed above.

