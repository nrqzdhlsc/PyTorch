// C++ program to implement above approach 
#include <iostream>

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
	int arr[] = { 1, 2, 3, 4, 5 }; 

	int k = 2; 

	int n = sizeof(arr) / sizeof(int); 

	cout << maxSum(arr, 0, n, k); 

	return 0; 
} 
