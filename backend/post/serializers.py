from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        # fields = (
        #     'id',
        #     'title',
        #     'content',
        # )

        model = Post

        fields = [f.name for f in Post._meta.fields]

# testing 에서 수정
# 한번 더 수정