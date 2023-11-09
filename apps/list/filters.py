import django_filters
from .models  import *

class RoomsFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name="price", lookup_expr="gte", label="Min Price")
    max_price = django_filters.NumberFilter(field_name="price", lookup_expr="lte", label="Max Price")

    class Meta:
        model=Rooms
        fields=(
            "category",
            "status",
        )

