#lib.py
from bs4 import BeautifulSoup

def getPostThumbs(posts, type=0):
  if type == "user":
    postContents = [BeautifulSoup(post[-2], "html.parser") for post in posts]
  else:
    postContents = [BeautifulSoup(post[-1], "html.parser") for post in posts]
    
  images = []

  for postContent in postContents:
    image = postContent.find('img')
    if not image:
      if type == "user":
        newTag = postContent.new_tag('img', src="/static/images/userthumb.png")
      else:
        newTag = postContent.new_tag('img', src="/static/images/no-image.png")

      images.append(newTag)
    else:
      images.append(image)
    
  thumbs = [image['src'] for image in images]
  return thumbs