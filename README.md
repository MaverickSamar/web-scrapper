# web-scrapper
Scrapes articles from theverge.com

## Modules used :
BeautifulSoup4
datetime
sqlite3
requests
pandas

Creates a SQLite db file named article.db and a csv file in dd-mm-yy.csv format with all the articles links, title, author name and date of publishing.

# Output


['A classic keyboard returns as the hot-swappable, wireless WhiteFox Eclipse', 'Here are some must-have accessories for your Nintendo Switch', 'Meta adds 14 free games you can play over video calls inside Messenger', 'T-Mobile will provide free MLB.TV to customers through 2028', 'Microsoft’s Windows 365 Cloud PCs get more flexible, LG TV integration, and more', 'Discord is launching an in-app soundboard', 'The first big Wild Hearts update is beautiful and deadly', 'April Fools’ Day 2023: the best and cringiest pranks', 'Meta’s layoffs are reportedly ‘gutting’ its new customer service teams', 'Apple’s M2 Mac Mini with expanded 512GB storage is $110 off']
0:00-04:00', '2023-04-06T10:46:19-04:00', '2023-04-06T10:46:05-04:00', '2023-04-06T10:15:00-04:00']
               Post Link                   Author                       Date    
0   A classic keyboard returns as the hot-swappabl...  https://www.theverge.com/22912942/best-nintendo-switch-controllers-cases-chargers-hea2023/4/6/23672354/whi...               Jon Porter  2023-04-06T13:00:00-04:00    mes-messenger-video-calls', 'https://www.theverge.com/2023/4/6/23672572/t-mobile-mlb-tv-free-2028', 'https://ww
1   Here are some must-have accessories for your N...  https://www.theverge.com/2023/4/6/23672001/discord-soundboard-nitro-super-emoji-reactions-themes22912942/best-nintend...      Alice Newcome-Beill  2023-04-06T12:37:38-04:00    te-murakumo', 'https://www.theverge.com/2023/4/1/23665955/april-fools-day-2023-pranks-jokes-best-worst', 'https
2   Meta adds 14 free games you can play over vide...  https://www.theverge.com/2023/4/6/23671495/apple-m2-mac-mini-ipad-pro-adata-ps5-ssd-anker-deal-sale',2023/4/6/23672441/met...              Umar Shakir  2023-04-06T11:47:12-04:00    
3   T-Mobile will provide free MLB.TV to customers...  https://www.theverge.com/2023/4/6/23672572/t-m...                Emma Roth  2023-04-06T11:41:21-04:00    
4   Microsoft’s Windows 365 Cloud PCs get more fle...  https://www.theverge.com/2023/4/6/23672363/mic...               Tom Warren  2023-04-06T11:00:00-04:00    
6   The first big Wild Hearts update is beautiful ...  https://www.theverge.com/23671365/wild-hearts-...           Andrew Webster  2023-04-06T11:00:00-04:00                   Post Link                   Author                       Date
7   April Fools’ Day 2023: the best and cringiest ...  https://www.theverge.com/2023/4/6/23672354/whi...               Jon Porter  2023-04-06T13:00:00-04:002023/4/1/23665955/apr...            Thomas Ricker  2023-04-06T10:46:19-04:00    22912942/best-nintend...      Alice Newcome-Beill  2023-04-06T12:37:38-04:00
8   Meta’s layoffs are reportedly ‘gutting’ its ne...  https://www.theverge.com/2023/4/6/23672441/met...              Umar Shakir  2023-04-06T11:47:12-04:002023/4/6/23672420/met...                Emma Roth  2023-04-06T10:46:05-04:00    2023/4/6/23672572/t-m...                Emma Roth  2023-04-06T11:41:21-04:00
9   Apple’s M2 Mac Mini with expanded 512GB storag...  https://www.theverge.com/2023/4/6/23672363/mic...               Tom Warren  2023-04-06T11:00:00-04:002023/4/6/23671495/app...  Antonio G. Di Benedetto  2023-04-06T10:15:00-04:00 
