using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Interviews
{
	public class BoxOnSite
	{
		//design a class with 10 accounts, each account with $1000 balance/account, able to transfer within accounts.
		static Dictionary<Guid, double> accountsbalances = new Dictionary<Guid, double>();
		//@TODO: Account IDs need to be more predictable for testing and test functions

		public BoxOnSite()
		{
			for (int i = 0; i < 10; i++) //10 accounts given
			{
				Guid guid = Guid.NewGuid();
				if (!accountsbalances.ContainsKey(guid))
				{
					accountsbalances.Add(guid, 1000);
				}
			}
		}

		public void DisplayBalance(Guid guid)
		{
			foreach (KeyValuePair<Guid, double> kvpaccount in accountsbalances)
			{
				if (guid == kvpaccount.Key)
				{
					Console.WriteLine("The account {0} has balance {1}", kvpaccount.Key, kvpaccount.Value);
				}
				else { Console.WriteLine("The account doesn't match"); }
			}
		}

		public string TransferBalance(Guid SourceAccount, Guid TargetAccount, double amount)
		{
			int stateTracker = 0;
			if (SourceAccount != TargetAccount)
			{
				if (DoesAccountExist(SourceAccount) && CheckBalance(SourceAccount, amount))
				{
					accountsbalances[SourceAccount] -= amount;
					stateTracker += 1; //for withdrawal
				}

				if (DoesAccountExist(TargetAccount))
				{
					accountsbalances[TargetAccount] += amount;
					stateTracker += 1; //for deposit
				}
			}

			if (stateTracker == 2)
			{
				return "Transfer Successful";
			}
			return "Failure";

		}

		private bool CheckBalance(Guid SourceAccount, double Amount)
		{
			foreach (KeyValuePair<Guid, double> kvpaccount in accountsbalances)
			{
				if (SourceAccount == kvpaccount.Key)
				{
					if (Amount < kvpaccount.Value)
					{
						return true;
					}
					else
					{
						return false;
					}
				}
			}
			return false;
		}

		private bool DoesAccountExist(Guid account)
		{
			foreach (KeyValuePair<Guid, double> kvpaccount in accountsbalances)
			{
				if (account == kvpaccount.Key)
				{
					return true;
				}
			}
			return false;
		}

	}
}
