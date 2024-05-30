
import pandas as pd
from django.shortcuts import render
from django.core.mail import send_mail
from .forms import UploadFileForm
from django.http import HttpResponseBadRequest

def handle_uploaded_file(f):
    if f.name.endswith('.xlsx'):
        df = pd.read_excel(f, engine='openpyxl')
    elif f.name.endswith('.csv'):
        df = pd.read_csv(f)
    else:
        raise ValueError("Unsupported file type. Please upload a .xlsx or .csv file.")

    # Debug: print the columns of the uploaded file
    print("Uploaded file columns:", df.columns)

    # Check if the required columns are present
    required_columns = {'State', 'DPD'}
    if not required_columns.issubset(df.columns):
        raise ValueError(f"Missing required columns. The file must contain {required_columns} columns.")
    
    summary = df.groupby(['State', 'DPD']).size().reset_index(name='Count')w
    return summary

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                summary = handle_uploaded_file(request.FILES['file'])
                summary_str = summary.to_string(index=False)
                send_mail(
                    'Summary Report',
                    summary_str,
                    'abhiv5976@gmail.com',  # Replace with your email
                    ['tech@themedius.ai', 'hr@themedius.ai'],
                    fail_silently=False,
                )
                return render(request, 'fileupload/success.html')
            except ValueError as e:
                return HttpResponseBadRequest(str(e))
    else:
        form = UploadFileForm()
    return render(request, 'fileupload/upload.html', {'form': form})

