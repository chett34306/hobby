using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using OpenQA.Selenium;
using OpenQA.Selenium.Firefox;
using System.Threading;

namespace SeleniumDemo
{
	class Program
	{
		static void Main(string[] args)
		{
			IWebDriver driver = new FirefoxDriver();
			driver.Url = "http://www.google.com";
			var sbox = driver.FindElement(By.Id("lst-ib"));
			sbox.SendKeys("Praveen Chettypally");
			Thread.Sleep(2000);
			driver.FindElement(By.Name("btnK")).Click();
			var link = driver.FindElements(By.ClassName("r"))[0];
			link.Click();
			bool pagecontains = driver.PageSource.Contains("Praveen Chettypally");
			driver.Close();
			
		}
	}
}
