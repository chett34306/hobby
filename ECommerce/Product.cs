using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ECommerce
{
	
	public class Product
	{
		public List<Tuple<string, double>> productCatalog = new List<Tuple<string, double>>
		{
			{Tuple.Create("iPad", 299.99) },
			{Tuple.Create("iPhone", 499.99) },
			{Tuple.Create("iWatch", 399.99) },
			{Tuple.Create("iMac", 999.99) },
		};
	}
}
