# This file contains core classes for the web crawler.
# Author: Kai Xu
# Date: 05/11/2016


#from HTMLParser import HTMLParser   # for parsing HTML
from html.parser import HTMLParser
#from urlparse import urljoin        # for join two urls
from urllib.parse import urljoin
from urllib.request import urlopen         # for GET request
from helper import clean, get_domain, valid, contain_static
import requests


class HTMLParser(HTMLParser):
    '''
    HTML parser to fetch urls and show assests
    '''

    def handle_starttag(self, tag, attrs):
        '''
        Overrid of the default function to handle <a> and ??? tags
        TODO: update this comments when assest handle is done
        '''
        for key, val in attrs:
            if key == "href":
                if contain_static(val):             # handle static files
                    print ("-", val)                  # show the static file
                elif tag == "a":                    # handle links
                    url = urljoin(self.url, val)    # append relative path to the root path
                    url = clean(url)                # clean up url
                    if valid(url, self.domain):
                        self.urls.append(url)       # append url to the return list
                else:
                    pass


    def run(self, url):
        '''
        Run the parser and return links in this page
        '''
        self.url = url                  # save root path
        self.domain = get_domain(url)   # get and save domain
        self.urls = []                  # init return list

        # Open the url and parse it
        # FIXME:
        # There will be potential error when some website handshake is unsuccessful due to the SSL.
        # This is temporarly fixed by ignoring such failure but it should be further investiagted.
        try:
            response = urlopen(url)                 # request and get response
            html = response.read().decode("utf-8")  # read and encode response; NOTE: decode is necessary for unicode
            self.feed(html)                         # parse the html file in string format
        except KeyboardInterrupt:                   # deal with Ctrl-C
            exit()
        except:
            print ("Unexpected failure happens and the spider escapes.")

        return self.urls

class TitleParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.match = False
        self.title = ''

    def handle_starttag(self, tag, attributes):
        self.match = True if tag == 'title' else False

    def handle_data(self, data):
        if self.match:
            self.title = data
            self.match = False


class Spider(object):
    def __init__(self):
        self.to_visit = []
        self.visted = set([])
        self.parser = HTMLParser()

    def crawl(self, target_url):
        target_url = clean(target_url)      # clean target_url
        self.to_visit.append(target_url)    # put target_url to to_visit list
        urlcount = 0
        status200count = 0
        urlredirectcount = 0
        f = open("visitedurls.txt", "w")

        #header for output file.
        f.write("urlcount" + "\t")
        f.write("url" + "\t")
        f.write("response.status_code" + "\t")
        f.write("response.elapsed" + "\t")
        f.write("response.is_redirect" + "\t")
        f.write("\n")


        while len(self.to_visit) > 0:
            url = self.to_visit.pop(0)      # get next url
            urlcount = urlcount + 1

            response = requests.get(url)
            print("The spider is visiting:", url, response.status_code, response.elapsed, response.is_redirect)
            if response.status_code == 200:
                status200count = status200count + 1

            if response.is_redirect is True:
                urlredirectcount = urlredirectcount + 1

            # todo: add object to get and verify titles of each page
            # todo: add object to get and verify static cotent of each page
            # todo: add object to get and verify image count, sizes, on each page


            #write url, title to a file -- possibly expand.
            f.write(str(urlcount) + "\t")
            f.write(url+ "\t")
            f.write(str(response.status_code)+ "\t")
            f.write(str(response.elapsed)+ "\t")
            f.write(str(response.is_redirect)+ "\t")
            f.write("\n")


            print("Count of url crawled", urlcount)
            urls = self.parser.run(url)     # parse the url
            self.visted.add(url)            # add this visted url to visted list

            # Add urls from the praser to to_visit lits
            # When they are not visited or already in the to_vist list
            for url in urls:
                if url not in self.visted and url not in self.to_visit:
                    self.to_visit.append(url)

        print ("The spider has finished crawling the web at {url}".format(url=target_url))
        print("Total Count of urls crawled", urlcount)
        print ("Total Count of urls with status200count", status200count)
        print("Total Count of urls with redirected", urlredirectcount)

        f.write("The spider has finished crawling the web at {url}".format(url=target_url)+ "\n" )
        f.write("Total Count of urls crawled: \t" + str(urlcount) + "\n" )
        f.write("Total Count of urls with status200count: \t" + str(status200count)+ "\n" )
        f.write("Total Count of urls with redirected: \t" + str(urlredirectcount)+ "\n" )
        f.close()



if __name__ == "__main__":
    print ("I don't like snakes. Don't python me directly.")
