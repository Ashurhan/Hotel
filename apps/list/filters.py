import django_filters
from .models  import *

class RoomsFilter(django_filters.FilterSet):
    class Meta:
        model=Rooms
        fields=(
            "category",
            "status",
        )

