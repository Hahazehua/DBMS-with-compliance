

 
COMP3140-311
2024/11/18
Design Database For 





Content

1. Background
2. Objectives
3. Design and data(ETL)
a. ETL (Extarct)
b. ETL (Transform)
c. ETL (Load)
4. Reason for design/ normalization/how to manage the input data
a. Design
b. Normalization
c. How to manage the input data
5. Conclusions & Discussions
a. Limitations of your design
b. What difficulties did you overcome?
c. What should we have done at the beginning so that you can do it better?
d. Members’ Contributions  Who did what? 
1. Background:
As new compliance challenges arise, such as Evergrande’s Hengda debt and the bankruptcy of Silicon Valley Bank, it becomes crucial to proactively identify potential compliance issues. Our group is embarking on a project to create a comprehensive database for a Compliance Management System (CMS) focused on stock data. This initiative is driven by our intrinsic interest in the stock finance market and the availability of valuable stock data. After conducting a review of the relevant literature, we identified financial analysis—particularly stock trend prediction and financial question answering—as a crucial area of interest[1]. We believe that focusing on financial question answering can offer significant potential for compliance within the CMS framework. Our users can be banks, investment companies and governments who have the potential to use our database to monitor the trend of stocks. 

2. Objectives:
With advancements in AI and deep learning, detecting compliance issues has become more accessible. AI requires vast amounts of data to achieve optimal results. In this context, our database can assist users in utilizing stock data to train their models.

