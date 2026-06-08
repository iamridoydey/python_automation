import requests
import os

def list_of_pull_request(owner, repo):
    url= f"https://api.github.com/repos/{owner}/{repo}/pulls"
    response = requests.get(url)
    
    # Pull requst creator and how much pull request being made by the user
    pr_creators = {}
    
    # write the pull request in the file
    # with open("github-res.json", "w+") as file:
    #     file.write(response.text)
    if response.status_code == 200:
        
        # convert the response into json
        pull_requests = response.json()
        
        for pull_req in pull_requests:
            user = pull_req['user']['login']
            if user in pr_creators:
                pr_creators[user] += 1
            else:
                pr_creators[user] = 1
    
    return pr_creators
    
    
    


if __name__ == "__main__":
    pr_creators = list_of_pull_request("kubernetes", "kubernetes")
    
    print("[")
    for name, reqs in pr_creators.items():
        print(f"\t{{user: {name}, pull_reqs: {reqs}}}")
    print("]")