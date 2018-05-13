using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;

namespace Interviews
{
	class Program
	{
		private static Dictionary<int, string> wordsfreqDict;
		private static List<Tuple<int, string>> wordsfreqDict1;
		private static Dictionary<int, string> partialMatch;
		private static List<Tuple<int, string>> partialMatch1;
		private static Dictionary<int, string> sortedPartialMatch;
		private static List<Tuple<int, string>> sortedPartialMatch1;
		private static Dictionary<int, string> listofKwords;
		private static List<Tuple<int, string>> listofKwords1;
		static void Main(string[] args)
		{
			//Box(); //via karat
			//string validinvalid = ValidInvalid("aabcc");	   //Sherlock and the Valid String @ https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem
			//int retVal = digitSum("12", 2); //https://www.hackerrank.com/challenges/recursive-digit-sum/problem
			//indicesofarraytogetasum();//https://www.hackerrank.com/challenges/icecream-parlor/problem
			//AutoComplete(args); //via datometry
								//BoxOnSite box = new BoxOnSite();
			MinimumLoss(); //https://www.hackerrank.com/challenges/minimum-loss/problem

		}

		static void MinimumLoss()
		{
			int minLoss = Int32.MaxValue;
			long[] price = new long[] { 20, 7, 8, 2, 5 };
			minLoss = minimumLoss(price);
			Console.WriteLine("Minimum loss: {0}", minLoss);
		}

		public static int minimumLoss(long[] price)
		{
			// Complete this function
			int min = Int32.MaxValue;
			for (int i = 0; i < price.Length - 1; i++)
			{
				for (int j = i + 1; j < price.Length; j++)
				{
					if (price[i] > price[j])
					{
						long delta = price[i] - price[j];
						if (delta < min)
						{
							min = (int)delta;
						}
					}
				}
			}

			return min;
		}
		static void indicesofarraytogetasum()
		{
			int m = 4; //money pooled  by two people
			int[] arr = new int[] { 2, 2, 4, 3 }; //4 flavors of icecream

			int[] indices = icecreamParlor(m, arr);
		}

		static int[] icecreamParlor(int m, int[] arr)
		{
			// Complete this function
			int counter = 0;
			List<int> l = new List<int>();
			for (int i = 0; i < arr.Length; i++)
			{
				if (m >= arr[i])
				{
					m = m - arr[i];
					counter += 1;
					l.Add(i + 1);
				}
				if (m == 0 && l.Count() == 2 && counter == 2)
				{
					return l.ToArray();
				}
			}

			return l.ToArray();
		}

		static int digitSum(string n, int k)
		{
			// Complete this function
			string p = "";
			for (int i = 0; i < k; i++)
			{
				p = p + n;
			}
			int sd = superDigit(int.Parse(p));
			return sd;
		}
		static int superDigit(int p)
		{
			int retVal = p;
			while (p > 9)
			{
				retVal = superDigit1(p);
				p = retVal;
			}
			return retVal;
		}

		static int superDigit1(int p)
		{
			if (p != 0)
			{
				return p % 10 + superDigit1(p / 10);
			}
			else
			{
				return 0;
			}

		}

		static string ValidInvalid(string s)
		{
			if (s.Length < 1 || s.Length > 100000)
			{
				return "NO";
			}

			Dictionary<char, int> charCount = new Dictionary<char, int>();
			foreach (char ch in s)
			{

				if (!charCount.ContainsKey(ch))
				{
					charCount.Add(ch, 1);
				}
				else
				{
					charCount[ch] = charCount[ch] + 1;
				}
			}

			Boolean isNotValid = false;
			foreach (char ch in s)
			{
				charCount[ch] = charCount[ch] - 1;
				/*foreach(KeyValuePair<char, int> kvp in charCount)
				{
					Console.WriteLine("{0}:{1}",charCount.ElementAt(0), kvp.Value);
				}*/

				for (int index = 0; index < charCount.Count - 1; index++)
				{
					if (charCount[charCount.ElementAt(index).Key] != charCount[charCount.ElementAt(index + 1).Key])
					{
						isNotValid = true;
						break;
					}
				}
				charCount[ch] = charCount[ch] + 1;
			}

			if (isNotValid)
			{
				return "NO";
			}


			return "YES";
		}

