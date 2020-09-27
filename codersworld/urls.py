from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import homepage.views, news.views, accounts.views, \
    courses.views, books.views, blogs.views

urlpatterns = (
        [
            path("", homepage.views.homepage,
                 name="homepage"),
            path("news/", news.views.news, name="news"),
            path("courses/", courses.views.showCourses,
                 name="courses"),
            path("books/", books.views.showBooks,
                 name="books"),
          #   path("blogs/", blogs.views.showBlogs,
          #        name="blogs"),
            path("blogs/", include('blogs.urls')),
            path("register/", accounts.views.register,
                 name="register"),
            path("login/", accounts.views.login,
                 name="login"),
            path("logout/", accounts.views.logout,
                 name="logout"),
            path("admin/", admin.site.urls),
        ]
        + static(settings.STATIC_URL,
                 document_root=settings.STATIC_ROOT)
        + static(settings.MEDIA_URL,
                 document_root=settings.MEDIA_ROOT)
)
