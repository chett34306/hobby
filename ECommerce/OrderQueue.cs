using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ECommerce
{
	class OrderQueue
	{
		Queue<Order> orderQueue = new Queue<Order>();
		public void AddOrderToQueue(Order order)
		{
			orderQueue.Enqueue(order); //adding order to queue.
		}

		public void EditOrderInQueue()
		{
			throw new NotImplementedException();
		}

		public void RemoveOrderFromQueue()
		{
			throw new NotImplementedException();
		}

		public Order[] TotalOrdersInQueue()
		{
			return orderQueue.ToArray();
			//throw new NotImplementedException();
		}

		public void GetOrdersDetailsInQueue()
		{
			throw new NotImplementedException();
		}
	}
}
