"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.insert(0, os.path.join(BASE_DIR, 'extra_apps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1)^6087)m5brjl5vb2_8j81j9-iozzxuo(@9l4-9o+va9qjed2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

# app 目录
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 新建app
    "apps.blog",
    # "apps.book",
    # "apps.movie",
    "apps.user",
    "apps.other",

    # 插件
    "extra_apps.xadmin",  # 后台
    "crispy_forms",
    "notifications",  # 消息通知
    "ckeditor",  # 富文本编辑器
    "haystack",  # 搜索
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'

# CKEditor配置项
CKEDITOR_CONFIGS = {
    'comment_ckeditor': {
        'toolbar': 'custom',
        'toolbar_custom': [
            ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript'],
            ["TextColor", "BGColor", 'RemoveFormat'],
            ['NumberedList', 'BulletedList'],
            ['Link', 'Unlink'],
            ["Smiley", "SpecialChar", 'Blockquote', 'CodeSnippet'],
        ],
        'width': 'auto',
        'height': '180',
        'tabSpaces': 4,
        'removePlugins': 'elementspath',
        'resize_enabled': False,

        'extraPlugins': ','.join(['codesnippet', 'uploadimage', 'widget', 'lineutils', ]),
    },

    'default': {
        'toolbar': 'custom',
        'toolbar_custom': [
            ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript'],
            ["TextColor", "BGColor", 'RemoveFormat'],
            ['NumberedList', 'BulletedList'],
            ['Link', 'Unlink'],
            ["Smiley", "SpecialChar", 'Blockquote'],
        ],
        'width': 'auto',
        'height': '180',
        'tabSpaces': 4,
        'removePlugins': 'elementspath',
        'resize_enabled': False,
    }
}

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': "mysite",
        "USER": "root",
        "PASSWORD": "root",
        "HOST": "127.0.0.1",
    }
}

# 使用whoosh搜索引擎
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'apps.blog.whoosh_cn_backend.WhooshEngine',
        'PATH': os.path.join(BASE_DIR, 'whoosh_index'),
    },
}

# 当添加、修改、删除数据时，自动生成索引
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

# 搜索结果分页
HAYSTACK_SEARCH_RESULTS_PER_PAGE = 7

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/
# 中文
LANGUAGE_CODE = 'zh-Hans'
# 北京时间
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, '/static/')

# 静态文件路径
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

# 上传文件路径
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
#
#
#
# 文章列表 单页文章数量
ARTICLE_PAGINATE_BY = 8

# 书单影单分页数量
BOOK_MOVIE_PAGINATE_BY = 8

# 搜索结果分页
HAYSTACK_SEARCH_RESULTS_PER_PAGE = 7
