# data_processor/views.py

from django.shortcuts import render
from django.contrib import messages
from .forms import UploadFileForm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import io
import urllib, base64
import os

def index(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            if not file.name.endswith('.csv'):
                messages.error(request, "Please upload a CSV file only.")
                return render(request, 'data_processor/index.html', {'form': form})

            try:
                df = pd.read_csv(file, encoding='utf-8')
            except UnicodeDecodeError:
                df = pd.read_csv(file, encoding='ISO-8859-1')
            except Exception as e:
                messages.error(request, f"An error occurred while reading the file: {e}")
                return render(request, 'data_processor/index.html', {'form': form})

            request.session['data'] = df.to_dict()
            messages.success(request, "File uploaded successfully. Now you can click on the following buttons to see the data processing or visualization of your data.")
            return render(request, 'data_processor/index.html', {'form': form})
    else:
        form = UploadFileForm()
    return render(request, 'data_processor/index.html', {'form': form})

def process_data(request):
    df = pd.DataFrame(request.session['data'])
    
    first_five_rows = df.head().to_html()
    numeric_df = df.select_dtypes(include=[np.number])
    summary_stats = numeric_df.agg(['mean', 'median', 'std']).to_html()

    missing_values = df[df.isnull().any(axis=1)].to_html()
    columns_with_missing = df.columns[df.isnull().any()].tolist()
    
    df_dropped = df.dropna()

    context = {
        'first_five_rows': first_five_rows,
        'summary_stats': summary_stats,
        'missing_values': missing_values,
        'columns_with_missing': columns_with_missing,
        'message': "The Missing values can be handled in many ways such as dropping the rows or columns that contain missing values or taking mean/median of the missing value fields etc.",
        'df_dropped': df_dropped.to_html(),
    }
    return render(request, 'data_processor/process.html', context)

def visualize_data(request):
    df = pd.DataFrame(request.session['data'])
    img = io.BytesIO()
    df.hist(figsize=(10, 10))
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    return render(request, 'data_processor/visualize.html', {'plot_url': plot_url})
