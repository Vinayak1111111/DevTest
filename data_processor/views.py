# data_processor/views.py
import pandas as pd
from django.shortcuts import render
from django.core.mail import send_mail
from .forms import FileUploadForm

def process_file(file):
    # Reading the Excel file
    df = pd.read_excel(file)
    
    # Processing the summary
    summary = df.groupby(['Cust State']).agg(
        Total_Pins=('Cust Pin', 'nunique'),
        Total_DPD=('DPD', 'sum'),
    ).reset_index()
    
    # Renaming the columns to match the provided sample output
    summary.columns = ['Cust State', 'Total Pins', 'Total DPD']
    
    return summary

def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            summary = process_file(file)
            summary_html = summary.to_html(index=False)

            # Send email
            send_mail(
                subject='Python Assignment - Your Name',
                message='Please find the summary report attached.',
                from_email='your_email@example.com',
                recipient_list=['recipient@example.com'],
                fail_silently=False,
                html_message=summary_html,
            )
            return render(request, 'data_processor/summary.html', {'summary': summary_html})

    else:
        form = FileUploadForm()
    return render(request, 'data_processor/upload.html', {'form': form})
