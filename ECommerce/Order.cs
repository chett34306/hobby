using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ECommerce
{
	public class Order
	{
		public List<Tuple<string, int, double>> products = new List<Tuple<string, int, double>>();
		
		public void AddProductToOrder(string prodName, int prodQuant, double prodPrice)
		{
			products.Add(Tuple.Create(prodName, prodQuant, prodPrice)); //add a new product
			return;
			//throw new NotImplementedException();
		}

		public List<Tuple<string, int, double>>  RemoveProductFromOrder()
		{
			products.RemoveAll(item => item.Item1 == "iPad");
			return products;
			//throw new NotImplementedException();
		}

		public void ChangeQuantityInOrder()
		{
			throw new NotImplementedException();
		}
	}
}
