# # your_project/celery.py
#
# from __future__ import absolute_import, unicode_literals
# import os
# from celery import Celery
#
# # Устанавливаем настройки Django для Celery
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_project.settings')
#
# app = Celery('my_project')
#
# # Используем строку конфигурации Celery
# app.config_from_object('django.conf:settings', namespace='CELERY')
#
# # Автоматически ищет задачи в файлах tasks.py приложений Django
# app.autodiscover_tasks()
