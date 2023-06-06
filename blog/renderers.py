from rest_framework.renderers import JSONRenderer


class JSONRendererOnly(JSONRenderer):
    """
    Renderer which always returns JSON, ignoring the 'Accept' header.
    """
    media_type = '*/*'
