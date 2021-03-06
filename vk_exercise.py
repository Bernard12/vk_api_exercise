#!/usr/bin/python
# -*- coding: utf-8 -*-
""" 
VK API, лайки и sqlite.

Уровень 1:
Написать программу, получающую самый залайканный пост на стене пользователя вконтакте через vk api.

Уровень 2:
Написать программу, скачивающую все посты на стене пользователя и кладущую их в базу данных sqlite3.

Уровень 3:
Написать программу, скачивающую все посты на стене пользователя и кладущую их в одну из баз данных:
	a. MongoDB
	b. PostgreSQL
	c. Oracle

"""

""" Начало задания внизу, там где написано Уровень 1"""
import vk #pip install vk

def get_most_liked_url(user_profile_url):


    session = vk.AuthSession(app_id='wasd12', scope="offline,wall")

    api = vk.API(session)

    """ 3. Получите из ссылки пользователя его id или domain, необходимые, чтобы найти его
			Документация по объекту пользователя поможет вам решить, что вам нужно (читайте: проще получить и использовать): id или domain.
			https://vk.com/dev/fields

	"""

    #user_id = ""
    #user_domain = ""

    """ 4. Получите объект пользователя используя метод
			https://vk.com/dev/users.get

			Здесь необходимо обратиться к api. Для этого мы используем обертку vk.
			Парочку примернов использования можно найти здесь: 
			https://pypi.python.org/pypi/vk/2.0.2
			(Внизу есть ссылка "Read full documentation", она там не просто так)

			Обертка vk api позволяет запрашивать методы api например так:
			api.users.get(<params>)
			Самое важное - знать какие и в какой форме подать параметры - это вы найдете в документации api.
 	"""

 #user
    user=api.users.get(user_id=29027980)

    print(user)


    """ 5. Получите записи со стены пользователя, используя https://vk.com/dev/wall.get

		Убедитесь, что получаете только записи пользователя user.
    """

    wall_posts = []
    dom=user_profile_url.split('/')[-1]
    for i in api.wall.get(domain=dom,count=100,offset=0):
        wall_posts.append(i)

    #for i in wall_posts:
    #    print(i)

    mx=-1
    #for i in wall_posts:
    #    print(i)

    for i in range(1,len(wall_posts)):
        if wall_posts[i]['likes']['count']>mx:
            mx=wall_posts[i]['likes']['count']
        #print(wall_posts[i]['likes'])
    print(mx)
    res=''
    for i in range(1,len(wall_posts)):
        if wall_posts[i]['likes']['count']==mx:
           # print('Most liked post is '+str(i)+'-th')
           res+='https://vk.com/'+dom+'?w=wall'+str(wall_posts[i]['to_id'])+'_'+str(wall_posts[i]['id'])
           res+='\n'
        #print('https://vk.com/'+dom+'?w=wall'+str(wall_posts[i]['to_id'])+'_'+str(wall_posts[i]['id']))

    """ 6. Отсортируйте список записей по количеству лайков.

			Может помочь: https://vk.com/dev/datatypes

		Найдите самый залайканный пост и выведите прямую ссылку на него.

    """
    most_liked = None

    most_liked_url = None

    return res
""" 
	Уровень 2: 

	1. Подключите модуль sqlite3

	2. Создайте локальную базу данных

	3. Создайте таблицу posts, содержащую все поля записи на стене вк

	4. Вставьте в таблицу все посты из wall_posts 

	5. Не забудьте сделать connection.commit()!

	6. Для душевного успокоения скачайте любой gui для sqlite, откройте с его помощью свою базу данных и тихо радуйтесь, глядя на скачанные записи.

	Уровень 3:

	1. Скачайте, установите и настройте базу данных по выбору

	2. Скачайте модуль для работы с ней через python

	3. Проделайте шаги Уровня 2 для новой базы данных.

"""
	

"""
	Уровень 1:


	1. Зарегистрируйте новое приложение VK типа standalone

		https://vk.com/editapp?act=create


	   	Поместите его ID и secret_key (каждый на отдельной строке) в файл api.key

		secret_key нельзя хранить и передавать открыто. Файл api.key должен быть в .gitignore!

"""

try:
    with open('api.key', 'r') as f:
        app_id = f.readline()
        secret_key = f.readline()
except:
    print("Put app_id and secret_key in file api.key")

""" Введите ссылку на профиль пользователя """
user_profile_url = "https://vk.com/btseytlin"

if __name__ == "__main__":
    print(get_most_liked_url(user_profile_url))
