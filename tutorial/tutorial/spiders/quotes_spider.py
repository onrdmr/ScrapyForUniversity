import scrapy
#from urllib import request
#import os

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    #file = open("quotes.txt", "a", encoding = "utf-8")
    start_urls = [
"http://people.scs.carleton.ca/~roth/comp4102a-18/"
    ]        
    
    def parse(self, response):
        table_cells = response.css("tr")
        print("number of elements are " , len(table_cells))
        for row_idx in range(2,len(table_cells)-1):
            table_cols = table_cells[row_idx].css("tr").css("td")
            #for cols_idx in len(table_cols):
            icon_name = table_cols[0].css("img::attr(src)").get()
            link_name_offset = table_cols[1].css("a::attr(href)").get()
            url_to_download = self.start_urls[0] + link_name_offset
            #request.urlretrieve(url_to_download, os.path.join(self.start_urls[0].split('/')[-1], link_name_offset))
            date = table_cols[2].css("td::text").get()
            descr = table_cols[3].css("td::text").get()

            print(row_idx, icon_name, link_name_offset, url_to_download, date, descr)

            yield {
                "icon_name" : icon_name,
                "filename" : link_name_offset,
                "url" : url_to_download,
                "date" : date,
                "desc" : descr
            }
