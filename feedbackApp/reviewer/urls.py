from django.urls import path
from .views import (
    ProductListCreateAPIView,
    ProductRetrieveUpdateDestroyAPIView,
    ReviewListCreateAPIView,
    ReviewRetrieveUpdateDestroyAPIView,
    RatingListCreateAPIView,
    RatingRetrieveUpdateDestroyAPIView,
    FeedbackListCreateAPIView,
    FeedbackRetrieveUpdateDestroyAPIView,
    CommentListCreateAPIView,
    CommentRetrieveUpdateDestroyAPIView,
    ReportListCreateAPIView,
    ReportRetrieveUpdateDestroyAPIView,
    ModerationListCreateAPIView,
    ModerationRetrieveUpdateDestroyAPIView,
    NotificationListCreateAPIView,
    NotificationRetrieveUpdateDestroyAPIView,
)

urlpatterns = [
    # Product endpoints
    path('products/', ProductListCreateAPIView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-detail'),

    # Review endpoints
    path('reviews/', ReviewListCreateAPIView.as_view(), name='review-list'),
    path('reviews/<int:pk>/', ReviewRetrieveUpdateDestroyAPIView.as_view(), name='review-detail'),

    # Rating endpoints
    path('ratings/', RatingListCreateAPIView.as_view(), name='rating-list'),
    path('ratings/<int:pk>/', RatingRetrieveUpdateDestroyAPIView.as_view(), name='rating-detail'),

    # Feedback endpoints
    path('feedback/', FeedbackListCreateAPIView.as_view(), name='feedback-list'),
    path('feedback/<int:pk>/', FeedbackRetrieveUpdateDestroyAPIView.as_view(), name='feedback-detail'),

    # Comment endpoints
    path('comments/', CommentListCreateAPIView.as_view(), name='comment-list'),
    path('comments/<int:pk>/', CommentRetrieveUpdateDestroyAPIView.as_view(), name='comment-detail'),

    # Report endpoints
    path('reports/', ReportListCreateAPIView.as_view(), name='report-list'),
    path('reports/<int:pk>/', ReportRetrieveUpdateDestroyAPIView.as_view(), name='report-detail'),

    # Moderation endpoints
    path('moderations/', ModerationListCreateAPIView.as_view(), name='moderation-list'),
    path('moderations/<int:pk>/', ModerationRetrieveUpdateDestroyAPIView.as_view(), name='moderation-detail'),

    # Notification endpoints
    path('notifications/', NotificationListCreateAPIView.as_view(), name='notification-list'),
    path('notifications/<int:pk>/', NotificationRetrieveUpdateDestroyAPIView.as_view(), name='notification-detail'),
]
