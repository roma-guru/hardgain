class CORSMiddleware(object):
    """
    Very simple middleware to insert CORS header.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Headers"] = "X-Requested-With"

        return response
