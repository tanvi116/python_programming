#include <iostream>
#include <cmath>
#include <vector>

using namespace std;

int missingterm(vector<int> ap)
{
	int len = ap.size();

	int d1 = ap[1] - ap[0];
	int d2 = ap[2] - ap[1];
	int difference = min(abs(d1), abs(d2));
	if (d1 < 0)
		difference *= -1;

	int start = 0;
	int end = len - 1;

	while (start <= end)
	{
		int mid = (end + start) / 2;
		if ((ap[mid] - ap[start]) == ((mid - start) * difference))
		{
			start = mid;
		}
		else if ((ap[end] - ap[mid]) == ((end - mid) * difference))
		{
			end = mid;
		}
		else return mid;
	}

}

int main()
{
	vector<int> arr;
	int n;
	cin >> n;
	for (int i = 0; i < n; i++)
		cin >> arr[i];

	cout << missingterm(arr);
}


#include <iostream>
#include <cmath>

using namespace std;

int missingterm(int ap[], int len)
{
	int d1 = ap[1] - ap[0];
	int d2 = ap[2] - ap[1];
	int difference = min(abs(d1), abs(d2));
	if (d1 < 0)
		difference *= -1;

	int start = 0;
	int end = len - 1;

	while (start <= end)
	{
		int mid = (end + start) / 2;
		if ((ap[mid] - ap[start]) == ((mid - start) * difference))
		{
			start = mid;
		}
		else if ((ap[end] - ap[mid]) == ((end - mid) * difference))
		{
			end = mid;
		}
		else return mid;
	}

}

int main()
{
	int arr[100];
	int n;
	cin >> n;
	for (int i = 0; i < n; i++)
		cin >> arr[i];

	cout << missingterm(arr, n);
}