# Blog Publish Github Action

### GitHub Action that publishes blogs, when pushed to the GitHub repository, to the specified websites automatically.

This action parses the the github markdown (.md file) to the corressponding requirements of different blogging websites and publishes them.
This action is triggered by a push and can also be triggered manually.

### Supported Blogging Websites

- Dev.to
- Medium
- Hashnode

### Info

- Type of markdown we are using -> GitHub Markdown
- Only create blog post is supported. If you modify a blog post, the action will do nothing.
- Currently updating is not support for any of the blogging websites due to its complex nature and bad support in many blogging platforms. So if you want to update your blogs it is better to use the UI of that particular blogging website.
- If for some reason your blog didn't get published go the actions tab in GitHub, select the workflow on the left hand side and then select the job which failed to get more info about it using logs.

### Instructions

1. Create a new repository to which the blogs will be pushed.
2. Create github secrets which will store your medium/dev.to/hashnode apikey. It is not mandatory to put all the api keys. You can only store the API keys of the platforms that you wish to upload to.
3. You can have the following directory structure

```
project
└───.github
│   └───workflows
│       │   action.yml
│
└───media
│   │   profile.png
│   └───engineering
│       │   tesla.png
│       │   edison.jpeg
│       │   best_friends.jpeg
│
│───blogs
│   │   blog.md
│   └───engineering
│       │   scientist.md
│       │   ceo.md
│       │   mba.md
```

5. Copy the sample action.yml folder as provided in `.github/workflows` directory.

<details>
<summary>Sample action.yml file</summary>
<p>

```yaml
name: blog-publish-github-action
on: [push, workflow_dispatch]
jobs:
  devto-blog-publish:
    runs-on: ubuntu-latest
    steps:
      - name: Use blog publish github action for devto
        uses: aru31/blog-publish-action@master
        with:
          website: "devto"
          log_level: "info"
          token_github: ${{ secrets.GITHUB_TOKEN }}
          token: ${{ secrets.DEVTO_TOKEN }}

  medium-blog-publish:
    runs-on: ubuntu-latest
    steps:
      - name: Use blog publish github action for medium
        uses: aru31/blog-publish-action@master
        with:
          website: "medium"
          log_level: "info"
          token_github: ${{ secrets.GITHUB_TOKEN }}
          token: ${{ secrets.MEDIUM_TOKEN }}

  hashnode-blog-publish:
    runs-on: ubuntu-latest
    steps:
      - name: Use blog publish github action for hashnode
        uses: aru31/blog-publish-action@master
        with:
          website: "hashnode"
          log_level: "info"
          token_github: ${{ secrets.GITHUB_TOKEN }}
          token: ${{ secrets.HASHNODE_TOKEN }}
```

</p>
</details>

6. That's it you are good to go!

7. If you want to modify the action then fork the repository, make changes, and then replace the uses section with your `username/repo`.

### Assumption and Requirements

- For this to work, we require only one commit per single push. But one commit can have multiple number of blogs.
- It is required to use **\<img>** tags for any images in the **content/body** of the markdown.
  <br>
  **Example:** `<img src="../media/profile.png" alt="Profile Picture">`
- Blogs should be added to the blogs folder and any media should be added to the media folder. You can have as many sub folders within them as required.

## How do we support images

While writing a blog you can store the images in the media folder and reference them using relative paths. Once pushed the action parses the markdown file and replaces `<img src="../media/profile.png" alt="Profile Picture">` with `https://raw.githubusercontent.com/{Username}/{Repository}/{Branch}/media/profile.png`

All the images in GitHub are stored using raw URLs.

## Sample blog.md file

<details>
<summary>Sample blog.md file</summary>
<p>

````md
---
title: Title of the blog
description: Description of the blog
tags:
  - post
  - tag
cover_url: ../**/media/cover.jpg

# dev_to specific metadata
devto_series: "Linux"

# hashnode specific metadata
hashnode_publication_id: 6243f3afa8722ae0e658142d

# bool values, if False or not provided then the blog will not be published on that platform
publish_devto: True
publish_medium: True
publish_hashnode: True
---

Content/body of the markdown file.

Using images:
<img src="../media/google.png" alt="another tag" />

```python
def python():
  pass
```

**This is bold text**

_This is italic text_

`This is inline code`

[This is a link](www.google.com)

# Heading 1

##### Heading 5

- Bullet points

1. Number points
````

</p>
</details>

## Markdown Metadata Fields
| Markdown Metadata fields (Case sensitive) | Blogging websites supported | Use case                                                               | If not provided                        |
|-------------------------------------------|-----------------------------|------------------------------------------------------------------------|----------------------------------------|
| title                                     | dev.to/medium/hashnode      | Title of the blog                                                      | Set title: Untitled                    |
| description                               | dev.to/medium/hashnode      | description                                                            | NA                                     |
| tags                                      | dev.to/medium/hashnode      | Tags for the blog. Example #linux                                      | NA                                     |
| cover_url                                 | dev.to/medium/hashnode      | Cover URL of the blog                                                  | NA                                     |
| hashnode_publication_id                   | hashnode                    | Publish to a particular publication                                    | Blog on Hashnode will not be published |
| publish_devto                             | dev.to                      | Boolean field to specify if you want the blog to published on dev.to   | It will not be published on dev.to     |
| publish_medium                            | medium                      | Boolean field to specify if you want the blog to published on medium   | It will not be published on medium     |
| publish_hashnode                          | hashnode                    | Boolean field to specify if you want the blog to published on hashnode | It will not be published on hashnode   |

## To Do

- [ ] Support html format.
- [ ] Support update request for blogs.

### Features not supported

- Dev.to, medium
  - [Code Folding](https://gist.github.com/pierrejoubert73/902cc94d79424356a8d20be2b382e1ab) not supported.
- Hashnode
  - Use of tags.

## Developer Tips

- You can change the logging level incase you are debugging

## References
