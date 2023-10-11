import asyncio

from misc.config import read_config
from misc.log import *

from db.tasks import tasks_run

CONFIG_ENV_KEY = 'SRVC_CONFIG'

if __name__ == "__main__":
    config_path = os.environ[CONFIG_ENV_KEY]
    conf = read_config(config_path)
    asyncio.run(tasks_run(conf.get("db")))
