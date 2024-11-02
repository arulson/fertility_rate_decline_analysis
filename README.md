# fertility_rate_decline_analysis

We use a lasso regression to determine the causal factors of the fertility rate decline in various countries.

## Data Cleaning 
Initially merged daily income and GDP columns over country and year as they had the max number of countries
And then left join/merge on every other factor/indicator
GDP column was cleaned by multiplying by 1000 for datapoints which had “k” like 13.1k -> 13100
 
Specifically for wpp_clean_data before merging to main dataset:

1. Modified data type from character (chr) to numeric.
2. Filtered out unwanted (meaningless) columns.
3. Filtered out rows where country = "World" and Year = NA.
4. Scaled selected variables (denoted as thousand-unit) by multiplying their values by 1,000,
5.  and removed "thousand" from the column names.
 
Once merged, extracted data for 1990-2023 for train, valid and test dataset.
Merging was done using Python script and cleaning through excel.

### notes
60 cols initially
plotted correlations
mortality rate related chunks are highly correlated
we get correlationswith thresold 0.7 and remove cols that data that can be repeated. All done on excel.

this leaves 27 cols that are not too correlated
initially when lassoing, net reproduction rate was the most common one that is highly correlated with fertility rate. After removing it, we got better factors
We only plotted for top 10 countries. Whne we merge individiual factors, some factors had key issue (USA vs untied states of america). We did the data cleaning using open refine. fon the NaNs, we set thm to zero. We filter dates to 1990 to 2020. our test was 2020 to 2023. 

 
