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
        self.comment_id = generate_id(comments)
        self.author = str(author)
        self.message = message
        self.time = datetime.datetime.now()

    def create(self):
        comment = {
            "id": self.comment_id,
            "author": self.author,
            "message": self.message,
            "time": self.time,
        }
        comments.append(comment)

        return comments


@click.command()
@click.option('--user_id', prompt=True, help='eg Comment(your_id, "Your comment message")')
@click.option('--message', prompt=True, help='eg Comment(your_id, "Your comment message")')
def create_comment(user_id, message):
    click.echo("CREATE COMMENT")
    comment = Comment(user_id, message)
    click.echo("Comments: %s" % Comment.create(comment))


@click.command()
@click.option('--comment_id', prompt=True, help='eg Comment(your_id, "Your comment message")')
@click.option('--new_message', prompt=True, help='eg Comment(your_id, "Your comment message")')
def edit_comment(comment_id, new_message):
    click.echo("EDIT COMMENT")
    for comment in comments:
        if comment.get("id") == comment_id:
            comment["message"] = new_message
            click.echo(" Edited Comment: %s" % comment)


def generate_id(comments_list):
    if comments_list:
        return comments_list[-1] + 1
    return 1


if __name__ == '__main__':
    create_comment()
    edit_comment()



