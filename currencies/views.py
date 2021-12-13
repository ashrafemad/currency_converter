from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from currencies.serializers import ConvertCurrencySerializer


class ConvertCurrencyView(CreateAPIView):
    serializer_class = ConvertCurrencySerializer
    permission_classes = (IsAuthenticated, )

    def get_serializer_context(self):
        ctx = super().get_serializer_context()
        ctx['user'] = self.request.user
        return ctx
