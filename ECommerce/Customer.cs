using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ECommerce
{
	class Customer
	{
		private string firstname;
		private string lastname;
		private int customerid;

		public Customer(string fname, string lname, int custid)
		{
			firstname = fname;
			lastname = lname;
			customerid = custid;
			return;
		}
	}
}
