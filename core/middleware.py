from django.http import JsonResponse


class ErrorDataBaseIntegrityHandlerMiddleware:
  def __init__(self, get_response):
    self.get_response = get_response

  def __call__(self, request):
    response = self.get_response(request)
    return response

  def process_exception(self, request, exception):
    message = exception and exception.args[0].lower() or ''
    if 'unique constraint' in message:
      return JsonResponse({'detail': 'Record already exist.'}, status=503, safe=False)

