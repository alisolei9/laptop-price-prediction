import pandas as pd

# ////////////////////////////////////////////
def extract_capacity(text):

    capacity = text.split()[0]

    if "TB" in capacity:
        return float(capacity.replace("TB", "")) * 1024

    return float(capacity.replace("GB", ""))

# ///////////////////////////////////////////
def extract_ssd(text):

    parts = [part.strip() for part in text.split("+")]

    ssd = 0

    for part in parts:

        if "SSD" in part:
            ssd += extract_capacity(part)

    return ssd

# ///////////////////////////////////////////
def extract_hdd(text):

    parts = [part.strip() for part in text.split("+")]

    hdd = 0

    for part in parts:

        if "HDD" in part:
            hdd += extract_capacity(part)

    return hdd

#  //////////////////////////////////////////
def extract_flash_storage(text):

    parts = [part.strip() for part in text.split("+")]

    flash = 0

    for part in parts:

        if "Flash Storage" in part:
            flash += extract_capacity(part)

    return flash

# ///////////////////////////////////////////
def extract_hybrid(text):

    parts = [part.strip() for part in text.split("+")]

    hybrid = 0

    for part in parts:

        if "Hybrid" in part:
            hybrid += extract_capacity(part)

    return hybrid


