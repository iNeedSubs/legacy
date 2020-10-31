from django.views.generic import TemplateView
from django.utils.cache import patch_response_headers


class VueView(TemplateView):
    template_name = 'index.html'

    def render_to_response(self, context, **response_kwargs):
        # Get response from parent TemplateView class
        response = super().render_to_response(
            context, **response_kwargs
        )

        # Add Cache-Control and Expires headers
        patch_response_headers(response, cache_timeout=86400)

        # Return response
        return response
