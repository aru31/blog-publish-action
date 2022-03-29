import requests
import urllib


# Assumption here is that user pushes a single blog at a given time via a commit

all_commits = requests.get(
    "https://api.github.com/repos/aru31/test-blog-publish/commits")
latest_sha = all_commits.json()[0]["sha"]

latest_commit = requests.get(
    f"https://api.github.com/repos/aru31/test-blog-publish/commits/{latest_sha}")
latest_files = latest_commit.json()["files"]

for file in latest_files:
    if (file["status"] == "added") or (file["status"] == "modified"):
        get_file_name = file["filename"].split("/")
        if(get_file_name[-1].split(".")[-1] == "md"):
            #urllib.request.urlretrieve(file["raw_url"], get_file_name[-1])
            urllib.request.urlretrieve(file["raw_url"], "blog.md")
