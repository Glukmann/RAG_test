import logging
import sys

from indexer.config import settings

logging.basicConfig(
    level=getattr(logging, settings.indexer_log_level.upper(), logging.INFO),
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)

logger = logging.getLogger("indexer")
