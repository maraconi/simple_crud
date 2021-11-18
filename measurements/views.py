from rest_framework.viewsets import ModelViewSet
from measurements.serializers import ProjectSerializer, MeasurementSerializer
from measurements.models import Project, Measurement



class ProjectViewSet(ModelViewSet):
    """ViewSet для проекта."""
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class MeasurementViewSet(ModelViewSet):
    """ViewSet для измерения."""
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
