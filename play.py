"""
checkout https://www.django-rest-framework.org/tutorial/1-serialization/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
import django
django.setup()

from api.models import Snippet
from api.serializers import SnippetSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


import sys


if sys.argv[1] == "0":
    print(Snippet.objects.all())

if sys.argv[1] == "1":
    print(Snippet.objects.all().delete())

if sys.argv[1] == "2":
    snippet = Snippet(title="foo", code='foo = "bar"\n')
    snippet.save()

    snippet = Snippet(title="hello world", code='print("hello, world")\n')
    snippet.save()



if sys.argv[1] == "3":
    snippet = Snippet.objects.filter(title="foo")[0]
    serializer = SnippetSerializer(snippet)
    print(serializer.data)
    content = JSONRenderer().render(serializer.data)
    print(content)


    # desirialize

    import io

    stream = io.BytesIO(content)
    data = JSONParser().parse(stream)

    serializer = SnippetSerializer(data=data)
    serializer.is_valid()
    # True
    serializer.validated_data
    # OrderedDict([('title', ''), ('code', 'print("hello, world")\n'), ('linenos', False), ('language', 'python'), ('style', 'friendly')])
    serializer.save()
    # <Snippet: Snippet object>


    # serializin query sets
    #serializer = SnippetSerializer(Snippet.objects.all(), many=True)
    #serializer.data
