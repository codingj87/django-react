from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        """A string representation of the model."""
        return self.title

#EOF
# master 에서 수정
# 한번 더 수정
# 수정
# Rebase Test 3
# Rebase Test 4
# Rebase Test 5
# Rebase Test 6
# Rebase Test 7
# Rebase Test 8