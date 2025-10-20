"""OCR utilities using OCR.space API."""
import os
import base64
import requests
import logging

logger = logging.getLogger(__name__)

ENABLE_OCR = os.getenv("ENABLE_OCR", "true").lower() == "true"
ENABLE_ASR = os.getenv("ENABLE_ASR", "false").lower() == "true"
OCR_SPACE_API_KEY = os.getenv("OCR_SPACE_API_KEY", "helloworld")


def extract_ocr_from_bytes(image_bytes: bytes) -> str:
    url = "https://api.ocr.space/parse/image"
    # Prefer multipart file upload rather than base64 payload — more robust for some file types
    files = {'file': ('upload.png', image_bytes, 'image/png')}
    data = {'apikey': OCR_SPACE_API_KEY, 'language': 'eng', 'OCREngine': 2}
    try:
        response = requests.post(url, files=files, data=data, timeout=60)
    except requests.exceptions.RequestException as e:
        logger.error("OCR.space request failed: %s", e)
        raise Exception("OCR.space request failed: %s" % str(e))

    # If provider returned non-2xx, surface a helpful message
    if not response.ok:
        logger.error("OCR.space returned non-OK status %s: %s", response.status_code, response.text[:500])
        raise Exception(f"OCR.space service error (status {response.status_code})")

    # Try to parse JSON, but be defensive: provider occasionally returns HTML or plain text
    try:
        result = response.json()
    except ValueError:
        logger.error("OCR.space returned non-JSON response: %s", response.text[:1000])
        raise Exception("OCR.space returned invalid response format")

    # Helpful debug logging for troubleshooting provider errors (dev-only)
    logger.debug("OCR.space response: %s", result)
    if result.get('OCRExitCode') != 1:
        # Prefer structured messages when available
        err_msg = result.get('ErrorMessage') or result.get('ErrorDetails') or ['Unknown']
        # ErrorMessage may be a list
        if isinstance(err_msg, list):
            err_msg = err_msg[0]
        raise Exception(f"OCR failed: {err_msg}")
    # Defensive access to parsed results
    parsed_results = result.get('ParsedResults') or []
    if not parsed_results:
        raise Exception("OCR.space returned no parsed results")
    text = parsed_results[0].get('ParsedText', '')
    return text.strip()


def extract_ocr_bytes(data: bytes, filename: str) -> dict:
    try:
        text = extract_ocr_from_bytes(data)
        return {'text': text, 'filename': filename}
    except Exception as e:
        return {'error': str(e)}
