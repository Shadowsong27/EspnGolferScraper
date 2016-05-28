'''
This script is based on Wang Zexin's idea.
'''

from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv

names = ['Jordan_Spieth', 'Rory_Mcilroy', 'Jason_Day', 'Rickie_Fowler', 'Adam_Scott', 'Dustin_Johnson',
         'Justin_Rose', 'Bubba_Watson', 'Henrik_Stenson', 'Hideki_Matsuyama', 'Tiger_Woods', 'Louis_Oosthuizen',
         'Phil_Mickelson', 'Branden_Grace', 'Matt_Kuchar', 'Sergio_Garcia', 'Jimmy_Walker', 'Patrick_Reed',
         'Brooks_Koepka', 'Brandt_Snedeker', 'Jim_Furyk', 'Paul_Casey']
IDs = ['5467', '3470', '1680', '3702', '388', '3448', '569', '780', '576', '5860', '462', '1293',
       '308', '4383', '257', '158', '446', '5579', '6798', '1222', '153', '72']

years = ['2016','2015','2014','2013','2012','2011','2010']

result_url = "http://espn.go.com/golf/player/results/_/id/"
profile_url = "http://espn.go.com/golf/player/_/id/"

# construct csv header
with open(names[0] + ".csv", 'w') as f:
    writer = csv.writer(f, delimiter=",")
    writer.writerow(['Player Name',
                     'Country', 'Swings','Turned Pro',
                     'PGA Debut', 'College', 'Birth Date', 'Age','Birth Place','Weight'
                     'event_count','ave_scores','rank','fedex','money_rank','earnings',
                     'birdies','egales','driving_distance','putting','driving_accuracy','green_hit_in_regualtion','sand_saves','total_driving'
                     ])

    for i in range(22):
        # construct urls
        final_profile_url = profile_url + IDs[i]

        sock = urlopen(final_profile_url)
        profile_content = sock.read()

        # build soup
        profile_soup = BeautifulSoup(profile_content, 'html.parser')

        result = []

        # grab content
        # name
        result.append(names[i])

        # country, swings, turnpro [2-3]
        if len(profile_soup.ul) != 2:
            for li in profile_soup.ul:
                result.append(li.text)
        else:
            for li in profile_soup.ul:
                result.append(li.text)
                result.append("NA")




        [s.extract() for s in profile_soup('span')] # remove span tag
        for li in profile_soup.find_all('ul',{"class":"player-metadata floatleft"}):
            for element in li:
                if "(" in element.text:
                    temp = element.text.split("(")
                    result.append(temp[0]) # birth date
                    result.append(temp[1][-3:-1]) # age
                else:
                    result.append(element.text)

        # 2016 Overview: event_count,ave_scores,rank,fedex,money_rank,earnings [6]
        for tr in profile_soup.find_all('tr', {'class':"career"}):
            for td in tr:
                result.append(td.text)

        # birdies,eagles,Driving distance,putting,driving accuracy,green hit in regulation,sand saves,total driving [9]
        for strong in profile_soup.find_all('strong')[-8:]:
            result.append(strong.text.split(" ")[0])

        writer.writerow(result)


'''
Missing Values are taken care using Excels and R, this script simply write every piece of information into the csv file
without handling missing values
'''

