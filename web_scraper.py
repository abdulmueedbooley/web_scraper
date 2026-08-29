from bs4 import BeautifulSoup
import requests
import time


def find_jobs():
    html_text = requests.get('https://realpython.github.io/fake-jobs/').text
    soup = BeautifulSoup(html_text, 'lxml')

    jobs = soup.find_all("div", class_ = "card-content")

    for index, job in enumerate(jobs):
        company_name = job.find('h3', class_ = 'subtitle is-6 company').text
        job_title = job.find('h2', class_ = 'title is-5').text
        publish_date = job.find('p', class_ = 'is-small has-text-grey').text.strip()
        apply_link = job.footer.find_all('a')[1]['href'] # hypertext reference

        with open(f'python_job_postings/{index}.txt', 'w') as file:
            file.write(f'Company Name: {company_name} \n')
            file.write(f'Job Title: {job_title} \n')
            file.write(f'Publish Date: {publish_date} \n')
            file.write(f'Apply Link: {apply_link}')

        print(' ')

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting {time_wait} minutes....')
        time.sleep(time_wait * 60)