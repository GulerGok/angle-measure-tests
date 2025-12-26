import time, os

def sleep(seconds=3):
    """Kısa ve okunabilir bekleme"""
    time.sleep(seconds)


def resolve_real_path(path: str) -> str:
    """
    Dosya yolunu büyük/küçük harf duyarsız şekilde
    diskten gerçek adıyla bulur.
    """
    directory, filename = os.path.split(path)

    if not os.path.isdir(directory):
        raise FileNotFoundError(f"Klasör bulunamadı: {directory}")

    for f in os.listdir(directory):
        if f.lower() == filename.lower():
            return os.path.join(directory, f)

    raise FileNotFoundError(f"Dosya bulunamadı: {filename}")
