# Run Django shell (python manage.py shell) and then run the following commands...

# >>> import json
# >>> from blog.models import Post
# >>> with open('posts.json') as f:
# ...   post_json = json.load(f)
# ...
# >>> for post in post_json:
# ...   post = Post(title=post['title'], content=post['content'], author_id=post['user_id'])
# ...   post.save()
# ...
# >>> exit()
