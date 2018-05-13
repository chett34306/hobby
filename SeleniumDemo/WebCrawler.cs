using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using OpenQA.Selenium;
using OpenQA.Selenium.Firefox;
using OpenQA.Selenium.Chrome;

using System.Net;

namespace SeleniumDemo
{
	static class WebCrawler
	{
		public static IWebDriver driver = new ChromeDriver(); //FirefoxDriver();
		public static List<Tuple<string, bool, string, DateTime>> urls = new List<Tuple<string, bool, string, DateTime>>();
		public static string justDomain;
		public static int visitedUrlCounter = 0;
		public static List<string> visitedUrls = new List<string>();
		public static int newUrlCounter = 0;
		public static List<string> newUrls = new List<string>();

		//Design WebCrawler for a given site. 
		//Req1.Navigate all the web pages under a domain, capture response code, error codes.
		public static void SimpleWebCrawler(string domainUrl)
		{
			Uri uri = new Uri(domainUrl);
			string[] uriParts = uri.Host.Split('.');
			if (uriParts.Length == 3)
			{
				justDomain = string.Format("{0}.{1}", uriParts[1], uriParts[2]);
			}
			else if (uriParts.Length == 2)
			{
				justDomain = string.Format("{0}.{1}", uriParts[0], uriParts[1]);
			}

			GetURLs(domainUrl);
			driver.Close();
			driver.Quit();
		}

		static void GetURLs(string domainUrl)
		{
			driver.Url = domainUrl;
			try
			{
				var aElements = driver.FindElements(By.TagName("a"));
				foreach (IWebElement a in aElements)
				{
					string ahref = a.GetAttribute("href");
					if (ahref.ToLower().Contains(justDomain))
					{
						VisitURL(ahref);
					}
				}
			}
			catch (Exception ex)
			{

			}
			//driver.Quit();
			//driver.Close();
		}
		static void VisitURL(string url)
		{
			var tuple = urls.Find(s => s.Item1 == url);
			if (tuple == null) //tuple.Item1.ToString() != url)
			{
				HttpWebRequest webRequest = (HttpWebRequest)WebRequest
										   .Create(url);
				webRequest.AllowAutoRedirect = false;
				HttpWebResponse response = (HttpWebResponse)webRequest.GetResponse();
				urls.Add(Tuple.Create(url, true, response.StatusCode.ToString(), DateTime.Now));
				newUrlCounter += 1;
				newUrls.Add(url);
				driver.Url = url;
				GetURLs(url);
			}
			else
			{
				visitedUrlCounter += 1;
				visitedUrls.Add(url);
			}
			//var tuple = urls.Find(s => s.Item1 == "http://wwww.google.com");
			//if (tuple.Item1.ToString() == "http://wwww.google.com")
			//{
			//	urls[0] = Tuple.Create("http://wwww.starbucks.com", true, "200OK", DateTime.Now);
			//	Console.WriteLine("First element of List after update {0}", urls[0]);
			//}
		}
	}
}