		static void Box()
		{
			var parentChildPairs = new List<Tuple<int, int>>()
			{
				Tuple.Create(1, 3),
				Tuple.Create(2, 3),
				Tuple.Create(3, 6),
				Tuple.Create(5, 6),
				Tuple.Create(5, 7),
				Tuple.Create(4, 5),
				Tuple.Create(4, 8),
				Tuple.Create(8, 9)
			};

			List<List<int>> output = ZeroParentsOneParent(parentChildPairs);
			foreach (var outer in output)
			{
				foreach (var inner in outer)
				{
					Console.WriteLine("{0}", inner.ToString());
				}
			}
		}

		static List<List<int>> ZeroParentsOneParent(List<Tuple<int, int>> parentChildPairs)
		{
			Dictionary<int, int> dict = new Dictionary<int, int>();

			//This is to initialize the dictionary with all the elements from all the pairs to 0
			foreach (var pair in parentChildPairs)
			{
				if (!dict.ContainsKey(pair.Item1))
				{
					dict.Add(pair.Item1, 0);
				}

				if (!dict.ContainsKey(pair.Item2))
				{
					dict.Add(pair.Item2, 0);
				}

			}

			//To get the count of each of elements in the pair
			foreach (var pair in parentChildPairs)
			{
				if (dict.ContainsKey(pair.Item2))
				{
					dict[pair.Item2] = dict[pair.Item2] + 1;
				}
			}

			//This is to collect exactly with 0 parents                      
			List<int> noParents = new List<int>();
			//This is to collect exactly with 1 parents
			List<int> oneParent = new List<int>();
			foreach (var dictpair in dict)
			{
				if (dictpair.Value == 0)
				{
					noParents.Add(dictpair.Key);
				}
				if (dictpair.Value == 1)
				{
					oneParent.Add(dictpair.Key);
				}
			}

			List<List<int>> returnList = new List<List<int>>();
			returnList.Add(noParents);
			returnList.Add(oneParent);

			return returnList;

		}


		/* 
		Suppose we have some input data describing relationships between parents and children over multiple generations. The data is formatted as (parent, child) pairs, where each individual is assigned a unique integer identifier.

		1   2     4
		 \ /     / \
		  3     5   8
		   \   / \   \
			\ /   \   \
			 6     7   9

		Write a function:
			param - parent_child_pairs
			return - two collections:
							one containing all individuals with zero known parents, and 
							one containing all individuals with exactly one known parent.

		Sample output (pseudocode):
		[
		  [1, 2, 4],   // Individuals with zero parents
		  [5, 7, 8, 9] // Individuals with exactly one parent
		]

		 */

		static void AutoComplete(string[] args)
		{
			//See the full solution in C:\Users\pchettypally\Documents\Visual Studio 2017\Projects\InterviewPractice\AutoComplete\
			//Here is my approach. 
			//Step1: Load the words.txt into dictionary
			//Step2: Read the input file from CLI and parse the file
			//Step3: for each line in input file sample_input.txt loop through below
			//Step4: retrieve subdictionary with the partial matches with the file like like M* from dictionary values.
			//Step5: Sorty subdictionary on Keys (frequencies)
			//Step6: Write top K Words from subdictionary into a file.
			//Step7: repeast Step3 - Step6 for each work in input file.

			if (args.Length <= 0) return;

			string pathToWordsFile = args[0];
			string pathToInputFile = args[1];
			int k = Int32.Parse(args[2]);
			string pathToOutputFile = args[3];

			if (!File.Exists(pathToWordsFile) || !File.Exists(pathToInputFile) || !File.Exists(pathToOutputFile) || k <= 0)
				return;

			//Step1. 
			//wordsfreqDict = LoadFileToDict(pathToWordsFile);
			wordsfreqDict1 = LoadFileToDict1(pathToWordsFile);
			File.WriteAllText(pathToOutputFile, string.Empty);

			var lines = File.ReadLines(pathToInputFile);
			foreach (var line in lines)
			{
				//Step2, 3
				//partialMatch = PartialMatch(pathToInputFile, line);
				partialMatch1 = PartialMatch1(pathToInputFile, line);

				//Step4, 5
				//sortedPartialMatch = sortPartialMatchOnFrequency(partialMatch);
				sortPartialMatchOnFrequency1(partialMatch1); //in-place sort

				//Step6
				//listofKwords = ListTopKWords(sortedPartialMatch, k);
				listofKwords1 = ListTopKWords1(partialMatch1, k);

				//WriteToOutPutFile(pathToOutputFile, line);
				WriteToOutPutFile1(pathToOutputFile, line);
			}
		}
		static Dictionary<int, string> LoadFileToDict(string path)
		{
			Dictionary<int, string> wordsfreqDict = new Dictionary<int, string>();
			var lines = File.ReadLines(path);
			foreach (var line in lines)
			{
				var temp = line.Split('\t');
				if (!wordsfreqDict.ContainsKey((Int32.Parse(temp[0].Trim()))))
				{
					wordsfreqDict.Add(Int32.Parse(temp[0].Trim()), temp[1]);
				}
			}
			return wordsfreqDict;
		}

