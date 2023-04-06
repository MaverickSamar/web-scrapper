from bs4 import BeautifulSoup
from bs4.element import Comment
import requests 
import pandas as pd
import sqlite3
from datetime import date

def dbConnection(finalData):
    connection = sqlite3.connect('article.db')

    c = connection.cursor()
    # Table Created
    c.execute("""CREATE TABLE articles (
    id integer,
    post_link text,
    title text,
    author text
    )""")

    print("table created")


    # Insert in the table
    finalData.to_sql('articles',connection,if_exists='replace',index=False)

    print('Data Inserted')

    #Retrieve data
    rDf = pd.read_sql("select * from articles",connection)
    print(rDf)

    connection.commit()

    connection.close()


def createCsv(finalData):
    today = date.today()
    Str = date.isoformat(today) + '.csv'
    print("String Representation", Str)
    print(type(Str))
    finalData.to_csv(Str)

def appendData(posts, authors, postLinks, dateOfPost):
    finalData = pd.DataFrame()
    data = []
    data = pd.DataFrame({
        "Title":posts,
        "Post Link":postLinks,
        "Author":authors,
        "Date": dateOfPost
        })
    finalData = finalData._append(data, ignore_index = True)

    createCsv(finalData)
    dbConnection(finalData)


def fillArrrays(soup, entry):
    title = []
    author = []
    dateOf = []
    link = []
    
    while True:    
        try:
            au = entry.find('author')
            author.append(" ".join(au.find('name')))
        except:
            author.append(" ")
            
        try:
            title.append(" ".join(entry.find('title')))
        except:
            title.append(" ")
        
        try:
            dateOf.append(" ".join(entry.find('published')))
        except:
            dateOf.append(" ")
            
        try:
            link.append(" ".join(entry.find('id')))
        except:
            link.append(" ")
        
        try:   
            # Next sibling of entry, here: entry 
            entry = entry.find_next_sibling('entry')
        except:
            break

    
    print(author)
    print(len(author))
    print(title)
    print(len(title))
    print(dateOf)
    print(len(dateOf))
    print(link)
    print(len(link))  

    appendData(title, author, link, dateOf)  



def main():

    url = "https://www.theverge.com/rss/index.xml"
        
    xml_data = requests.get(url).content

    soup = BeautifulSoup(xml_data, "xml")

    # Find all text in the data
    texts = str(soup.findAll(text=True)).replace('\\n','')

    entry = soup.find("entry")

    fillArrrays(soup, entry)

if __name__ == "__main__":
    main()
    
    
