----

时间：20190608

译者：BING

原文链接：https://www.geeksforgeeks.org/maximum-sum-of-non-overlapping-subarrays-of-length-atmost-k/

----

给定一个整数数组`arr`，长度为N，以及一个整数K，选择一些非重叠的子数组，使得每个子数组的长度至多为K。任何两个子数组**不相邻**，求出所有选择的子数组的和的最大值。

**例子:**

```bash
Input : arr[] = {-1, 2, -3, 4, 5}, k = 2
Output : 11
Sub-arrays that maximizes sum will be {{2}, {4, 5}}.
Thus, the answer will be 2+4+5 = 11.

Input :arr[] = {1, 1, 1, 1, 1}, k = 1
Output : 3

Input: arr[] = {1, 2, 3, 4, 5}, k = 2
Output: 12 // {{1, 2}, {4, 5}}
```

**直观解法** : 一种简单的方法是递归生成所有可能的子数组，子数组满足上面的要求，然后找到最大和。
**时间复杂度** : $O(2^N)$

**高效解法:** 一种更好的方法是使用**动态规划**。

我们假设处在索引`i`处，令`dp[i]`表示所有可能的从下标`i`到`n-1`的子序列的最大和。

我们有K+1个可能的选择：

1. 拒绝`i`并求解`i+1`

2. 选择子数组`{i}`并求解`i+2`

3. 选择子数组`{i, i+1}`并求解`i+3`

    .
    .

  k+1) 选择子数组`{i, i+1, i+2, .., i+k-1}`并求解`i+k+1`

PS. 注意一旦选择某个元素，就得跳一个元素向后求解。

因此，递推关系是：

```c
dp[i] = max(dp[i+1], arr[i]+dp[i+2], arr[i]+arr[i+1]+dp[i+3],
        ...arr[i]+arr[i+1]+arr[i+2]...+arr[i+k-1] + dp[i
        +k+1])
```

下面是这个方法的实现：

```c
// C++ program to implement above approach 
#include <bits/stdc++.h> 
#define maxLen 10 
using namespace std; 

// Variable to store states of dp 
int dp[maxLen]; 

// Variable to check if a given state has been solved 
bool visit[maxLen]; 

// Function to find the maximum sum subsequence 
// such that no two elements are adjacent 
int maxSum(int arr[], int i, int n, int k) 
{ 
	// Base case 
	if (i >= n) 
		return 0; 

	// To check if a state has been solved 
	if (visit[i]) 
		return dp[i]; 
	visit[i] = 1; 

	// Variable to store 
	// prefix sum for sub-array 
	// {i, j} 
	int tot = 0; 
	dp[i] = maxSum(arr, i + 1, n, k); 

	// Required recurrence relation 
	for (int j = i; j < i + k and j < n; j++) { 
		tot += arr[j]; 
		dp[i] = max(dp[i], tot + 
					maxSum(arr, j + 2, n, k)); 
	} 
	// Returning the value 
	return dp[i]; 
} 

// Driver code 
int main() 
{ 
	// Input array 
	int arr[] = { -1, 2, -3, 4, 5 }; 

	int k = 2; 

	int n = sizeof(arr) / sizeof(int); 

	cout << maxSum(arr, 0, n, k); 

	return 0; 
} 
```

END.