		static List<Tuple<int, string>> LoadFileToDict1(string path)
		{
			List<Tuple<int, string>> wordsfreqDict = new List<Tuple<int, string>>();
			var lines = File.ReadLines(path);
			foreach (var line in lines)
			{
				var temp = line.Split('\t');
				wordsfreqDict.Add(Tuple.Create(Int32.Parse(temp[0].Trim()), temp[1]));
			}
			return wordsfreqDict;
		}

		static Dictionary<int, string> PartialMatch(string pathtoInput, string line)
		{
			Dictionary<int, string> partialMatch1 = new Dictionary<int, string>();
			foreach (KeyValuePair<int, string> kvp in wordsfreqDict)
			{
				if (kvp.Value.Substring(0, line.Length) == line)
				{
					partialMatch1.Add(kvp.Key, kvp.Value);
				}
			}
			return partialMatch1;
		}

		static List<Tuple<int, string>> PartialMatch1(string pathtoInput, string line)
		{
			List<Tuple<int, string>> partialMatch1 = new List<Tuple<int, string>>();
			foreach (var item in wordsfreqDict1)
			{
				if (item.Item2.Substring(0, line.Length) == line)
				{
					partialMatch1.Add(Tuple.Create(item.Item1, item.Item2));
				}
			}
			return partialMatch1;
		}

		static Dictionary<int, string> sortPartialMatchOnFrequency(Dictionary<int, string> partialMatch)
		{
			Dictionary<int, string> sortedPartialMatchOnFreq = new Dictionary<int, string>();
			var list = partialMatch.Keys.ToList();
			list.Sort();
			var sortedKeys = from key in partialMatch.Keys
							 orderby key descending
							 select key;
			foreach (var key in sortedKeys)
			{
				sortedPartialMatchOnFreq.Add(key, partialMatch[key]);
			}
			return sortedPartialMatchOnFreq;
		}

		static void sortPartialMatchOnFrequency1(List<Tuple<int, string>> partialMatch1)
		{
			//List<Tuple<int, string>> sortedPartialMatchOnFreq1 = new List<Tuple<int, string>>();
			partialMatch1.OrderByDescending(a => a.Item1);
		}
		static Dictionary<int, string> ListTopKWords(Dictionary<int, string> sortedPartialMatch, int k)
		{
			Dictionary<int, string> listofKwords = new Dictionary<int, string>();
			int kCounter = 0;
			foreach (KeyValuePair<int, string> kvp in sortedPartialMatch)
			{
				listofKwords.Add(kvp.Key, kvp.Value);
				kCounter += 1;
				if (kCounter == k)
				{
					break;
				}
			}
			return listofKwords;
		}

		static List<Tuple<int, string>> ListTopKWords1(List<Tuple<int, string>> sortedPartialMatch, int k)
		{
			List<Tuple<int, string>> listofKwords1 = new List<Tuple<int, string>>();
			int kCounter = 0;
			foreach (var item in sortedPartialMatch)
			{
				if (kCounter < k)
				{
					listofKwords1.Add(item);
					kCounter += 1;
				}
				else
				{
					break;
				}

			}
			return listofKwords1;
		}
		static void WriteToOutPutFile(string path, string inputline)
		{
			using (StreamWriter writetext = new StreamWriter(path, true))
			{
				writetext.WriteLine("{0}:", inputline);
				foreach (KeyValuePair<int, string> kvp in listofKwords)
				{
					string line = string.Format("{0}, ({1})", kvp.Value, kvp.Key.ToString());
					writetext.WriteLine(line);
				}
				writetext.WriteLine();
			}
		}

		static void WriteToOutPutFile1(string path, string inputline)
		{
			using (StreamWriter writetext = new StreamWriter(path, true))
			{
				writetext.WriteLine("{0}:", inputline);
				foreach (var item in listofKwords1)
				{
					string line = string.Format("{0}, ({1})", item.Item2, item.Item1.ToString());
					writetext.WriteLine(line);
				}
				writetext.WriteLine();
			}
		}
	}
	
}
