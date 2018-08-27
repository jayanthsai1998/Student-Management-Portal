import os
import django

os.environ['DJANGO_SETTINGS_MODULE'] = "onlineproject.settings"
django.setup()

from onlineapp.models import *

def main():
    manager = College.objects
    query_sets = College.objects.all()
    print(query_sets)
    for query_set in query_sets:
        print(query_set)


if __name__ == "__main__":
    main()