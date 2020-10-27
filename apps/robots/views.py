from django.http import HttpResponse
from django.views.generic import View


class RobotsTxt(View):

    def get(self, *args):
        lines = [
            'User-Agent: *',
            'Disallow: /admin/',
            'Disallow: /offline/',
        ]
        return HttpResponse('\n'.join(lines), content_type='text/plain')
