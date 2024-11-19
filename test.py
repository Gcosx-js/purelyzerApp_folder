import warnings

# UserWarning'leri özel bir blokta yakalamak için ayarla
with warnings.catch_warnings(record=True) as w:
    warnings.simplefilter("always", UserWarning)  # UserWarning'leri kaydet

    try:
        # Burada bazı işlemler
        warnings.warn("Bu bir UserWarning uyarısı!", UserWarning)
        raise ValueError("Bu bir ValueError hatası!")

    except Exception as e:
        # Sadece UserWarning harici hataları yakala
        if not any(issubclass(warning.category, UserWarning) for warning in w):
            print(f"Hata yakalandı: {e}")
        else:
            raise ValueError