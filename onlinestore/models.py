from django.db import models


# Create your models here.

class AlbumTitleSuggestion(models.Model):
    """
    A model representing album title suggestions.

    This model is used to store album title suggestions provided by users.
    It contains two fields: 'title' and 'votes'.

    :param title: The title of the album suggested by the user.
    :type title: str
    :param votes: The number of votes received for this suggestion.
    :type votes: int

    Attributes:
        title (str): The title of the album suggested by the user. It is a character field
            with a maximum length of 255 characters.

        votes (int): The number of votes received for this suggestion. It is an integer field
            with a default value of 0, indicating that no votes have been received initially.

    :Methods:
        __str__(): Returns the string representation of the album title suggestion, which is
            the title itself. This method is used to display the suggestion in a human-readable
            format, such as in the admin interface or when printing the object.

    :Note:
        This model should be used to store and manage album title suggestions in the application.
    """

    title = models.CharField(max_length=255)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    


class Post(models.Model):
    """
    A model representing a blog post.

    This model is used to store blog posts created by users. It contains four fields: 'title',
    'body', 'signature', and 'date'.

    :param title: The title of the blog post.
    :type title: str
    :param body: The main content of the blog post.
    :type body: str
    :param signature: The signature or author's name associated with the blog post.
    :type signature: str
    :param date: The date and time when the blog post was published.
    :type date: datetime.datetime

    Attributes:
        title (str): The title of the blog post. It is a character field with a maximum length of 140 characters.

        body (str): The main content of the blog post. It is a text field, allowing longer text entries.

        signature (str): The signature or author's name associated with the blog post. It is a character field
            with a maximum length of 140 characters and has a default value of "RG Baby".

        date (datetime.datetime): The date and time when the blog post was published. It is a DateTime field
            representing the moment of publication.

    :Methods:
        __str__(): Returns the string representation of the blog post, which is its title. This method is used
            to display the post in a human-readable format, such as in the admin interface or when printing the object.

    :Note:
        This model should be used to store and manage blog posts in the application.
    """

    title = models.CharField(max_length=140)
    body = models.TextField()
    signature = models.CharField(max_length=140, default="RG Baby")
    date = models.DateTimeField()

    def __str__(self):
        return self.title