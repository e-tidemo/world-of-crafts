from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from crafts_likes.models import Likes, LikeOrUnlike
from crafts_likes.serializers import LikeSerializer
from django.contrib.auth.models import User
from crafts_posts.models import Post
from django.shortcuts import render
from django.http import JsonResponse


class LikesList(generics.ListCreateAPIView):
    """
    List likes or create a like if logged in.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = LikeSerializer
    queryset = Likes.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LikesDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a like or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = LikeSerializer
    queryset = Likes.objects.all()

def index(request):
     

    likes = LikeOrUnlike.objects.all()
    postLiked = []
    try:
        for like in likes:
            if like.user.id == request.user.id:
                postLiked.append(like.post.id)
    except:
        postLiked = [] 
    return render(request, "network/index.html",{
        'likes':likes,
        'postLiked': postLiked


})# function for liking post
def like(request, post_id):
    post = Post.objects.get(pk=post_id)
    user = User.objects.get(pk=request.user.id)
    likePost = LikeOrUnlike(user=user, post=post)
    likePost.save()
    return JsonResponse({"message": "Liked"})

# function for unliking post
def unlike(request, post_id):
    post = Post.objects.get(pk=post_id)
    user = User.objects.get(pk=request.user.id)
    unlikePost = LikeOrUnlike.objects.filter(user=user, post=post)
    unlikePost.delete()
    return JsonResponse({"message": "Unliked"})