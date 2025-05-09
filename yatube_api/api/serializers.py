from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from posts.models import Comment, Follow, Post, Group, User


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field="username", read_only=True
    )

    class Meta:
        fields = "__all__"
        model = Post


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        fields = "__all__"
        model = Group


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field="username",
        read_only=True,
        default=serializers.CurrentUserDefault(),
    )
    post = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        fields = "__all__"
        read_only_fields = (
            "author",
            "post",
        )
        model = Comment


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field="username",
        default=serializers.CurrentUserDefault(),
        queryset=User.objects.all()
    )
    following = serializers.SlugRelatedField(
        slug_field="username", queryset=User.objects.all()
    )

    class Meta:
        model = Follow
        fields = "__all__"
        validators = (
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=(
                    "user",
                    "following",
                ),
                message="Вы уже подписаны на данного автора",
            ),
        )

    def validate(self, data):
        if self.context["request"].user == data["following"]:
            raise serializers.ValidationError(
                "Нельзя подписаться на самого себя"
            )
        return data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
