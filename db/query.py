from datetime import datetime

from django.db.models import Q, Count, Avg
from pytz import UTC

from db.models import User, Blog, Topic


def create():
    '''
    Создание
    '''
    # Создать пользователя first_name = u1, last_name = u1.
    u1 = User(first_name ='u1', last_name ='u1')
    u1.save()
    # Создать пользователя first_name = u2, last_name = u2.
    u2 = User(first_name ='u2', last_name ='u2')
    u2.save()
    # Создать пользователя first_name = u3, last_name = u3.
    u3 = User(first_name ='u3', last_name ='u3')
    u3.save()
    # Создать блог title = blog1, author = u1.
    b1 = Blog(title = 'blog1', author = u1)
    b1.save()
    # Создать блог title = blog2, author = u1.
    b2 = Blog(title = 'blog2', author = u1)
    b2.save()
    # Подписать пользователей u1 u2 на blog1, u2 на blog2.
    b1.subscribers.add(u1, u2)
    b2.subscribers.add(u2)
    # Создать топик title = topic1, blog = blog1, author = u1.
    t1 = Topic(title = 'topic1', blog = b1, author = u1)
    t1.save()
    # Создать топик title = topic2_content, blog = blog1, author = u3, created = 2017-01-01.
    t2 = Topic(title = 'topic2_content', blog = b1, author = u3, created = '2017-01-01')
    t2.save()
    # Лайкнуть topic1 пользователями u1, u2, u3.
    t1.likes.add(u1, u2, u3)


def edit_all():
    '''
    Поменять first_name на uu1 у всех пользователей.
    '''
    User.objects.all().update(first_name="uu1")


def edit_u1_u2():
    '''
    Поменять first_name на uu1 у пользователей, у которых first_name u1 или u2.
    '''
    User.objects.filter(Q(first_name="u1")|Q(first_name="u2")).update(first_name="uu1")


def delete_u1():
    '''
    удалить пользователя с first_name u1.
    '''
    User.objects.filter(first_name="u1").delete()


def unsubscribe_u2_from_blogs():
    '''
    отписать пользователя с first_name u2 от блогов
    '''
    b1 = Blog.objects.get(title = 'blog1')
    b2 = Blog.objects.get(title = 'blog2')
    u = User.objects.get(first_name ='u2')
    b1.subscribers.remove(u)
    b2.subscribers.remove(u)


def get_topic_created_grated():
    '''
    Найти топики у которых дата создания больше 2018-01-01
    '''
    return Topic.objects.filter(created__gte='2018-01-01')


def get_topic_title_ended():
    '''
    Найти топик у которого title заканчивается на content
    '''
    return Topic.objects.filter(title__endswith='content')


def get_user_with_limit():
    '''
    Получить 2х первых пользователей (сортировка в обратном порядке по id)
    '''
    users = User.objects.all().order_by('-id')[:2]
    return users


def get_topic_count():
    '''
    7. Получить количество топиков в каждом блоге, назвать поле topic_count, отсортировать по topic_count по возрастанию.
    '''
    return Blog.objects.annotate(topic_count=Count('topic')).order_by('topic_count')


def get_avg_topic_count():
    '''
    8. Получить среднее количество топиков в блоге.
    '''
    return Blog.objects.annotate(topic_count=Count('topic')).aggregate(avg=Avg('topic_count'))


def get_blog_that_have_more_than_one_topic():
    '''
    Найти блоги, в которых топиков больше одного.
    '''
    return Blog.objects.annotate(topic_count=Count('topic')).filter(topic_count__gt=0)


def get_topic_by_u1():
    '''
    Получить все топики автора с first_name u1.
    '''
    return Topic.objects.filter(author__first_name='u1')


def get_user_that_dont_have_blog():
    '''
    Найти пользователей, у которых нет блогов, отсортировать по возрастанию id.
    '''
    return User.objects.filter(blog__isnull=True).order_by('id')


def get_topic_that_like_all_users():
    '''
    Найти топик, который лайкнули все пользователи.
    '''
    return Topic.objects.filter(likes__in=User.objects.all()).distinct()


def get_topic_that_dont_have_like():
    '''
    Найти топики, у которы нет лайков
    '''
    return Topic.objects.filter(likes__isnull=True)
