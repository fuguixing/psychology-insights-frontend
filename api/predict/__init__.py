import logging
import azure.functions as func
from .handlers import bigfive_handler, preview_handler

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    route = req.route_params.get('route')
    if route == 'bigfive':
        return bigfive_handler(req)
    elif route == 'preview':
        return preview_handler(req)
    else:
        return func.HttpResponse("Invalid route.", status_code=404)
