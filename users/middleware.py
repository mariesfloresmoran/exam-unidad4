from datetime import datetime

class IpMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        ip = request.META.get('REMOTE_ADDR')
        fecha = datetime.now()

        f = open("ip_visitantes.txt", "a")
        f.write(f"Visita de: {ip} - {fecha}\n")
        f.close()

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
