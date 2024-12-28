from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import Form, Question, AnalyticsCache
from .models import Response as FormResponse   
from .serializers import FormSerializer, QuestionSerializer, ResponseSerializer, AnalyticsSerializer

class FormListCreateView(generics.ListCreateAPIView):
    queryset = Form.objects.all()
    serializer_class = FormSerializer

class QuestionCreateView(generics.CreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class ResponseCreateView(generics.CreateAPIView):
    queryset = FormResponse.objects.all()
    serializer_class = ResponseSerializer

class FormAnalyticsView(APIView):
    def get(self, request, form_id):
        try:
            analytics = AnalyticsCache.objects.get(form_id=form_id)
            return Response({
                "form_id": analytics.form_id,
                "analytics": analytics.data,
                "updated_at": analytics.updated_at
            })
        except AnalyticsCache.DoesNotExist:
            return Response({"error": "Analytics not available for this form."}, status=404)

