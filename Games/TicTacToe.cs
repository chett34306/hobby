using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Games
{
	public static class TicTacToe
	{
		public static int[] boardInit = new int[9];
		public static int player1;
		public static int player2;
		public static string player1Name;
		public static string player2Name;
		public static Dictionary<int, int> boardValues = new Dictionary<int, int>();
		public static int totalMoves = 0;
		public static void ShowGameBoard()
		{
			Console.WriteLine("Board location and player moves, -1 shows moves not done yet");
			foreach (KeyValuePair<int,int> item in boardValues)
			{
				Console.WriteLine("{0},{1}", item.Key.ToString(), item.Value.ToString());
			}
		}

		public static void InitializeGameBoard()
		{
			Console.WriteLine("*******Welcome to TIC-TAC-TOE Game********");
			//It's easier with int[] to calcualte win/lose
			for (int i = 0; i < boardInit.Length; i++)
			{
				boardInit[i] = -1;
			}

			//It's easier to keep track of the board, player values with dict object
			for (int i = 0; i < boardInit.Length; i++)
			{
				if (!boardValues.ContainsKey(i))
				{
					boardValues.Add(i, -1);
				}
			}
		}

		public static void InitializePlayers(int playerrep1, int playerrep2)
		{
			if (playerrep1 < 0 && playerrep1 > 1) return;
			if (playerrep2 < 0 && playerrep2 > 1) return;
			player1 = playerrep1;
			player2 = playerrep2;
			Console.WriteLine("Starting a new game with 2 new players");
			Console.WriteLine("Enter player1 name:");
			player1Name = Console.ReadLine();
			Console.WriteLine("Enter player2 name:");
			player2Name = Console.ReadLine();
		}

		public static void ShowWinBoard()
		{
			Console.WriteLine("Showing the Win Board");
			foreach (KeyValuePair<int, int> locplayermovepair in boardValues)
			{
				Console.WriteLine("{0},{1}", locplayermovepair.Key.ToString(), locplayermovepair.Value.ToString());
			}
		}

		public static void ShowDrawBoard()
		{
			Console.WriteLine("Showing the Draw Board");
			foreach (KeyValuePair<int, int> locplayermovepair in boardValues)
			{
				Console.WriteLine("{0},{1}", locplayermovepair.Key.ToString(), locplayermovepair.Value.ToString());
			}
		}

		public static int CheckWinBoard()
		{
			if ((boardInit[0] == player1 && boardInit[1] == player1 && boardInit[2] == player1) || //horizontal1
				(boardInit[0] == player1 && boardInit[4] == player1 && boardInit[8] == player1) || //diagonal1
				(boardInit[0] == player1 && boardInit[3] == player1 && boardInit[6] == player1) || //vertical1
				(boardInit[3] == player1 && boardInit[4] == player1 && boardInit[5] == player1) || //horizontal2
				(boardInit[2] == player1 && boardInit[4] == player1 && boardInit[6] == player1) || //diagonal2
				(boardInit[1] == player1 && boardInit[4] == player1 && boardInit[7] == player1) || //vertical2
				(boardInit[6] == player1 && boardInit[7] == player1 && boardInit[8] == player1) || //horizontal3
				(boardInit[2] == player1 && boardInit[5] == player1 && boardInit[8] == player1)     //vertical3
				)
			{
				return player1;
			}

			if ((boardInit[0] == player2 && boardInit[1] == player2 && boardInit[2] == player2) || //horizontal1
				(boardInit[0] == player2 && boardInit[4] == player2 && boardInit[8] == player2) || //diagonal1
				(boardInit[0] == player2 && boardInit[3] == player2 && boardInit[6] == player2) || //vertical1
				(boardInit[3] == player2 && boardInit[4] == player2 && boardInit[5] == player2) || //horizontal2
				(boardInit[2] == player2 && boardInit[4] == player2 && boardInit[6] == player2) || //diagonal2
				(boardInit[1] == player2 && boardInit[4] == player2 && boardInit[7] == player2) || //vertical2
				(boardInit[6] == player2 && boardInit[7] == player2 && boardInit[8] == player2) || //horizontal3
				(boardInit[2] == player2 && boardInit[5] == player2 && boardInit[8] == player2)     //vertical3
				)
			{
				return player2;
			}

			return -1;
		}

		public static bool CheckDrawBoard()
		{
			int player1Counter = 0;
			int player2Counter = 0;
			foreach (var item in boardInit)
			{
				if (item == player1)
				{
					player1Counter += 1;
				}

				if (item == player2)
				{
					player2Counter += 1;
				}
			}

			if (player1Counter + player2Counter == boardInit.Length)
			{
				if (CheckWinBoard() == -1) return true;
			}
			return false;
		}

		public static void Player1Move()
		{
			Console.WriteLine("Choose the move location from 0 - 8:");
			int x;
			while (!int.TryParse(Console.ReadLine(), out x) || !(x >= 0 && x <= 8))
				Console.WriteLine("The value must be of integer type between 0 - 8");
			while (x >=0 && x <=8)
			{
				if (boardInit[x] == -1)
				{
					boardInit[x] = player1;
					boardValues[x] = player1;
					totalMoves += 1;
					break;
				}
				else
				{
					Console.WriteLine("Choose another move location from 0 - 8:");
					x = Int32.Parse(Console.ReadLine());
				}
			}
		}

		public static void Player2Move()
		{
			Console.WriteLine("Choose the move location from 0 - 8:");
			int x;
			while (!int.TryParse(Console.ReadLine(), out x) && !(x >= 0 && x <= 8))
				Console.WriteLine("The value must be of integer type between 0 - 8");
			while (x >= 0 && x <= 8)
			{
				if (boardInit[x] == -1)
				{
					boardInit[x] = player2;
					boardValues[x] = player2;
					totalMoves += 1;
					break;
				}
				else
				{
					Console.WriteLine("Choose another move location from 0 - 8:");
					x = Int32.Parse(Console.ReadLine());
				}
			}
		}
	
	}
}
