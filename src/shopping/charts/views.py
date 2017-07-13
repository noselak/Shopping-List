from django.shortcuts import render, redirect
from django.views.generic import View


class BoughtItemsChartView(View):
    def get(self, request):
        template = 'charts/category_chart.html'
        context = {}
        return render(request, template, context)
