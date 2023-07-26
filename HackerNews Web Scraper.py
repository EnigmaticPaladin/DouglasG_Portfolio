import requests
from bs4 import BeautifulSoup
import pprint


# WEBSCRAPING - HACKERNEWS
#
# res = requests.get('https://news.ycombinator.com/news')
# soup = BeautifulSoup(res.text, 'html.parser')
# # print(soup)
# # print(soup.body)
# # print(soup.body.contents)
# # print(soup.find_all('div'))
# # print(soup.find_all('a'))
# # print(soup.title)
# # print(soup.a)
# # print(soup.find(id='score_35138319'))
# # print(soup.selector(id='score_35138319'))
# # print(soup.select('.score'))
# links = (soup.select('.titleline'))
# votes = soup.select('.score')
# # print(votes[0])
# #print(votes[0].get('id'))

# _____________________________________________________

# res = requests.get('https://news.ycombinator.com/news')
# soup = BeautifulSoup(res.text, 'html.parser')
# links = (soup.select('.titleline'))
# subtext = soup.select('.subtext')
#
#
# def sort_stories_by_votes(hnlist):
#     return sorted(hnlist, key= lambda k:k['votes'], reverse=True)
#
# def create_custom_hn(links, subtext):
#     hn = []
#     for idx, item in enumerate(links):
#         title = links[idx].getText()
#         href = links[idx].get('href', None)
#         vote = subtext[idx].select('.score')
#         if len(vote):
#             points = int(vote[0].getText().replace(' points', ''))
#             if points > 99:
#                 hn.append({'title': title, 'link': href, 'votes': points})
#     return sort_stories_by_votes(hn)
#
# pprint.pprint(create_custom_hn(links, subtext))
#

# Adding page 2 of HackerNews

res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/?p=2')
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')
links = (soup.select('.titleline'))
subtext = soup.select('.subtext')
links2 = (soup2.select('.titleline'))
subtext2 = soup2.select('.subtext')

mega_links = links + links2
mega_subtext = subtext + subtext2

def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key= lambda k:k['votes'], reverse=True)

def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)

pprint.pprint(create_custom_hn(mega_links, mega_subtext))

# --------------------------------------------------------------------



