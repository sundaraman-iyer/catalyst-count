import csv
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Company
from .forms import CSVUploadForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CompanySerializer


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dataupload')  # Redirect to some authenticated view after successful login
        else:
            # Handle invalid login credentials (You can add error messages here if needed)
            return render(request, 'myapp/login.html', {'error_message': 'Invalid credentials. Please try again.'})

    return render(request, 'myapp/login.html')

@login_required
def data_upload_view(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csvFile']
            try:
                decoded_file = csv_file.read().decode('utf-8')
                csv_reader = csv.DictReader(decoded_file.splitlines())
                for row in csv_reader:
                    # Assuming you want to save the data in a 'Company' model
                    Company.objects.create(
                        name=row['name'],
                        domain=row['domain'],
                        year_founded=row['year founded'],
                        industry=row['industry'],
                        size_range=row['size range'],
                        locality=row['locality'],
                        country=row['country'],
                        linkedin_url=row['linkedin url'],
                        current_employee_estimate=row['current employee estimate'],
                        total_employee_estimate=row['total employee estimate'],
                    )
                return JsonResponse({'success': True})
            except Exception as e:
                return JsonResponse({'success': False, 'error': str(e)})
    else:
        form = CSVUploadForm()
    return render(request, 'myapp/dataupload.html', {'form': form})

@login_required
@api_view(['GET', 'POST'])
def query_builder_view(request):
    name_filter = request.data.get('name', '')
    year_founded_filter = request.data.get('year_founded', '')
    industry_filter = request.data.get('industry', '')
    country_filter = request.data.get('country', '')

    filtered_companies = Company.objects.filter(
        name__icontains=name_filter,
        year_founded__icontains=year_founded_filter,
        industry__icontains=industry_filter,
        country__icontains=country_filter,
    )

    # Serialize the filtered companies
    serializer = CompanySerializer(filtered_companies, many=True)

    count = filtered_companies.count()

    # Redirect to a separate view for rendering the template
    return render(request, 'myapp/querybuilder.html', {'count': count, 'data': serializer.data})

@login_required
def users_view(request):
    users = User.objects.all()
    return render(request, 'myapp/users.html', {'users': users})
