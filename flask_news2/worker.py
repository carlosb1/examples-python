import time
import logging
LOGGER = logging.getLogger()


def runTask(group_name, group_owner, group_description):
    LOGGER.error("starting runTask")
    time.sleep(5)
    LOGGER.error("finished runTask")
    return {group_name: 'task complete'}
