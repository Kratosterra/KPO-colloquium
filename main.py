import logging

import coloredlogs

from common import utils

# Оформляем логирование.
coloredlogs.install(level='DEBUG')
logger = logging.getLogger(__name__)
coloredlogs.install(
    level='DEBUG', logger=logger,
    fmt='%(asctime)s.%(msecs)03d %(filename)s:%(lineno)d %(levelname)s %(message)s'
)

# Создаём базы данных!
utils.create_database()

# Получаем микросервисы
from service.app import app

if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1", port="3000")
