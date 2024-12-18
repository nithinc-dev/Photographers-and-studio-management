from django.shortcuts import render, redirect
from .forms import PhotographerForm, StudioForm, AppointmentForm, StudioSearchForm
from .models import Photographer, Studio, Appointment , Address, Service
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import random

def home(request):
    home = "hello "
    return render(request, 'home.html',{'home':home})

@login_required    
def photographer(request):
    if request.method == "POST":
        form = PhotographerForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            messages.success(request, "Your form has been submitted successfully !")
            return redirect('p_reg') #redirect to the same view function
    else:
        form = PhotographerForm()
    return render(request, 'photo_registration.html', {'form': form})

@login_required 
def studio(request):
    if request.method == "POST":
        form = StudioForm(request.POST)
        if form.is_valid():
            form.save()
            # messages.success(request, "Your form has been submitted successfully !")
            return redirect('s_reg') #redirect to the same view function
    else:
        form = StudioForm()
    return render(request, 'studio_registration.html', {'form': form})



from django.shortcuts import render
from .forms import StudioSearchForm
from .models import Studio, Address

@login_required 
def studio_search(request):
    if request.method == "POST":
        form = StudioSearchForm(request.POST)
        if form.is_valid():
            district = form.cleaned_data.get('district')
            area = form.cleaned_data.get('area')

            # Filter Address objects based on district and area
            address_qs = Address.objects.all()
            if district:
                address_qs = address_qs.filter(district__icontains=district)
            if area:
                address_qs = address_qs.filter(area__icontains=area)

            # Filter Studio objects based on the filtered Address queryset
            studios = Studio.objects.filter(address__in=address_qs)

            # Reset the form
            form = StudioSearchForm()

            return render(request, 'search.html', {'form': form, 'filtered_result': studios})
    else:
        form = StudioSearchForm()

    return render(request, 'search.html', {'form': form})


# def studio_search(request):
#     if request.method == "POST":
#         form = StudioSearchForm(request.POST)
#         if form.is_valid():
#             if form.is_valid():
#                 district = form.cleaned_data['district']
#                 area = form.cleaned_data['area']
                
#                 addressf = Address.objects.filter(district=district, area=area)
#                 studios = Studio.objects.filter(address=addressf)
#                 form = StudioSearchForm()
#                 return render(request, 'search.html',{'form': form,'filtered_result': studios})
#     else:
#         form = StudioSearchForm()
#     return render(request, 'search.html', {'form': form})
                
@login_required               
def all(request):
    a = "2 buttons for all photographers and studios "
    return render(request, 'all.html',{'txt': a})
@login_required 
def all_s(request):
    studios = Studio.objects.all()
    return render(request, 'all_studios.html',{'studios': studios})
@login_required 
def all_p(request):
    photographers = Photographer.objects.all()
    return render(request, 'all_photos.html',{'photographers':photographers})


# import smtplib
# import os
# from email.message import EmailMessage
# from dotenv import load_dotenv
# load_dotenv()
# sender= os.getenv('email')
# receiver= 'cnithin650@gmail.com'

# msg = EmailMessage()
# msg['subject'] = 'Appointment Conformed'

# msg['From'] = os.getenv('email')

# @login_required 
# def appoint(request):
#     ls =['Services include: Marriage Photography, Event Photography','Services include: Documentary Photography and Videography, Journalism  Photography','Services include: Event Photography, Astral Photography, Drone Photography','Services include: VFX, SFX, 3D animation']
#     random.shuffle(ls)
#     if request.method == "POST":
#         form = AppointmentForm(request.POST)
#         if form.is_valid():
#             form.save()
#             email = form.cleaned_data['email']
#             customer = form.cleaned_data.get('customer_name')
#             studio = form.cleaned_data.get('studio')
#             msg['To'] = email
#             msg.set_content(f"{customer}, You will be soon get an email/call regarding the appointment!,the studio {studio} can offer services like {ls[0]}")
#             with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
#                 smtp.login(os.getenv('email'),os.getenv('password'))
#                 smtp.send_message(msg)
#             messages.success(request, f"{customer}, You will be soon get an email/call regarding the appointment!,the studio {studio} can offer services like {ls[0]}")
#             return redirect('appointment') #redirect to the same view function
#     else:
#         form = AppointmentForm()
#     return render(request, 'appointment.html', {'form': form,'descriptions':ls})




import smtplib
import os
from email.message import EmailMessage
from dotenv import load_dotenv
import random  # Add this import
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages  # Add this import

load_dotenv()
sender = os.getenv('email')
receiver = 'cnithin650@gmail.com'

msg = EmailMessage()
msg['subject'] = 'Appointment Confirmed'  # Fixed typo
msg['From'] = os.getenv('email')

@login_required 
def appoint(request):
    ls = [
        'Services include: Marriage Photography, Event Photography',
        'Services include: Documentary Photography and Videography, Journalism Photography',
        'Services include: Event Photography, Astral Photography, Drone Photography',
        'Services include: VFX, SFX, 3D animation'
    ]
    random.shuffle(ls)
    
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            customer = form.cleaned_data.get('customer_name')
            studio = form.cleaned_data.get('studio')
            msg['To'] = email
            msg.set_content(f"{customer}, The studio {studio} can offer services like {ls[0]}, call:9573883935 Thank you for using Photo Hub, a global application for managing studio and photographers")
            
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(os.getenv('email'), os.getenv('password'))
                smtp.send_message(msg)
            
            messages.success(request, f"{customer}, You will soon get an email/call regarding the appointment! The studio {studio} can offer services like {ls[0]}")
            return redirect('appointment')  # Redirect to the same view function
    else:
        form = AppointmentForm()
    
    return render(request, 'appointment.html', {'form': form, 'descriptions': ls})



def gallery(request):
    gls = ['1.jpg', '2.jpg', '3.jpg', '4.png','5.png', '6.jpg', '7.jpg', '8.jpg','9.png', '10.png','11.png', '12.png', '13.png', '14.jpg', '15.jpg', '16.jpg']
    random.shuffle(gls)
    return render(request, 'gallery.html',{'all_images':gls})

from django.views.generic import ListView, DetailView

class StudioDetailView(DetailView):
    template_name = 'single_studio.html'
    model = Studio

import csv
from django.http import HttpResponse 


def export_model_csv(request):
    # usually http response will send html now we are changing the content type
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Photographers.csv"'
    writer = csv.writer(response)
    #heading
    writer.writerow(['Name', 'liscence No', 'Phone'])
    enrollments = Photographer.objects.all().values_list('name', 'license_no', 'phone_number')
    
    for row in enrollments:
        writer.writerow(row)
        #it takes list as input 
    return response



    
    
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from io import BytesIO
from .models import *
from django.utils import timezone


def export_model_pdf(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="studio_data.pdf"'
   
    p = canvas.Canvas(response)
   
    # Draw the title
    p.drawString(100, 750, "Studios data")
   
    # Fetch data from the model
    data = Studio.objects.all()
    # data = Enrollment.objects.all().select_related('student', 'course')
   
    # Set starting position for the data
    y = 720
    line_height = 20
   
    # Write data to the PDF
    for entry in data:
        p.drawString(100, y, f"Name: {entry.name}, Course: {entry.phone_num}")
        y -= line_height
       
        # Check if we need to move to a new page
        if y < 50:
            p.showPage()
            y = 750
   
    # Close the PDF object cleanly.
    p.showPage()
    p.save()
   
   
    return response