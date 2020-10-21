#lib.py
from bs4 import BeautifulSoup

def getPostThumbs(posts):
  postContents = [BeautifulSoup(post[6], "html.parser") for post in posts]
  images = []

  for postContent in postContents:
    image = postContent.find('img')
    if not image:
      newTag = postContent.new_tag('img', src="/static/images/no-image.png")
      images.append(newTag)
    else:
      images.append(image)
    
  thumbs = [image['src'] for image in images]
  return thumbs