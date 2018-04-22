using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Threading;

namespace InterviewPractice
{
	public class Program
	{
		static void Main(string[] args)
		{
			Console.WriteLine("hello world!");
			string rhea = "Rhea doesn't care";
			Random r = new Random(0);
			for (int i = 0; i < 1; i++)
			{
				//Console.BackgroundColor = (ConsoleColor)r.Next(15);
				//Console.ForegroundColor = (ConsoleColor)r.Next(15);
				//Console.WriteLine("{0}:{1}", i, rhea);
				//System.Threading.Thread.Sleep(1000);
			}

			var p = new Program();
			//p.GuessRandomNumber();
			//p.CountNumberFactor(200, 1, 0);
			// creating and calling a thread
			/*
			ThreadStart childref = new ThreadStart(p.CallToChildThread);
			Console.WriteLine("In Main: Creating the Child thread");

			Thread childThread = new Thread(childref);
			childThread.Start();
			Console.ReadKey();
			*/

			/*
			Thread thread1 = new Thread(new ThreadStart(p.print1to10Thread));
			thread1.Start();

			if (Thread.Yield())
			{
				Thread thread2 = new Thread(new ThreadStart(p.print11to20Thread));
				thread2.Start();
			}
			Console.ReadKey();
			*/

			//p.mergesortedLists();

			//create a tree
			//Node N = new Node();
			//Node hNode = N.CreateAddNode(N, 10);

			//Create a Queue
			/*Queue q = new Queue();
			q.AddItem(10);
			q.AddItem(20);
			q.AddItem(30);
			q.RemoveItem(20);
			Console.WriteLine(q.GetItem().ToString());
			Console.WriteLine(q.GetItem().ToString());
			Console.WriteLine(q.GetItem().ToString());
			*/

			//print dept, #ofstudents, #offriendsinotherdept.
			printTuple();
		}

		static void printTuple()
		{	//<std_id, std_name, dept_name
			List<Tuple<int, string, string>> tEntries = new List<Tuple<int, string, string>>()
			{
				Tuple.Create(1, "Joe", "Engg"),
				Tuple.Create(2, "John", "Engg"),
				Tuple.Create(3, "Praveen", "HR")
			};

			//std_id, friends_id
			List<Tuple<int, int>> tFriends = new List<Tuple<int, int>>()
			{
				Tuple.Create(1, 2),
				Tuple.Create(1, 3),
				Tuple.Create(2, 3),
				Tuple.Create(3, 1),
			};


			//dept_name, no_of_students, no_of_friends
			Dictionary<string, int> dDeptTotalEmployees = new Dictionary<string,  int>();
			foreach (Tuple<int, string, string> t in tEntries)
			{
				if (!dDeptTotalEmployees.ContainsKey(t.Item3))
				{
					dDeptTotalEmployees.Add(t.Item3, 1);
				}
				else
				{
					dDeptTotalEmployees[t.Item3] = dDeptTotalEmployees[t.Item3] + 1;
				}
			}

			//emp_id, friends_count
			Dictionary<int, int> dFriends = new Dictionary<int, int>();
			foreach (Tuple<int, int> tF in tFriends)
			{
				if (!dFriends.ContainsKey(tF.Item1))
				{
					dFriends.Add(tF.Item1, 1);
				}
				else
				{
					dFriends[tF.Item1] = dFriends[tF.Item1] + 1;
				}

			}

			foreach (KeyValuePair<string, int> kvp in dDeptTotalEmployees)
			{
				Console.WriteLine("{0}:{1}", kvp.Key, kvp.Value);
			}

			List<string> deptcountfrnds = new List<string>();
			foreach (Tuple<int, string, string> idnamedept in tEntries)
			{
				foreach(KeyValuePair<int, int> frndcount in dFriends)
				{
					foreach (KeyValuePair<string, int> deptcount in dDeptTotalEmployees)
					{
						if (idnamedept.Item1 == frndcount.Key && !deptcountfrnds.Contains(deptcount.Key.ToString()))
						{
							deptcountfrnds.Add(deptcount.Key.ToString());
							deptcountfrnds.Add(deptcount.Value.ToString());
							deptcountfrnds.Add(frndcount.Value.ToString());
							break;
						}
					}
				}
			}
		}
		/// <summary>
		/// get factors for a given number in recursive
		/// </summary>
		/// <param name="iValue"></param>
		/// <param name="index"></param>
		/// <param name="factorCnt"></param>
		public void CountNumberFactor(int iValue,int index, int factorCnt )
		{
			if (index <= iValue)
			{
				if (iValue % index == 0)
				{
					Console.WriteLine("Factor of {0} is {1}", iValue, index);
					++factorCnt;
					CountNumberFactor(iValue, index + 1, factorCnt);
					
				}
				else
				{
					CountNumberFactor(iValue, index + 1, factorCnt);
				}
			}

			if (index == iValue)
			{
				Console.WriteLine("Total number of factors for {0} is {1}", iValue, factorCnt);
			}
		}

