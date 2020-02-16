
# China_CoronaVirus_Data_Miner

This simple python script collects data from the coronavirus status updates published by Tecent. 

Data source: https://news.qq.com/zt2020/page/feiyan.htm 

Note: It focuses on China only.

The script grabs the data and save them into three seperate csv files in the path where the script is stored. 

The data collected contain information at *country* , *province* and *prefecture* levels. For country level data, it collects all data from 1/17/2020 to the time being. For province and prefecture level data, it collects data for the day ONLY since there is no historical data available from the data source.


Fields of the country level output are as follows:
  1. Date (日期)
  2. Accumulated Confirmed (累计确诊)
  3. Suspect (疑似)
  4. Dead (死亡)
  5. Heal (治愈)
  6. Current Confirmed (现有确诊)
  7. Current Severe (现有重症)
  8. Death Rate (死亡率)
  9. Heal Rate (治愈率)


Fields of the province level output are as follows:
  1. Province (省)
  2. Daily Added Confirmed (新增确诊)
  3. Accumulated Confirmed (累计确诊)
  4. Dead (死亡)
  5. Healed (治愈)
  6. Death Rate (死亡率)
  7. Heal Rate (治愈率)

Fields of the prefecture level output are as follows:
  1. Province (省)
  2. Prefecture (市)
  3. Daily Added Confirmed (新增确诊)
  4. Accumulated Confirmed (累计确诊)
  5. Dead (死亡)
  6. Healed (治愈)
  7. Death Rate (死亡率)
  8. Heal Rate (治愈率)
  
To run the script, please make sure you are using python 3.x, and have libraries of pandas and requests installed.

A set of sample results is also provided.

# 武汉加油！ 中国加油！ #

#### Update 02-06-20: Removed "Suspect" as the original data do not provide such info for prefecture level.

#### Update 02-07-20: Added a new capability to get province level data.

#### Update 02-14-20: Added a new field '新增确认' for daily added confirmed cases, as the data source now provides such info.

#### Update 02-15-20: Added country level data (current + historical); Added death rate and heal rate to all levels.

⚠️ Disclaimer / Warning!
This repository/project is intended for Educational/Research Purposes ONLY.
Please do not use it for any other non-educational or non-research reason and definitely don't depend on it for anything important!

 
