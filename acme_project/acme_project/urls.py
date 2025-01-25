from django.contrib import admin
from django.urls import include, path
from django.conf import settings

# Импортируем функцию, позволяющую серверу разработки отдавать файлы.
from django.conf.urls.static import static


# Добавьте новые строчки с импортами классов.
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView

# К импортам из django.urls добавьте импорт функции reverse_lazy
from django.urls import include, path, reverse_lazy

handler404 = 'core.views.page_not_found'

urlpatterns = [

    path('', include('pages.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls')),
    path(
        'auth/registration/',
        CreateView.as_view(
            template_name='registration/registration_form.html',
            form_class=UserCreationForm,
            success_url=reverse_lazy('pages:homepage'),
        ),
        name='registration',
    ),
    path('birthday/', include('birthday.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    import debug_toolbar
    # Добавить к списку urlpatterns список адресов из приложения debug_toolbar:
    # urlpatterns += (path('__debug__/', include(debug_toolbar.urls)),)

    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),] + urlpatterns
    # такой костыль т.к. после перехода на вью классыперестал работать
