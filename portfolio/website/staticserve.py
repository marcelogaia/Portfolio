from django.views.static import serve as staticserve
import portfolio.settings as settings
def serve(request, what):
   response = staticserve(request, what,
              document_root=settings.STATIC_ROOT)
   response['Cache-Control'] = 'no-cache'
   return response