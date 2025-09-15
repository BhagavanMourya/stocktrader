from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
import numpy as np

def stock_analysis(request):
    if request.method == 'GET':
        # Example data for analysis
        data = {
            'AAPL': [150, 152, 153, 155, 157],
            'GOOGL': [2800, 2820, 2810, 2830, 2850],
            'AMZN': [3400, 3420, 3410, 3430, 3450],
        }
        
        df = pd.DataFrame(data)
        
        # Calculate moving averages
        moving_averages = df.rolling(window=3).mean().to_dict()
        
        return JsonResponse({
            'moving_averages': moving_averages,
            'original_data': data
        })
    
    return JsonResponse({'error': 'Invalid request method'}, status=400)