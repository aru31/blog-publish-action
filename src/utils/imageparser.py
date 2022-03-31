from bs4 import BeautifulSoup as BSHTML


def get_img_src(filename):
    """
    :return: imag src path parsed by Beautiful soup
    """

    with open(filename, 'r') as file:
        htmlText = file.read().replace('\n', '')
    soup = BSHTML(htmlText)
    images = soup.findAll('img')
    return images


def replace_with_url(filename):
    """
    :return: replace the src in ima tag with github raw url
    """

    github_username_and_repo = "aru31/test-blog-publish"
    github_branch = "master"
    image_list = get_img_src(filename)
    print(image_list)
    for relative_image_path in image_list:
        required_path = "media" + relative_image_path['src'].split("media", 1)[1]
        url = f"https://raw.githubusercontent.com/{github_username_and_repo}/{github_branch}/{required_path}"
        with open(filename, 'r') as file:
            filedata = file.read()

        # Replace the target string
        filedata = filedata.replace(relative_image_path['src'], url)

        # Write the file out again
        with open(filename, 'w') as file:
            file.write(filedata)
