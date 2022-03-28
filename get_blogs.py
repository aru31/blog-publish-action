import requests
import urllib


r = requests.get("https://api.github.com/repos/aru31/test-blog-publish/git/trees/master?recursive=1")
blogs = r.json()["tree"]

blog_path = f"https://github.com/aru31/test-blog-publish/blob/master/blogs"

get_all_blogs = list()

for blog in blogs:
    if blog["path"].startswith("blogs/"):
        get_all_blogs.append(blog["path"][6:])

print(get_all_blogs)

with open("bloglist.txt") as f:
    all_blogs = f.read().splitlines()

new_ones = list(set(get_all_blogs)^set(all_blogs))
print(new_ones)

with open("bloglist.txt", "a") as myfile:
    for blog in new_ones:
        myfile.write(f"{blog}\n")

# Download files
for blog in new_ones:
    urllib.request.urlretrieve(f"https://raw.githubusercontent.com/aru31/test-blog-publish/master/blogs/{blog}", blog)