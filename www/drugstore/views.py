from datetime import timedelta
from django.contrib.auth.models import AnonymousUser
from rest_framework import views, permissions, generics, mixins, response
from rest_framework_simplejwt.tokens import Token

from .serializers import DrugSerializer, VaccinationSerializer, Drug, Vaccination


# Create your views here.
class DrugList(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Drug.objects.all()
    serializer_class = DrugSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class DrugDetail(mixins.RetrieveModelMixin,
                 mixins.CreateModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 generics.GenericAPIView):
    queryset = Drug.objects.all()
    serializer_class = DrugSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class VaccinationList(generics.ListCreateAPIView):
    queryset = Vaccination.objects.all()
    serializer_class = VaccinationSerializer


class VaccinationDetail(generics.RetrieveAPIView,
                        generics.UpdateAPIView,
                        generics.DestroyAPIView):
    queryset = Vaccination.objects.all()
    serializer_class = VaccinationSerializer


class ValidationView(views.APIView):
    """
    Create a JSON Web Token -JWT- to access to project endpoints
    """
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        # Since django is oriented to be used together with the model,
        # it's necessary to validate against a User when creating
        # the token, that is why we use an AnonymousUser model
        user = AnonymousUser
        # A sliding token has an expiration time, and for create a Token
        # with simplejwt its needed set a time, thus its a perfect simple implementation
        Token.token_type = 'sliding'
        Token.lifetime = timedelta(minutes=5)
        token = Token.for_user(user)
        return response.Response({'token': token.__str__()})
