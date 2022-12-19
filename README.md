# Final Project Overview 


## Topic 

Markowitz-Optimal Portfolio Under Inflation in China


## Background 

Global inflation has reached its highest level since 2008 in recent years due to the shock of covid-19, supply chain disruptions, and increasingly tense international conditions. More than half of the countries with inflation-targeting frameworks have already exceeded their target rates. Inflation implies a prolonged period of rising price levels, which leads to a contraction in the real value of assets. The erosion of the real return of a portfolio caused by inflation is one of the fundamental risks faced by investors in financial markets. 


## Abstract

The main purpose of this research is to test the inflation hedging ability of different categories of important financial assets, for example, commodity futures, real estate, gold, industry stocks, Treasury Inflation-Protected Securities (TIPS) and so on, and then to select the assets that can effectively combat inflation risk to construct the inflation hedging portfolio using mean-variance model. First, 4 categories and 30 kinds of assets’returns are regressed on the expected and unexpected inflation rate. The results show that 8 of them do not have obvious inflation-hedging ability. And commodity futures of soybeans, PVC, and gold, spot gold, medicine and health care industry index, and real estate have significant hedging ability against inflation.
The remaining 22 assets are used to construct optimal mean-variance portfolio. In the case of no short-selling restrictions, investment in real estate plays an important role in the portfolio. The assumption of no shorting restriction makes investment more flexible and efficient. Investors are recommended to have investment of real estate.



## Data 

### Data Source 
All data is obtained from Choice, a data provider like Bloomberg in China.
The sample period for real estate date is from June 2011 to December 2021, for other date is from January 2010 to December 2021.
Real inflation data is proxied by the monthly year-on-year CPI data in the form of logarithms. Expected inflation data is one-period lagged one-year national bond's yield to maturity. 
Sixteen commodity futures' monthly settlement price data from Shanghai and Dalian futures exchange, 10 industry stocks' monthly closing price data from Hushen 300 industry index, spot gold's monthly closing price data from Shanghai Gold Exchange and monthly data on residential prices in Tier 1, Tier 2, and Tier 3 cities are obtained. Returns of these assets are calculated in the form of logarithmic monthly year-on-year yield.

### Data Management 
The research focues on the monthly data of no more than 30 types of financial or economical data. Even the raw data covers the period of several years, or is in daily basis, the size of each `.csv` file is no larger than 10M. Furthermore, most of the data needed in this research is a long-formatted and monthly time series data with the most simple structure. Therefore, it is not neccessary to implement an local or online database with SQL or other tools, and uploading these `.csv` files to Github would be a better way to share data within the team. 


## Reference 

[1]	Attie, Alexander P and Shaun K Roache (2009). "Inflation hedging for long-term investors". In: IMF Working Papers 2009(090).

[2]	Di, JP (2012). "Can real estate provide a hedge against inflation evidence from Chinese mainland". In: Chinese Real Estate 2, pp. 10–17.

[3]	Engsted, Tom and Carsten Tanggaard (2002). "The relation between asset returns and inflation at short and long horizons". In: Journal of International Financial Markets, Institutions and Money 12(2), pp. 101–118.

[4]	Fama, Eugene F. and G.William Schwert (1977). "Asset returns and inflation". In:Journal of Financial Economics 5(2), pp. 115–146. issn: 0304-405X.

[5]	Levin, Eric J, A Montagnoli, and RE Wright (2006). "Short-run and long-run determinants of the price of gold". In: World Gold Council. 

[6]	Yu, Mei et al. (2015). "A Study on the Optimal Portfolio Strategies Under Inflation". In: Journal of Systems Science and Information 3(2), pp. 111–132.

[7]	Qin, S, CY Qin, and RX Chen (2004). "The optimal portfolios model with inflation rate". In: Systems Engineering Theory Methodology Application 13(4), pp. 316–319. 

[8]	Rapach, David E (2002). "The long-run relationship between inflation and real stock prices".  In: Journal of Macroeconomics 24(3), pp. 331–351.



