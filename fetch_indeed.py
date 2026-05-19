import requests
from bs4 import BeautifulSoup
import json

def fetch_indeed_jobs(query="cybersecurity remote", limit=10):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
    }
    url = f"https://www.indeed.com/jobs?q={query.replace(' ', '+')}&l=Remote"
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "html.parser")
    jobs = []

    for card in soup.select(".jobsearch-CardContainer")[:limit]:
        title = card.select_one(".jobTitle")
        company = card.select_one(".companyName")
        link = card.select_one("a")

        if title and company:
            jobs.append({
                "title": title.get_text(strip=True),
                "company": company.get_text(strip=True),
                "link": "https://www.indeed.com" + link["href"] if link else ""
            })

    return jobs

if __name__ == "__main__":
    jobs = fetch_indeed_jobs()
    print(json.dumps(jobs, indent=2))