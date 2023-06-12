import requests
from bs4 import BeautifulSoup
import pandas as pd
import random
import re

HR = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/5370.36',
      'referer': 'https://www.google.com/'}
PARSE_LIST = [['https://virginiasports'], ['https://yalebulldogs']]


class Scraper():
    def __init__(self) -> None:
        self.log = []

    def get_page(self, url, get_links=False, virginiasports=False, yalebulldogs=False):
        self.log.append("Get Page...")
        # print("Get Page...")
        rand = random.randint(4, 10)
        page = requests.get(url, headers=HR, timeout=rand)
        soup = BeautifulSoup(page.text, 'html.parser')
        all_info = soup.find_all()
        if get_links:
            if virginiasports:
                all_info = soup.find_all('div', 'roster__image')
        if yalebulldogs:
            return soup
        return all_info

    def get_link(self, all_info, virginiasports=False, yalebulldogs=False):
        # print("Get Link...")
        self.log.append("Get Link...")
        link_list = []

        if virginiasports:
            for info in all_info:
                x = info.find('a')
                link = x.get("href")
                title = x.text
                link_l = [link, title.strip("\n")]
                link_list.append(link_l)
            return link_list

        elif yalebulldogs:
            for option in all_info.find_all('option'):
                x = option
                link = x['value']
                title = x.text.replace(" ", "")
                base = ('https://yalebulldogs.com/' + "/roster.aspx?rp_id=")
                link_l = [link, str(title.split("\r\n")[0]).replace(",", " ")]
                link_l[0] = base+link_l[0]

                link_list.append(link_l)
            return link_list

    def scrape(self, all_info, virginiasports=False, yalebulldogs=False):
        # print("Scrape...")
        self.log.append("Scrape...")
        names, tmp, dic = [], [], []
        lists = None
        if virginiasports:
            # print("Virginsport")
            self.log.append("Virginsport")
            for info in all_info:
                name = info.find("meta",  property="og:title")
                if name != None:
                    nm = name.get("content")
                    if nm not in names:
                        names.append(nm)
                        # print(nm)
                        self.log.append(nm)

                position = info.find("div",  class_="description")
                value = info.find("div",  class_="value")

                if position != None and value != None:
                    tmp.append(["Name", nm])
                    key = position.text
                    val = value.text
                    lists = [key, val]

                if lists not in tmp:
                    tmp.append(lists)

                if tmp not in dic:
                    dic.append(tmp)
            return names, dic

        elif yalebulldogs:
            # print("YaleBulldogs")
            self.log.append("YaleBulldogs")
            name, jursey_number, content = [], [], []
            # soup = self.get_page()

            all_info = all_info.find_all(
                "div", "sidearm-roster-player-header-details")
            for i in all_info:
                nm = i.find(
                    "span", "sidearm-roster-player-name").text.strip("\n")
                j_num = i.find(
                    "span", "sidearm-roster-player-jersey-number").text
                tmp = []
                for k in i.find_all("dl", "flex-item-1"):
                    key = k.find("dt").text
                    val = k.find("dd").text
                    tmp.append([key, val])
            tmp.append(['Name' , nm.replace("\n", " ")] )
            tmp.append(['Jersey Number', re.findall(r'\d+', j_num)[0]])
            tmp1, tmp2 = [], []
            for d in tmp:
                tmp1.append(d[0])
                tmp2.append(d[1])
            content.append(dict(zip(tmp1, tmp2)))
        
            return content
       

    def list_of_dic(self, dic):
        main = []
        for i in dic:
            tmp1, tmp2 = [], []
            for k in i:
                tmp1.append(k[0])
                tmp2.append(k[1])
            main.append(dict(zip(tmp1, tmp2)))
        return main

    def save_in_file(self, content, file_name, file_type="csv", virginiasports=False, yalebulldogs=False):
        # print(content)
        # print("Save In File...")
        # print(virginiasports, yalebulldogs)
        self.log.append(content)
        self.log.append("Save In File...")
        self.log.append([virginiasports, yalebulldogs])
    
        if virginiasports:
            ds = pd.DataFrame(content)
            
            ds.replace(pd.NA, "No Data", inplace=True)
          
            self.log.append(ds.shape)
       
            col = ['Name', 'Position', 'Height', 'Weight', 'Class', 'B/T', 'Hometown',
                   'Previous' 'School', 'High School', 'Instagram', 'Twitter', 'Phone', 'E-Mail']
            ds = ds.reindex(columns=col)
            print(ds.head())
            self.log.append(ds.head())

        elif yalebulldogs:
            ds = pd.DataFrame(content)
            
            col = ['Name', 'Jersey Number', 'Height',
                   'Weight', 'Class', 'Hometown', 'Highschool']
            ds = ds.reindex(columns=col)
            print(ds.head())
     
            self.log.append(ds.head())
            self.log.append(ds.shape)

        if file_type == "csv":
            ds.to_csv(file_name+".csv", index=False)
            output_file = file_name+".csv"

        elif file_type == "excel":
            ds.to_excel(file_name+".xlsx", index=False)
            output_file = file_name+".xlsx"
        elif file_type == "html":
            ds.to_html(file_name+".html", index=False)
            output_file = file_name+".html"
        elif file_type == "db":
            from sqlite3 import connect
            conn = connect(file_name+".db")
            ds.to_sql("Player Data", con=conn, index=False)
            output_file = file_name+".db"
        else:
            output_file = (f"File type {file_type} is currently not supported. or there is spelling mistake")
        self.log.append(output_file)
        return output_file

    def get_info(self, url, virginiasports=False, yalebulldogs=False):

        names, contents = [], []
        # print("Get Info...", virginiasports, yalebulldogs)
        self.log.append(("Get Info...","virginiasports:", virginiasports,"yalebulldogs:", yalebulldogs))
        if virginiasports:
            page = self.get_page(url, get_links=True, virginiasports=True)
            link_list = self.get_link(page, virginiasports=True)
            self.log.append(len(link_list))
            # link_list = link_list[:3]

            for url, _ in link_list:
                page = self.get_page(url, virginiasports=True)
                name, content = self.scrape(page, virginiasports=True)
                content = self.list_of_dic(content)
                self.log.append(content)
                self.log.append(name)
                names.append(name)
                contents.append(content)
            return contents

        elif yalebulldogs:
            page = self.get_page(url, get_links=True, yalebulldogs=True)
            link_list = self.get_link(page,  yalebulldogs=True)
            self.log.append(len(link_list))
      
            for ur, _ in link_list:
                self.log.append(ur)
                page = self.get_page(ur, yalebulldogs=True)
                content = self.scrape(page, yalebulldogs=True)
                self.log.append(['loop:', content])
                contents.append(content)
             

        return  contents

    def unpack(self, lista):
        tmp1, tmp2 = [], []
        self.log.append("Unpacking List.")
        self.log.append(["lista: ", lista])
        # if len(lista) == 2:
        for i in lista:

            tmp1.append(i[0][0])
            tmp2.append(i[0][1])
        # else : return lista
        return tmp1, tmp2

    def run_bot_virginiasports(self, url, file_name, file_type):
        self.log.append("Virginsport")

        content = self.get_info(url, virginiasports=True)
        two = []
        for i in content:
            two.append(i[0])
        self.log.append(content)
        outfile = self.save_in_file(
             content=two, file_name=file_name, file_type=file_type, virginiasports=True)
        print("Info scrapped and saved successfully. fpath: ", outfile)

    def run_bot_yalebulldogs(self, url, file_name, file_type):
        self.log.append("yalebulldogs")
        content = self.get_info(url, yalebulldogs=True)
        two = []
        self.log.append("Unpacking list")
        for i in content:
            two.append(i[0])


        outfile = self.save_in_file(
             content=two, file_name=file_name, file_type=file_type, yalebulldogs=True)
        if outfile == f"File type {file_type} is not supported.":
            pass
        else:
            print("Info scrapped and saved successfully. fpath: ", outfile)

    def save_log(self):
        if len(self.log) != 0:
            with open("log_file.txt", 'w') as f:
                for i in self.log:
                    f.write(str(i))
            print("Log file was saved")
def run():
    scrapper = Scraper()
    scrapper.save_log()
    # url ='https://virginiasports.com/sports/baseball/roster/'
    url = input("Enter URL: ")
    file_name = input("Enter Output File Name: ")
    extension = input("Enter Output File Exetension: ")
    if url.split(".")[0] in PARSE_LIST[0]:
        scrapper.run_bot_virginiasports(
            url, file_name=file_name, file_type=extension)
        scrapper.save_log()
    elif url.split(".")[0] in PARSE_LIST[1]:

        scrapper.run_bot_yalebulldogs(
            url, file_name=file_name, file_type=extension)
        scrapper.save_log()

    else:
        print("This tool can't extract values from sites other than, ", PARSE_LIST)
        print(url.split("."))
        scrapper.save_log()


if __name__ == "__main__":
    run()
    
