using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Games
{
	class Program
	{
		static void Main(string[] args)
		{
			
			//https://www.hackerrank.com/challenges/an-interesting-game-1/problem
			int[] arr = new int[] { 5, 2, 6, 3 };
			int ret = gamingArray(arr);
		}

		static int gamingArray(int[] arr)
		{
			/*
			 * Write your code here.
			 */
			int arrlength = arr.Length;
			int gameCount = 0;
			while (arrlength > 0)
			{
				int max = 0;
				int maxIndex = 0;

				for (int i = 0; i < arrlength; i++)
				{
					if (arr[i] > max)
					{
						max = arr[i];
						maxIndex = i;
					}
				}

				for (int j = maxIndex; j < arr.Length; j++)
				{
					bool isarrmodified = false;
					if (arr[j] != -1)
					{
						arr[j] = -1;
						arrlength -= 1;
						isarrmodified = true;
					}
					if (isarrmodified)
					{
						gameCount += 1;
					}
				}
			}

			if (gameCount % 2 == 0)
			{
				Console.WriteLine("The winner of the game is BOB");
				return 0;
			}
			else
			{
				Console.WriteLine("The winner of the game is ANDY");
				return 1;
			}
		}
	}
}
