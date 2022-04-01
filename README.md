# Blog Publish Github Action
### GitHub Action that continuously publishes blogs, when pushed to the GitHub repository, to the specified websites automatically. 

This action parses the the github markdown (.md file) to the corressponding requirements of different blogging websites and publishes them.
This action is triggered by a push and can also be triggered manually.

### Supported Blogging Websites
- Dev.to
- Medium
- Hashnode

### Info
- Type of markdown we are using -> GitHub Markdown
- Only create blog post is supported.
- Currently updating is not support for any of the blogging websites due to its complex nature and bad support in many blogging platforms.

### Instructions
1. Clone the github action.
2. Create a new repository to which the blogs will be pushed.
3. Create github secrets which will store your medium/dev.to/hashnode apikey. It is not mandatory to put all the api keys.
4. Create the following directory structure.
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

5. Copy the action.yml folder as provided in .github/workflows directory.
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
          log_level: "debug"
          token_github: ${{ secrets.GITHUB_TOKEN }}
          token: ${{ secrets.DEVTO_TOKEN }}
          
  medium-blog-publish:
    runs-on: ubuntu-latest
    steps:
      - name: Use blog publish github action for medium
        uses: aru31/blog-publish-action@master
        with: 
          website: "medium"
          log_level: "debug"
          token_github: ${{ secrets.GITHUB_TOKEN }}
          token: ${{ secrets.MEDIUM_TOKEN }}

  hashnode-blog-publish:
    runs-on: ubuntu-latest
    steps:
      - name: Use blog publish github action for hashnode
        uses: aru31/blog-publish-action@master
        with: 
          website: "hashnode"
          log_level: "debug"
          token_github: ${{ secrets.GITHUB_TOKEN }}
          token: ${{ secrets.HASHNODE_TOKEN }}
```

6. Replace uses field everywhere with {username}/{repository action name}@{branch}.
7. That's it you are good to go!

### Assumption and Requirements
- For this to work, we require only one commit per single push. But one commit can have multiple number of blogs.
- It is required to use **\<img>** tags for any images in the **content/body** of the markdown.
<br>
**Example:** \<img src="../media/profile.png" alt="Profile Picture">
- Blog must be pushed into the blog folder and all the images should be pushed into the media folder. But there can be subfolders in these folders as shown above.

## To Do
- Support html format.
- Support update request for blogs.

### Features not supported
- Dev.to, medium
  - [Code Folding](https://gist.github.com/pierrejoubert73/902cc94d79424356a8d20be2b382e1ab) not supported.
- Hashnode
  - Use of tags.

## Developer Tips
- You can change the logging level incase you are debugging
