import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN: str        = os.environ["8755130382:AAF9jzZEYZkoBiKTFFcqIQUaZO3GFL7QL_A"]
NDUS_COOKIE: str      = os.environ["PANWEB=1; TSID=m0RHbkAjLAp2ugYpZoIp9wgg7FHQY095; bid_n=18be85f750d4f42dba4207; _ga=GA1.1.1627430852.1700410655; fbm_756701921753953=base_domain=.terabox.app; ndus=Y-v8LeYteHuiTHDIo5RLqixbQFofA06gObCb9DUE; stripe_mid=ef178580-35ba-47ab-a706-1a000765950394f456; browserid=M8oIfy3G85e0v99eknqJDPeek9TdfnX963_PtXYvuosk_bIUUWm-W7sFEng=; lang=en; _ga_06ZNKL8C2E=GS1.1.1707915442.11.0.1707915554.60.0.0; csrfToken=EESlvx4P7Edqh6tOG30jTr7g"]

API_ID: int | None    = int(os.environ["API_ID"]) if os.getenv("API_ID") else None
API_HASH: str | None  = os.getenv("API_HASH")
SESSION_STRING: str | None = os.getenv("SESSION_STRING")

_4GB = 4 * 1024 ** 3
_2GB = 2 * 1024 ** 3
MAX_UPLOAD_SIZE: int  = _4GB if SESSION_STRING else _2GB
BOT_API_LIMIT: int    = 50 * 1024 ** 2

CACHE_TTL: int        = int(os.getenv("CACHE_TTL", 7200))
LOG_LEVEL: str        = os.getenv("LOG_LEVEL", "INFO").upper()
