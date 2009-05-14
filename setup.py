from distutils.core import setup
from glob import glob
from os.path import dirname, join

MO_FILES = join(dirname(__file__), "LOCALE", "pt_BR")
data_files = [
    (MO_FILES,
     join(MO_FILES, "django.po"),
     join(MO_FILES, "django.mo")),
]

setup(name="django-webalbum",
      version="0.1",
      description="A simple picture album manager form django",
      long_description="django-webalbum is a simple picture manager for django,"
                       " which consists in organizing pictures into albums. \nIt "
                       "is possibile to add a watermark, select a cover picture "
                       "and an album highlight image.",
      license="MIT",
      platforms=["Any"],
      author="Rodolfo da Silva Carvalho",
      author_email="rodolfo@rcarvalho.eti.br",
      url="http://github.com/rcarvalho/django-webalbum/",
      packages=["webalbum", "webalbum.templatetags", "webalbum.feeds"],
      package_data={"webalbum": [
            "locale/pt_BR/LC_MESSAGES/django.po",
            "locale/pt_BR/LC_MESSAGES/django.mo",
            "templates/admin/webalbum/album/*.html"
            ]},
)

