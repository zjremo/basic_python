import logging

# 获取logger实例
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# 处理器
handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
# handler.setLevel(logging.INFO)

# 日志格式 
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# 添加handler, 负责真正输出日志
logger.addHandler(handler)

logger.debug('hello, logger')