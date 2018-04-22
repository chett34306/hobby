using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DataStructures
{
	class Program
	{
		static void Main(string[] args)
		{
			//Quick Sort
			qSort();
			



		}

		static void qSort()
		{
			int[] sortList = new int[] { 1, 3, 8, 1, 2, 7, 6, 8 };
			int[] sortedList = quickSort(sortList, 0, sortList.Length - 1);

			for (int i = 0; i < sortedList.Length; i++)
			{
				Console.WriteLine("Quick Sorted:{0}", sortedList[i]);
			}
		}

		static int[] quickSort(int[] arr, int left, int right)
		{
			if (left >= right) return arr; //return error

			int index = partition(arr, left, right);

			if (left < index - 1)
			{
				quickSort(arr, left, index - 1);
			}

			if (index < right)
			{
				quickSort(arr, index, right);
			}

			return arr;
		}

		static int partition(int[] arr, int left, int right)
		{
			int pivot = arr[(left + right) / 2];
			while (left <= right)
			{
				while (arr[left] < pivot) left++;
				while (arr[right] > pivot) right--;
				if (left <= right)
				{
					//swap(arr, left, right);
					int tmp = arr[left];
					arr[left] = arr[right];
					arr[right] = tmp;
					left++;
					right--;
				}
			}
			return left;

		}
	}
}
