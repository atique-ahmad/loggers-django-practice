from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
import logging

logger = logging.getLogger(__name__)

def log_view(request):
    logger.info('This is an example log message.')
    return JsonResponse({'message': 'log messages!'})


def calculator(request):
    if request.method == 'POST':
        operation = request.POST.get('operation')
        x = float(request.POST.get('x'))
        y = float(request.POST.get('y'))

        if operation == 'add':
            result = x + y
            logger.info("Addition operation", extra={"operation": "add", "x": x, "y": y, "result": result})
        elif operation == 'subtract':
            result = x - y
            logger.info("Subtraction operation", extra={"operation": "subtract", "x": x, "y": y, "result": result})
        elif operation == 'multiply':
            result = x * y
            logger.info("Multiplication operation", extra={"operation": "multiply", "x": x, "y": y, "result": result})
        elif operation == 'divide':
            if y == 0:
                logger.error("Division by zero", extra={"operation": "divide", "x": x, "y": y})
                return JsonResponse({'error': 'Division by zero'})
            result = x / y
            logger.info("Division operation", extra={"operation": "divide", "x": x, "y": y, "result": result})
        else:
            return JsonResponse({'error': 'Invalid operation'})

        return JsonResponse({'result': result})

    return render(request, 'calculator.html')
    
