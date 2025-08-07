# home/views.py
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
from .models import CodeSnippet

def index(request):
    return render(request, 'home/index.html')

@csrf_exempt
@require_http_methods(["POST"])
def submit_code(request):
    try:
        data = json.loads(request.body)
        code_content = data.get('code', '')
        
        if not code_content.strip():
            return JsonResponse({'error': 'Code cannot be empty'}, status=400)
        
        # Create new code snippet - ID will auto-increment from 1
        code_snippet = CodeSnippet.objects.create(code_content=code_content)
        
        return JsonResponse({
            'success': True,
            'id': code_snippet.id,
            'message': f'Code saved with ID: {code_snippet.id}'
        })
    
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@require_http_methods(["GET"])
def get_code(request, code_id):
    try:
        code_snippet = CodeSnippet.objects.get(id=code_id)
        return JsonResponse({
            'success': True,
            'id': code_snippet.id,
            'code': code_snippet.code_content,
            'created_at': code_snippet.created_at.isoformat()
        })
    
    except CodeSnippet.DoesNotExist:
        return JsonResponse({'error': 'Code not found'}, status=404)
    
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)