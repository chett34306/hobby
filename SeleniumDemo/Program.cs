using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Threading;


namespace SeleniumDemo
{
	class Program
	{
		static void Main(string[] args)
		{
			string domainURL = "http://www.equityzen.com"; // "http://www.starbucks.com"; // "https://houze360.com";//"http://www.cnbc.com"; // "http://www.facebook.com"; //;
			WebCrawler.SimpleWebCrawler(domainURL);
		}
		
	}
}
