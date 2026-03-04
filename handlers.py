import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.constants import ParseMode
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

from config import MAX_UPLOAD_SIZE, SESSION_STRING, API_KEY  # Ensure API_KEY added in config
from core import fetch_file_list, cache_get, cache_set, send_file
from utils import is_valid_terabox_url, extract_surl, find_url_in_text, format_bytes

logger = logging.getLogger(__name__)

_LIMIT_NOTE = (
    "4 GB (owner session active)"
    if SESSION_STRING
    else "2 GB (set `SESSION_STRING` in `.env` to raise to 4 GB)"
)

# -------- COMMAND HANDLERS --------
async def cmd_start(update: Update, _ctx: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "☁️ *TeraBox Downloader Bot*\n\n"
        "Send me any TeraBox share link and I'll:\n"
        "• Upload the file directly to Telegram\n"
        "• Send you the direct download link\n\n"
        f"Upload limit: `{_LIMIT_NOTE}`\n\n"
        "Use /help for more info.",
        parse_mode=ParseMode.MARKDOWN,
    )

async def cmd_help(update: Update, _ctx: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "*How to use:*\n"
        "Just paste any TeraBox share link — the bot handles the rest.\n\n"
        "*Supported domains:*\n"
        "`terabox.com` · `terabox.app` · `1024terabox.com`\n"
        "`teraboxshare.com` · `teraboxlink.com`\n\n"
        "*File delivery:*\n"
        "≤ 50 MB → uploaded instantly via Bot API\n"
        "> 50 MB → downloaded on server, then uploaded via MTProto\n"
        f"> limit → download link only  _(limit: {_LIMIT_NOTE})_\n\n"
        "*Example link:*\n"
        "`https://terabox.app/s/1HSEb8PZRUE7Z1Tvd3ZtT0g`",
