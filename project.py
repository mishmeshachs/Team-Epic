import click
import datetime

"""
    List of static users we are going to use temporarily
"""
users = [
    {"id": 1, "role": "admin", "email": "admin@gmail.com", "password": "admin"},
    {"id": 2, "role": "moderator", "email": "moderator@gmail.com", "password": "moderator"},
    {"id": 3, "role": "normal", "email": "normal@gmail.com", "password": "normal"},
         ]
comments = []


class Comment:
    def __init__(self, author, message):
        self.author = str(author)
        self.message = message
        self.time = datetime.datetime.now()

    def create(self):
        comment = {
            "author": self.author,
            "message": self.message,
            "time": self.time,
        }
        comments.append(comment)

        return comments


@click.command()
@click.option('--comment_id', prompt=True, help='eg Comment(your_id, "Your comment message")')
@click.option('--message', prompt=True, help='eg Comment(your_id, "Your comment message")')
def create_comment(id, message):
    comment = Comment(id, message)
    click.echo("Comments: %s" % Comment.create(comment))


def delete_comment(comment_id):
    for comment in comments:
        if comment.get("comment_id") == comment_id:
            comments.pop(comment)
            click.echo ("comment deleted")
    click.echo ("comment deleted")

if __name__ == '__main__':
    create_comment()