		public void GuessRandomNumber()
		{
			//int guess = 0;
			Console.WriteLine("Guess a number:");
			string guessNumber = Console.ReadLine();
			int guessedNumber = Int32.Parse(guessNumber);
			Random r = new Random();
			int randNumber = r.Next(10);

			int guessCount = 0;
			while (randNumber != guessedNumber)
			{
				if (guessedNumber > randNumber)
				{
					Console.WriteLine("The number you guessed is larger, try smaller");
					Console.WriteLine("Guess a smaller number:");
					guessNumber = Console.ReadLine();
					guessedNumber = Int32.Parse(guessNumber);
					guessCount++;
				}
				else
				{
					Console.WriteLine("The number you guessed is smaller, try larger");
					Console.WriteLine("Guess a larger number:");
					guessNumber = Console.ReadLine();
					guessedNumber = Int32.Parse(guessNumber);
					guessCount++;
				}
			}

			Console.WriteLine("Total guesses you made is: {0}", guessCount+1);
			Console.WriteLine("Voila...guessed number is: {0}", guessedNumber);
		}

		public void CallToChildThread()
		{
			Console.WriteLine("Child thread starts");

			// the thread is paused for 5000 milliseconds
			int sleepfor = 5000;

			Console.WriteLine("Child Thread Paused for {0} seconds", sleepfor / 1000);
			Thread.Sleep(sleepfor);
			Console.WriteLine("Child thread resumes");
		}

		public void print1to10Thread()
		{
			object _locker = new object();
			int[] array = new int[] { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
			lock (_locker)
			{
				foreach (var item in array)
				{
					Console.WriteLine("Printing numbers from thread1: {0}", item.ToString());
					Thread.Sleep(1000);
				}
			}
		}

		public void print11to20Thread()
		{
			object _locker = new object();
			int[] array = new int[] { 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 };
			lock (_locker)
			{
				foreach (var item in array)
				{
					Console.WriteLine("Printing numbers from thread2: {0}", item.ToString());
					Thread.Sleep(1000);
				}
			}
		}

		public void mergesortedLists()
		{
			int[] aList = new int[] {1, 2, 3, 4, 5 }; //{ 1, 3, 5, 7, 9 };
			int[] bList = new int[] { 4, 6, 7, 9, 10 };
			Console.WriteLine("List1:");
			foreach (var r in aList)
			{
				Console.Write(" " + r.ToString() + ",");
			}
			
			Console.WriteLine("\nList2:");
			foreach (var r in bList)
			{
				Console.Write(" " + r.ToString() + ",");
			}
			int[] rList = new int[aList.Length + bList.Length];
			int i = 0; int j = 0; int k = 0;

			while (i < aList.Length && j < bList.Length)
			{
				if (aList[i] < bList[j])
				{
					rList[k] = aList[i];
					k++;
					i++;
				}
				else if (aList[i] > bList[j])
				{
					rList[k] = bList[j];
					k++;
					j++;
				}
				else
				{
					rList[k] = aList[i];
					k++;
					i++;
					j++;
				}
			}

			if (i < aList.Length)
			{
				for (int l = i; l < aList.Length; l++)
				{
					rList[k] = aList[i];
					k++;
				}
			}

			if (j < bList.Length)
			{
				for (int l = j; l < bList.Length; l++)
				{
					rList[k] = bList[l];
					k++;
				}
			}
			
			Console.WriteLine("\nSorted and deduped list:");
			foreach (var r in rList)
			{
				Console.Write(" " + r.ToString() + ",");
			}
		}
	}

	public class Node
	{
		int value;
		Node lNode = null;
		Node rNode = null;

		public Node CreateAddNode(Node newNode, int addValue)
		{
			if (newNode == null)
			{
				newNode = new Node();
				newNode.value = addValue;
				newNode.lNode = null;
				newNode.rNode = null;
				return newNode;
			}
			else if(newNode.lNode == null)
			{
				Node newnewNode = new Node();
				newnewNode.value = addValue;
				newNode.lNode = newnewNode;
				newnewNode.lNode = null;
				newnewNode.rNode = null;
				return newnewNode;
			}
			else if (newNode.rNode == null)
			{
				Node newnewNode = new Node();
				newnewNode.value = addValue;
				newNode.rNode = newnewNode;
				newnewNode.lNode = null;
				newnewNode.rNode = null;
				return newnewNode;
			}
			return null;
		}

		public void RemoveNode(Node hNode, int Value)
		{
		}
	}

	public class Queue
	{
		object value;
		int index = 0;
		List<int> l = new List<int>();
		
		public void AddItem(object value)
		{
			l.Add(Int32.Parse(value.ToString()));
			index++;
		}

		public Boolean RemoveItem(object value)
		{
			Boolean isRemoved = l.Remove(Int32.Parse(value.ToString()));
			if (isRemoved)
			{
				index--;
			}
			return isRemoved;
		}

		public void InsertItem(object value, int indexAt)
		{
			l.Insert(indexAt, Int32.Parse(value.ToString()));
			index++;
		}

		public object GetItem()
		{
			return l.ElementAt(l.Count - (index--));
		
		}
		public Boolean IsEmpty()
		{
			if (index == 0)
			{
				return true;
			}
			else
			{
				return false;
			}
		}

		public Boolean IsFull()
		{
			return false;
		}
	}
}
