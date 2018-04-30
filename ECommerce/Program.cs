using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ECommerce
{
	class Program
	{
		static void Main(string[] args)
		{
			//Put a basic design of ECOMMERCE
			//Product, Variation, Pricing Class
			//Cart Class
			//Users Class
			//Profile Class - Payments types, Payment Addresses Shipping Addresses
			//Payments class - add, removed, update payments types
			//Promos class -- codes, etc.
			//Queuing System for order work flow. -- add orders, process, ship from fulfillment, etc.
			//Tracking class for order tracking
			//Order class - Order, line items, costs, tax, shiping costs, total.

			//Step0: Login/Auth
			//Step1: Users chooses products from product catalog.
			//Step2: Add Product(s) to Cart
			//Step3: Add/Select payment type
			//Step4: Add/Select shipping address
			//Step5: Confirm the order.

			Customer c = new Customer("Praveen", "chettypally", 1);
			Product p = new Product();
			Order order = new Order();
			//add 1st product from catalog
			string prodName = p.productCatalog[0].Item1;
			double prodPrice = p.productCatalog[0].Item2;
			int prodQuantity = 1;
			order.AddProductToOrder(prodName, prodQuantity, prodPrice);
			//add 1st product from catalog
			prodName = p.productCatalog[1].Item1;
			prodPrice = p.productCatalog[1].Item2;
			prodQuantity = 1;
			order.AddProductToOrder(prodName, prodQuantity, prodPrice);


		}
	}
}