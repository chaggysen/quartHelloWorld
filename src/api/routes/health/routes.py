from quart import (Blueprint, jsonify)

bp = Blueprint('health', __name__)

@bp.route('/')
def index():
    return "Hello, World!"

@bp.route('/health')
def health():
    return jsonify({"status": "healthy"})