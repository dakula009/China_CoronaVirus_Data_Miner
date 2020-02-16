
# China_CoronaVirus_Data_Miner

This simple python script collects data from the coronavirus status updates published by Tecent. 

Data source: https://news.qq.com/zt2020/page/feiyan.htm 

Note: It focuses on China only.

The script grabs the data and save them into two seperate csv files in the path where the script is stored.

The data collected contain information at both *province* and *prefecture* levels.

Fields of the province level output are as follows:
  1. Province (省)
  2. Daily Added Confirmed (新增确认)
  3. Confirmed (确认)
  4. Dead (死亡)
  5. Healed (治愈)

Fields of the prefecture level output are as follows:
  1. Province (省)
  2. Daily Added Confirmed (新增确认)
  3. Prefecture (市)
  4. Confirmed (确认)
  5. Dead (死亡)
  6. Healed (治愈)
  
To run the script, please make sure you are using python 3.x, and have libraries of pandas and requests installed.

A set of sample results is also provided.

# 武汉加油！ 中国加油！ #

#### Update 02-06-20: Removed "Suspect" as the original data do not provide such info for prefecture level.

#### Update 02-07-20: Added a new capability to get province level data.

#### Update 02-15-20: Added a new field '新增确认' for daily added confirmed cases, as the data source now provides such info.

⚠️ Disclaimer / Warning!
This repository/project is intended for Educational/Research Purposes ONLY.
Please do not use it for any other non-educational or non-research reason and definitely don't depend on it for anything important!

 
