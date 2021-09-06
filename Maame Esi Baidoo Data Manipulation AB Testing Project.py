import codecademylib
import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')
print(ad_clicks.head())
#Determine which utm_source is yielding the most views
utm_source_counts = ad_clicks.groupby("utm_source").user_id.count().reset_index()
print(utm_source_counts)
#People will view only if ad_click_timestamp is not null
ad_clicks["is_click"] = ad_clicks["ad_click_timestamp"].isnull()
print(ad_clicks.head())
clicks_by_source = ad_clicks.groupby(["utm_source", "is_click"]).user_id.count().reset_index()
print(clicks_by_source)
#Pivot the data
clicks_pivot = clicks_by_source.pivot(columns = "is_click", index = "utm_source", values = "user_id").reset_index()
print(clicks_pivot)
#Determine the percent of people who clicked on ads from each utm_source
clicks_pivot["percent_clicked"] = (clicks_pivot[True] / (clicks_pivot[True] + clicks_pivot[False])) * 100
print(clicks_pivot)
#Determine if approximately the same number of people were shown both ads in experimental_group
a_b_count = ad_clicks.groupby("experimental_group").user_id.count().reset_index()
print(a_b_count)
a_b_group = ad_clicks.groupby(["experimental_group", "is_click"]).user_id.count().reset_index()
print(a_b_group)
a_b_pivot = a_b_group.pivot(columns = "is_click", index = "experimental_group", values = "user_id").reset_index()
print(a_b_pivot)
a_b_pivot["a_b_percent_clicked"] = (a_b_pivot[True] / (a_b_pivot[True] + a_b_pivot[False])) * 100
print(a_b_pivot)
#Calculating the percentage of users who clicked on each A and B ad by day
a_clicks = ad_clicks[ad_clicks.experimental_group == "A"].reset_index(drop = True)
print(a_clicks)
b_clicks = ad_clicks[ad_clicks.experimental_group == "B"].reset_index(drop = True)
print(b_clicks)
a_clicks_by_day = a_clicks.groupby(["day", "is_click"]).user_id.count().reset_index()
print(a_clicks_by_day)
a_clicks_by_day_pivot = a_clicks_by_day.pivot(columns = "is_click", index = "day", values = "user_id").reset_index()
print(a_clicks_by_day_pivot)
#Performing calculations for percentage who clicked on ad a by day and keeping in new column
a_clicks_by_day_pivot["percent_clicked_by_day"] = (a_clicks_by_day_pivot[True] / (a_clicks_by_day_pivot[True] + a_clicks_by_day_pivot[False])) * 100
print(a_clicks_by_day_pivot)
b_clicks_by_day = b_clicks.groupby(["day", "is_click"]).user_id.count().reset_index()
print(b_clicks_by_day)
b_clicks_by_day_pivot = b_clicks_by_day.pivot(columns = "is_click", index = "day", values = "user_id").reset_index()
print(b_clicks_by_day_pivot)
#Performing calculations for percentage who clicked on ad b by day and keeping in new column
b_clicks_by_day_pivot["percent_clicked_by_day"] = (b_clicks_by_day_pivot[True] / (b_clicks_by_day_pivot[True] + b_clicks_by_day_pivot[False])) * 100
print(b_clicks_by_day_pivot)
#Ad B has more people clicking on the Ad for each day than Ad A.