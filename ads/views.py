from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated

from ads.models import Ad
from ads.paginators import AdPaginator
from ads.permissions import IsOwnerOrManagerOrAdmin
from ads.serializers import AdCreateUpdateSerializer, AdListRetrieveSerializer


class AdCreateAPIView(generics.CreateAPIView):
    """
    View for creating a ad.
    Представление для создания объявления.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = AdCreateUpdateSerializer


class AdListAPIView(generics.ListAPIView):
    """
    View for viewing the list of ads for the current user.
    Представление для просмотра списка объявлений текущего пользователя.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = AdListRetrieveSerializer
    pagination_class = AdPaginator

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ('title', 'price', 'description',)
    search_fields = ('title', 'price', 'description',)
    ordering_fields = ('price',)

    def get_queryset(self):
        """ Метод вернет queryset с объявлениями текущего пользователя. """
        return Ad.objects.filter(user=self.request.user)


class AdAllListAPIView(generics.ListAPIView):
    """
    View for viewing the list of all ads.
    Представление для просмотра списка всех объявлений.
    """
    serializer_class = AdListRetrieveSerializer
    pagination_class = AdPaginator
    queryset = Ad.objects.all()

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ('title', 'price', 'description',)
    search_fields = ('title', 'price', 'description',)
    ordering_fields = ('price',)


class AdRetrieveAPIView(generics.RetrieveAPIView):
    """
    View for viewing a single ad.
    Представление для просмотра одного объявления.
    """
    serializer_class = AdListRetrieveSerializer
    queryset = Ad.objects.all()


class AdUpdateAPIView(generics.UpdateAPIView):
    """
    View for editing an ad.
    Представление для редактирования объявления.
    """
    permission_classes = [IsAuthenticated, IsOwnerOrManagerOrAdmin]
    serializer_class = AdCreateUpdateSerializer
    queryset = Ad.objects.all()


class AdDestroyAPIView(generics.DestroyAPIView):
    """
    View for deleting an ad.
    Представление для удаления объявления.
    """
    permission_classes = [IsAuthenticated, IsOwnerOrManagerOrAdmin]
    queryset = Ad.objects.all()
