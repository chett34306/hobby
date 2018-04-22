using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;

namespace AutoComplete
{
	class Program
	{
		private static List<Tuple<int, string>> wordsfreqDict1;
		private static List<Tuple<int, string>> partialMatch1;
		private static List<Tuple<int, string>> listofKwords1;
		
		static void Main(string[] args)
		{
			//Here is my approach
			//Step1: Load the words.txt into dictionary
			//Step2: Read the input file from CLI and parse the file
			//Step3: for each line in input file sample_input.txt loop through below
			//Step4: retrieve subdictionary with the partial matches with the file like like M* from dictionary values.
			//Step5: Sorty subdictionary on Keys (frequencies)
			//Step6: Write top K Words from subdictionary into a file.
			//Step7: repeast Step3 - Step6 for each work in input file.

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
				partialMatch1 = PartialMatch1(pathToInputFile, line);

				//Step4, 5
				sortPartialMatchOnFrequency1(partialMatch1); //in-place sort

				//Step6
				listofKwords1 = ListTopKWords1(partialMatch1, k);
				WriteToOutPutFile1(pathToOutputFile, line);
			}
		}

		
		static List<Tuple<int, string>> LoadFileToDict1(string path)
		{
			List<Tuple <int, string>> wordsfreqDict = new List<Tuple<int, string>>();
			var lines = File.ReadLines(path);
			foreach (var line in lines)
			{
				var temp = line.Split('\t');
				wordsfreqDict.Add(Tuple.Create(Int32.Parse(temp[0].Trim()), temp[1]));
			}
			return wordsfreqDict;
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

		static void sortPartialMatchOnFrequency1(List<Tuple<int, string>> partialMatch1)
		{
			//List<Tuple<int, string>> sortedPartialMatchOnFreq1 = new List<Tuple<int, string>>();
			partialMatch1.OrderByDescending(a => a.Item1);
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

		static void WriteToOutPutFile1(string path, string inputline)
		{
			using (StreamWriter writetext = new StreamWriter(path, true))
			{
				writetext.WriteLine("{0}:", inputline);
				foreach (var item in listofKwords1)
				{
					string line = string.Format("{0} ({1})", item.Item2, item.Item1.ToString());
					writetext.WriteLine(line);
				}
				writetext.WriteLine();
			}
		}
	}
}
