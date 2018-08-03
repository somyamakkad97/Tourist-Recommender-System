# Tourist-Recommender-System

Aim to develop a personalized travel planning system that simultaneously considers all categories of user requirements and provides users with a travel schedule planning service.This will enable the user in finding what they are looking for, easily without spending time and effort.
The recommender system will filter irrelevant options and provide personalised and relevant information to each particular user, matching the characteristics of tourism attractions,hotels etc. with the user needs. This also takes into consideration the distance of each tourist attraction from the user’s location and provides the recommendations accordingly.

## Dataset Extraction
Web Scraping is a technique employed to extract large amounts of data from websites whereby the data is extracted and saved to a local file. Python provides a framework called Scrapy, is used to efficiently extract data from websites. Data of best tourist places in Jaipur is extracted from https://www.trawell.in/rajasthan/jaipur/places-to-visit-things-to-do . Dataset contains title, category, distance(from railway station), duration, nearby places, rating etc

## Location API
Google maps location API is implemented which helps in finding the distance between the users location and tourist spot he/she wants to visit. This also helps in recommending the tourist places according to their distance from users location. Places which are closer to user might be given more preference.

## Content Based Filtering
Content-based filtering is used to calculate a degree of similarity between the users and the items to be recommended. The process is carried out by comparing the features of the item with respect to the user’s preferences. 
The output of the comparison process is usually an overall performance score, which indicates the degree of matching between the user’s profile and each alternative.  Weighted Rating of the places is calculated, cosine similarity is used to correlate the user preferences with the category of the place and the distance api is used to find the distance and duration of the shortlisted places from the user’s location.

## Collaborative Filtering
Collaborative filtering techniques are recommendation methods based on the opinions of a set of users.The methods based on items predict the interest of the user on an activity a considering the evaluation that this user has given to similar activities(defined as those that have been positively rated along with a by many users).New places are recommended to the user based on his/her rating history by calculating his similarity with the other users, finding the K- Nearest Neighbours and thus giving the Top Recommendations.Therefore, the main objective of our collaborative filtering techniques is to find users similar to the current one, so that the system can recommend him/her activities that were considered interesting by those similar users.



 


