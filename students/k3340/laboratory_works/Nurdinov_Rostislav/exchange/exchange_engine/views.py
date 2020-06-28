from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .models import JobSeeker, Vacancy, Resume
from .serializers import *


class JobSeekerListView(generics.ListAPIView):
    """Вывод списка соискателей"""
    queryset = JobSeeker.objects.all()
    serializer_class = JobSeekerListSerializer


class JobSeekerRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """Вывод соискателея"""
    queryset = JobSeeker.objects.all()
    serializer_class = JobSeekerDetailSerializer


class JobSeekerCreateView(generics.CreateAPIView):
    """Создание соискателя"""
    queryset = JobSeeker.objects.all()
    serializer_class = JobSeekerCreateSerializer


class VacancyListView(generics.ListAPIView):
    """Вывод списка вакансий"""
    serializer_class = VacancyListSerializer

    def get_queryset(self):
        queryset = Vacancy.objects.all()
        params = self.request.query_params

        profession = params.get('profession', None)
        from_s = params.get('from_s', None)
        to_s = params.get('to_s', None)
        min_exp = params.get('min_exp', None)

        if profession:
            queryset = queryset.filter(profession=profession)

        if from_s and to_s:
            queryset = queryset.filter(salary__range=(from_s, to_s))
        elif from_s:
            queryset = queryset.filter(salary__gte=from_s)
        elif to_s:
            queryset = queryset.filter(salary__lte=to_s)

        if min_exp:
            queryset = queryset.filter(min_exp__lte=min_exp)

        return queryset


class VacancyRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """Вывод вакансии"""
    queryset = Vacancy.objects.all()
    serializer_class = VacancyDetailSerializer


class VacancyCreateView(generics.CreateAPIView):
    """Создание вакансии"""
    queryset = Vacancy.objects.all()
    serializer_class = VacancyCreateSerializer


class ProfessionListView(generics.ListAPIView):
    """Вывод списка профессий"""
    queryset = Profession.objects.all()
    serializer_class = ProfessionListSerializer


class ProfessionRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """Вывод профессии"""
    queryset = Profession.objects.all()
    serializer_class = ProfessionDetailSerializer


class ProfessionCreateView(generics.CreateAPIView):
    """Создание професии"""
    queryset = Profession.objects.all()
    serializer_class = ProfessionCreateSerializer


class EmployerListView(generics.ListAPIView):
    """Вывод списка работодателей"""
    queryset = Employer.objects.all()
    serializer_class = EmployerListSerializer


class EmployerRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """Вывод работодателя"""
    queryset = Employer.objects.all()
    serializer_class = EmployerDetailSerializer


class EmployerCreateView(generics.CreateAPIView):
    """Создание работодателя"""
    queryset = Employer.objects.all()
    serializer_class = EmployerCreateSerializer


class ExperienceListView(generics.ListAPIView):
    """Список опытов работы"""
    queryset = Experience.objects.all()
    serializer_class = ExperienceListSerializer


class ExperienceRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """Опыт работы"""
    queryset = Experience.objects.all()
    serializer_class = ExperienceDetailSerializer


class ExperienceCreateView(generics.CreateAPIView):
    """Создания опыта работы"""
    queryset = Experience.objects.all()
    serializer_class = ExperienceCreateSerializer
