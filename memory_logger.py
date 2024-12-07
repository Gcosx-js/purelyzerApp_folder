import logging
from io import StringIO

# Bellekte logları tutacak stream
_log_stream = StringIO()

# Paylaşılan logger için global değişken
_shared_logger = None

def get_log_contents():
    return _log_stream.getvalue()

def get_shared_logger():
    """Paylaşılan logger nesnesini döndürür, gerekiyorsa oluşturur."""
    global _shared_logger
    if _shared_logger is None:  # Logger daha önce oluşturulmamışsa oluştur
        _shared_logger = logging.getLogger("SharedLogger")
        _shared_logger.setLevel(logging.DEBUG)
        
        # Handler ekle
        if not _shared_logger.hasHandlers():
            stream_handler = logging.StreamHandler(_log_stream)
            stream_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))
            _shared_logger.addHandler(stream_handler)
    return _shared_logger

def save_logs_to_file(file_path):
    """Logları bir dosyaya kaydeder."""
    with open(file_path, 'w') as f:
        f.write(_log_stream.getvalue())