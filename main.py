
import requests


from bs4 import BeautifulSoup

import pandas as pd

books = []

for i in range(1,5):
  url = f"https://internshala.com/jobs/software-development-jobs/page-{i}.html"
  response = requests.get(url)
  response = response.content
  soup = BeautifulSoup(response, 'html.parser')
  jobs = soup.find_all('div', {'class': 'individual_internship'})
  result = []
  for job in jobs:
        title = job.find('h4').text.strip()
        role = job.find('h3').text.strip()
        link = job.find('a').get('href')
        result.append({
            'title': title,
            'link': "https://internshala.com/" + link,
            'role': role
        })
    

df = pd.DataFrame(result, columns=['title', 'role', 'link'])
df.to_csv('jobs.csv')