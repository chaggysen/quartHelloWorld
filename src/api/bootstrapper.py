from quart import (Quart)
from azure.monitor.opentelemetry import configure_azure_monitor
from opentelemetry.instrumentation.openai import OpenAIInstrumentor
from opentelemetry.instrumentation.aiohttp_client import AioHttpClientInstrumentor
from opentelemetry.instrumentation.asgi import OpenTelemetryMiddleware
from opentelemetry.instrumentation.httpx import (
    HTTPXClientInstrumentor,
)
from quart_cors import cors
import logging
import os

def initialize_app() -> Quart:
    app = Quart(__name__)
    
    #from routes import health_bp
    from routes import health_bp
    app.register_blueprint(health_bp)
    
    # Add logging here
    if os.getenv("APPLICATIONINSIGHTS_CONNECTION_STRING"):
        configure_azure_monitor()

        # Instrument OpenAI
        # https://pypi.org/project/opentelemetry-instrumentation-openai/
        OpenAIInstrumentor().instrument()

        # This tracks HTTP requests made by aiohttp:
        AioHttpClientInstrumentor().instrument()
        
        # This tracks HTTP requests made by httpx:
        HTTPXClientInstrumentor().instrument()

        # This middleware tracks app route requests:
        app.asgi_app = OpenTelemetryMiddleware(app.asgi_app)  # type: ignore[assignment]

    default_level = "INFO" # In development, log more

    if os.getenv("WEBSITE_HOSTNAME"): # In production, don't log as heavily
      default_level = "WARNING"
    
    logging.basicConfig(level=os.getenv("APP_LOG_LEVEL", default_level))
    if allowed_origin := os.getenv("ALLOWED_ORIGIN"):
        app.logger.info("CORS enabled for %s", allowed_origin)
        cors(app, allow_origin=allowed_origin, allow_methods=["GET", "POST"])    
    
    return app