3. Design and data:
About this database design, we follow the ETL process, which is extract, transform and load data. We would like to discuss our building process by this principle.
a. ETL (Extarct)
The initial step is to collect the disparate stock data. The decision was taken to load data from the stock markets of Hong Kong, mainland China and the United States of America. This was on the grounds of familiarity with the former two, and the latter's status as the most influential market in the world. 
The data is primarily obtained through the Python library yfinance, which facilitates the download of market data from Yahoo! Finance's API.  
The yfinance module facilitates the acquisition of data in a straightforward manner, allowing for the utilization of Python for this purpose. However, the database requires the collection of disparate stock data and its categorization according to sector. In the initial stage, the data was collected according to the stock code, with categorization limited to the range 0-100. This approach is not optimal, as it is often unprecise. To address this issue, we have conducted a systematic crawl of sector data from the website (https://cn.tradingview.com/markets/stocks-hong-kong/sectorandindustry-sector/). 
By employing the requests and bs4 libraries, it is possible to obtain the content utilized on this webpage.  Furthermore, the find_all function enables the identification of a specific element within the page.  The names of the companies in the sector are then collated and incorporated into the Python code.  In total, the stock can be collected over a five-year period, broken down by sector.
 
Furthermore, the same methodology can be applied to collect analogous data from other regions, with minor modifications to the code.
Once the sector has been collected, the ETL process is initiated to facilitate the transformation of the data in order to align it more closely with the specific requirements of the user. Initially, the data is downloaded in its original form. 

However, the unprocessed data is not suitable for loading. The data set is devoid of the essential information, namely the sector name and stock code. In order to better align the data with our requirements, we have implemented a Python script to perform the necessary transformations. The stock data that cannot be obtained is eliminated by utilizing the command "if hist.shape[0] <= 1:". The addition of two new columns, designated 'Stock_name' and 'sector', respectively, enables the transformation of the data set. This method allows us to collate data for each stock within a given sector.
b.	ETL (Transform)
Transfrom collect data:
The subsequent step is to integrate the data. It is preferable to avoid the creation of an excessive number of tables within the database; therefore, we need to integrate them in to one csv file.
Integrated data
We mainly use Pandas module to integrate our data.
 
A for loop is employed to combine all data into a single file for each file in a given sector. This process allows for the consolidation of all stock data within a given sector.  
The better way to collect:
Nevertheless, this process is superfluous. An alternative approach would be to integrate all files directly and utilize the groupby function for categorization.  
In order to facilitate comparison with a specific stock within this sector, it is necessary to obtain the relevant sector data through calculation. Additionally, Python is employed for this purpose. The data is then categorized by the groupby function according to both the data and the sector. Subsequently, the volume should be multiplied by the sum of the high, low, close, and open prices, and then divided by the total volume.

 

 




To meet the needs of our database:
This methodology allows us to obtain a table of sector data for a given market. The objective is to establish a connection between the sector data and the entire Hong Kong stock market data set, which is represented by the Hang Seng Index. Furthermore, the same library can be utilized to install a five-year record of the Hang Seng Index.
 
A similar approach is employed with regard to the other markets in China and the USA. Ultimately, it is necessary to obtain data regarding the global stock market. Following the results of the literature review, it was decided that the MSCI index would be used to represent the global data, as the MSCI World Index is a comprehensive global equity index that represents the performance of large and mid-cap equities across 23 developed countries.
 
 

The data about compliance:
Furthermore, as a compliance database management system, our objective is to provide users with access to information such as policy, news, and anomaly stock data, which will assist them in analyzing compliance issues.
Pollicies data:
HongKong:The initial step is to collate the relevant policy documents from Hong Kong. The data is obtained through a process of crawling from the Hong Kong Exchanges and Clearing Limited website (https://www.hkex.com.hk/News/News-Release?sc_lang=en&DateFrom=2024-01-01&DateTo=2024-12-31&Category=&Category2=undefined).   

The utilisation of web crawling technology enables the expedient retrieval of policy data, facilitating the identification of a particular class within a given website. Adherence to the policy data facilitates the attainment of the compliance objective.  
In order to reduce redundancy and enhance database efficiency, this table employs a URL-based data structure, rather than a text-centric one. 
US: Similarly, data pertaining to American policy is obtained from the United States Securities and Exchange Commission (SEC) via an application programming interface (API), as the SEC provides open API access. The original data can be obtained directly by downloading it with the Python programming language.
 
Nevertheless, the issue arises from the fact that the data format is in the form of a JSON file. 
 
We try to collect the news in one more other from and we would like to try to discuss upload this JSON file to our database in next part of the report. 
By using yfinance newsapi-python module, gathering news and policy data can be accessible. Next, we combine the part of web scraping and API to collect the news about the companies one by one, as the way we collected our stock data. By combining web scraping and API, we can download the us policy and news for different companies. 
 
China: Ultimately, our objective is to collate the pertinent policy data from the Shanghai Stock Exchange. (https://www.sse.com.cn/regulation/supervision/dynamic/). 
 
 
After collecting all policy data, we decide to integrate all policies data together, as policy is different from other stock data. Each policy may have a chain reaction, affecting different stocks in different regions. For example, the US policy can affect global stocks, so we put the policies and news from different regions together to better help our users conduct compliance analysis. Furthermore, the market serves to demonstrate that the policies in question originate from the government or other exchange centers.
 
Anomaly stock data:
The following step is to collate the anomaly data from the specified regions in order to assist the user in obtaining a review of companies that have compliance-related queries. In the first instance, with regard to the Chinese market, data is collected pertaining to the category of stocks designated as "special treatment" (ST), which are identified by the presence of one or more of the following characteristics: negative net profits reported over two consecutive years, failure to disclose annual reports, imminent dissolution, or undergoing reorganization, settlement, or bankruptcy liquidation [3]. The same methodology is employed for the collection of these data as that used for the China stock market data. The initial step involves obtaining a list of ST stocks from the website (https://q.stock.sohu.com/cn/bk_4842.shtml. Subsequently, the stock names are extracted and the pertinent data are collected). 
  
Subsequently, the same methodology employed for the integration of the one market stock data is utilized to get the China anomaly stock data for compliance request.
In the Hong Kong market, the selection of companies is based on the presence of compliance-related inquiries in the compliance report(https://login.hkcgi.org.hk/file2.php?content=publication&filename=2023%E5%B9%B4%E9%A6%99%E6%B8%AF%E4%B8%8A%E5%B8%82%E5%85%AC%E5%8F%B8%E5%90%88%E8%A7%84%E8%A7%82%E5%AF%9F.pdf&id=2562). 
The data identified as warranting further examination with respect to compliance are assembled. The aggregation of these data sets facilitates the collection of Hong Kong anomaly data. We use the similar ways to gather the American anomaly data (https://www.winston.com/en/blogs-and-podcasts/capital-markets-and-securities-law-watch/sec-greenlights-nasdaqs-proposed-rule-change-on-bid-price-compliance). 
c. ETL(Load)
After extracting and transforming data, we need to load it to our database. We do not use auxiliary software such as DBeaver, as we have done our data transformation in python and we do not need to use them.
We upload our data for the following steps:
（1）	Upload our file to the server. 
（2）	Create the database table. 
（3）	Transmit the file table to database table.
 
In accordance with the diverse array of stock data, the field types were designated as decimals, integers, and datetimes. Additionally, the primary key was established in alignment with the preceding ERD.
Following the transmission of data, a SELECT command is employed to facilitate an examination of the database, with the objective of confirming the configuration. 
The same process is then carried out in accordance with the previously established design, with the objective of avoiding unnecessary repetition. 

The 14 tables are transmitted to the database.
  

4. Reason for design/ normalization/how to manage the input data
a. Design
Once the data has been collected, it is necessary to create an Entity Relationship Diagram in order to facilitate the construction of the database management system. 
b. Normalization 
The initial topic of discussion is our data and normalization. The rationale behind the decision not to normalize the database can be attributed to two key factors. Firstly, the stock data does not exhibit any partial or transitive dependency, as each piece of information is dependent on the composite primary keys, which are Date and Stock or Sector. Secondly, the stock data is primarily comprised of price and quantity data, which cannot be divided and normalized in any meaningful way. Furthermore, the intention is not to apply denormalization the database, as the stock data is in high quality.
c.	How to manage the input data
However, when we add the column sector to the stock_data table, which produce partial dependency. We decided not to convert it to Second Normal Form to increase on more table, which can increase redundancy. 
Without the need to make further transformation, we can design our Entity Relationship Diagram with the following tables: HK_stock data, HK_sector data, HSI_index, CN_stock data, CN _sector data, CN _index, US_stock data, US _sector data, Nasdqa_index, CN_ Anomaly, US_ Anomaly, HK_ Anomaly, MSCI_world data and three region policies. 
For each region, it is easy to draw the ERD in linear sequence for the stock data part. We can easily connect HK_stock data, HK_sector data, HSI_index and connect them with MSCI_world data in the following ways. We can do the similar arrange for other regions. But the difficulty is how to arrange the anomaly and the policy data. 
 
Because policies are one of the most essential parts in compliance management system, and it can affect almost every table in the database, it is a challenge for us to arrange policy in our database. Moreover, some policies, especially about American policies, can influence the stocks’ price in the globe. In this situation, we need to take substantial consideration on policy with database management. The objective of our compliance system is to provide the tool to regulate compliance question, which is mainly related with the single stock. So, we ultimately decided to focus on region overall stock data. 
 
Therefore, we choose to construct our ERD as shown above. We achieve our compliance function by the following two ways: the first one is about the connection of policy and stocks. The second one is about the connection of stocks and Anomaly stock data, which can help user to summarize features of anomaly stocks. 
For the entire ERD, we mainly connect them by using composited keys, which consists of Date and Stock name or sector name. Firstly, we connect the policy table with three market stocks with Date. We commence with the HK_stocks, CN_stocks, and US_stocks, subsequently delineating the methodologies for establishing the date and stock name as the composited primary key. We then proceed to integrate the stock data with sector data, utilizing the foreign key Sector. Subsequently, the sector data is linked with the overall market index, including the Hang Seng index and NASDAQ index, through the utilization of the foreign key data. Ultimately, for each market index, a connection is established with the world index, thereby ensuring comprehensive consideration. Moreover, we establish a connection between the anomaly stock data and the local stock data, thereby reducing complexity and enhancing usability and reasonableness.
Finally , we will discuss the question of circular ERD. Our response to this question is ambivalent. Although it may result in data integrity issues, ambiguity in relationships, and increased complexity, we have elected to attempt its use, as it has the potential to yield certain advantages, particularly in the context of our stock compliance system (Designing a Circular ERD: A Comprehensive Guide to Database Modeling). One significant rationale for employing a circular ERD is the intricate interconnectivity between stock data. Articulating our ERD in a lucid manner through the use of a circular ERD can prove advantageous, particularly in the event of incorporating additional regional data in the future. Furthermore, it fosters flexibility in data management. Despite these potential benefits, we recognize the inherent risks associated with such a design.
Conclusions & Discussions
a. Limitations of your design
The first and biggest limitation of our database design is the source of data. All stock data is accessible, while the policy data is difficult to collect. Initially, we try to just scrab data from official organizations. However, we failed to get a full data from these official organizations website because they usually they have anti-crawling settings. Moreover, when we use API to collect policy data, the API has a limit on the number of downloads. We can not directly get the most effective and efficient policy data with the technology we have. Furthermore, because compliance management requires attention to more detailed aspects such as company financial reports, company policies, company reputation, corporate ethics, and company culture, it is difficult for us to obtain all such information and store it in our database in an appropriate manner on our own.
In addition, in our design, we just collect three region data. It is insufficient in this big data era to use advanced technology such as deep learning and artificial intelligence to analysis the compliance challenges.

b. What difficulties did you overcome?
The first problem we encountered was how to integrate the data. Since we downloaded thousands of data tables, we needed to present the data in our database reasonably. First, we tried to store all the stock data in thousands of tables by date in time tables. But we soon discovered that this storage method was just as inefficient as the previous solution. Finally, according to the definition of primary key, we found that we can use two complicated primary keys to make the value of each row have referential integrity.
Next, we encountered the problem of how to identify sectors according to stock types and collect data by sector. The data is then processed using a Python for loop, which enables the collective retrieval of data for each sector and the addition of a sector column for classification purposes.
Another question is how to deal with the impact of policies on all stocks because the influence of one policy can be substantial. We finally chose to return to the theme of our project, the compliance investigation of a single stock. Therefore, we finally chose to merge all policies into one table and then connect it only to the stock. 

c.	What should we have done at the beginning so that you can do it better?
Despite the extensive redundancy work conducted during this project, there is value in learning from it. Firstly, due to a lack of foundational knowledge regarding databases, a considerable amount of time and effort was expended on unnecessary data transformations and extractions. These included incomplete data transformations, the execution of superfluous transformations, and the loading of irrelevant data. It would be beneficial to gain a deeper understanding of the fundamental concepts of databases before attempting further optimization. Moreover, we are supposed to follow more about our design principle. We have experienced the process of uploading data but needing to drop tables repeatedly many times. We need to follow the step one by one to maximize our efficiency.

d.	Members’ Contributions  Who did what?
Harry Chen: I collate and integrate stock data from the Hong Kong, mainland China, and US stock markets through the ETL process, and utilize tools such as Python and Pandas for data conversion and analysis. Concurrently, I collate data pertaining to policy and anomalous stock activity, which is then utilized to facilitate compliance analysis. Ultimately, I am responsible for developing an entity relationship diagram to facilitate the management of this data, thereby enabling users such as banks, investment companies, and governments to monitor stock trends and identify potential compliance issues.
Chole Lok: Use python to collect stock data in China, search for policies related to the stock market, and jointly make ERD, report and ppt.
Elva Zeng: Use Python to collect US data. And jointly produced ERD, reports, ppt.
Bob Feng: I looked up some regulations and policies for some US stocks. I was responsible for the introduction part of our project, which basically introduced the overall idea of our project and a background story of our project and the goals we were going to achieve.









Source：
[1]: Li, Xiang, et al. "AlphaFin: Benchmarking Financial Analysis with Retrieval-Augmented Stock-Chain Framework." arXiv preprint arXiv:2403.12582 (2024).
[2]: Cheng, Xin, Hongyi Chen, and Yinggang Zhou. "Is the renminbi a safe-haven currency? Evidence from conditional coskewness and cokurtosis." Journal of International Money and Finance 113 (2021): 102359.
[3]: Li, Zhiyong, et al. "Predicting the risk of financial distress using corporate governance measures." Pacific-Basin Finance Journal 68 (2021): 101334.
Code:
China_stocks data
 

China_sector data:
 
China policy data:
 
HK Anomaly data
 






HSIx data
 
HK policy data:
 



US policy data:
 
US sector data:
 
US news data:
 









world data:
 
 
Integrate news data:
 







cleaning data:
 
Cleaning column
 



Integrate data:
 







MSCI data
 

Nasdqa data:
 





Input data in database:
 










integrate US data1:
 

integrate US data 2:
 
  
 

 
 

