from misc import log
import uvicorn
from services.simple_http_server.main import factory

app = factory()

if __name__ == '__main__':
    uvicorn.run(
        'simple_http_server:app', host='0.0.0.0', port=8010, reload=True, debug=True, log_config='etc/logging.conf'
    )
