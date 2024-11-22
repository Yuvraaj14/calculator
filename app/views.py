from django.shortcuts import render
from .models import Calculation

def calculator(request):
    if request.method == 'POST':
        operation = request.POST.get('operation')
        operands = request.POST.get('operands').split(',')
        result = perform_calculation(operation, operands)
        
        # Save to database
        Calculation.objects.create(operation=operation, operands=','.join(operands), result=result)
        
        return render(request, 'index.html', {'result': result})

    return render(request, 'index.html')

def perform_calculation(operation, operands):
    # Implement the logic for different operations
    if operation == 'add':
        return sum(map(float, operands))
    elif operation == 'subtract':
        return float(operands[0]) - sum(map(float, operands[1:]))
    # Add more operations as needed