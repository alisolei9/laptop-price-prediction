import re

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



# ///////////////////////////////////////////
def extract_resolution(text):
    """
    Extract screen resolution.

    Returns
    -------
    tuple
        (width, height)
    """

    match = re.findall(r"\d+x\d+", text)

    if len(match) == 0:
        return None, None

    width, height = match[0].split("x")

    return int(width), int(height)
# ////////////////////////////////////////////

def extract_ips(text):
    """
    Return 1 if IPS Panel exists, otherwise 0.
    """

    if "IPS Panel" in text:
        return 1

    return 0
# //////////////////////////////////////////////

def extract_touchscreen(text):
    """
    Return 1 if Touchscreen exists, otherwise 0.
    """

    if "Touchscreen" in text:
        return 1

    return 0
# /////////////////////////////////////////////

def extract_cpu_family(cpu):
    """
    Extract CPU family from cpu_type.
    """

    cpu = cpu.lower()

    if "core i7" in cpu:
        return "Core i7"

    elif "core i5" in cpu:
        return "Core i5"

    elif "core i3" in cpu:
        return "Core i3"

    elif "pentium" in cpu:
        return "Pentium"

    elif "celeron" in cpu:
        return "Celeron"

    elif "atom" in cpu:
        return "Atom"

    elif "amd" in cpu or "a-series" in cpu or "a9" in cpu or "ryzen" in cpu:
        return "AMD"

    return "Other"
# //////////////////////////////////////////////

def extract_gpu_family(gpu):
    """
    Extract GPU family from gpu_type.
    """

    gpu = gpu.lower()

    if "gtx" in gpu:
        return "GTX"

    elif "mx" in gpu:
        return "MX"

    elif "quadro" in gpu:
        return "Quadro"

    elif "radeon" in gpu:
        return "Radeon"

    elif "firepro" in gpu:
        return "FirePro"

    elif "uhd graphics" in gpu:
        return "UHD Graphics"

    elif "hd graphics" in gpu:
        return "HD Graphics"

    elif "iris" in gpu:
        return "Iris Graphics"

    return "Other"
# ///////////////////////////////////////////


def engineer_features(df):
    """
    Apply all feature engineering steps.
    """

    df = df.copy()

    # Storage
    df["ssd"] = df["memory"].apply(extract_ssd)
    df["hdd"] = df["memory"].apply(extract_hdd)
    df["flash_storage"] = df["memory"].apply(extract_flash_storage)
    df["hybrid"] = df["memory"].apply(extract_hybrid)

    # Screen Resolution
    resolution = df["screen_resolution"].apply(extract_resolution)

    df["resolution_width"] = resolution.apply(lambda x: x[0])
    df["resolution_height"] = resolution.apply(lambda x: x[1])

    df["ips_panel"] = df["screen_resolution"].apply(extract_ips)
    df["touchscreen"] = df["screen_resolution"].apply(extract_touchscreen)

    # CPU
    df["cpu_family"] = df["cpu_type"].apply(extract_cpu_family)

    # GPU
    df["gpu_family"] = df["gpu_type"].apply(extract_gpu_family)

    # PPI
    pixel_diagonal = (
        (
            df["resolution_width"] ** 2
            + df["resolution_height"] ** 2
        ) ** 0.5
    )

    df["ppi"] = pixel_diagonal / df["inches"]

    # Drop unused columns
    df = df.drop(
        columns=[
            "memory",
            "cpu_type",
            "gpu_type",
            "screen_resolution",
        ]
    )

    return df
