from django_filters import rest_framework as filters
from reviews.models import Title


class TitlesFilter(filters.FilterSet):
    """Filter title objects."""
    name = filters.CharFilter(
        field_name='name', lookup_expr='contains')
    year = filters.CharFilter(
        field_name='year')
    category = filters.CharFilter(
        field_name='category__slug', lookup_expr='contains')
    genre = filters.CharFilter(
        field_name='genre__slug', lookup_expr='contains')

    class Meta():
        model = Title
        fields = ['name', 'year', 'genre', 'category']
