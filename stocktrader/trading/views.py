from django.shortcuts import render
from django.http import JsonResponse
from .models import StockTrade
import requests

def home(request):
    return render(request, 'trading/home.html')

def get_stock_data(request):
    stock_symbol = request.GET.get('symbol')
    if stock_symbol:
        response = requests.get(f'https://api.example.com/stocks/{stock_symbol}')
        data = response.json()
        return JsonResponse(data)
    return JsonResponse({'error': 'No stock symbol provided'}, status=400)

def create_trade(request):
    if request.method == 'POST':
        stock_symbol = request.POST.get('symbol')
        quantity = request.POST.get('quantity')
        price = request.POST.get('price')
        trade = StockTrade(symbol=stock_symbol, quantity=quantity, price=price)
        trade.save()
        return JsonResponse({'message': 'Trade created successfully'}, status=201)
    return JsonResponse({'error': 'Invalid request method'}, status=405)