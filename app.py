import streamlit as st


# ---------- Constants ----------

COMPANIES = [
    "Acer", "Apple", "Asus", "Dell",
    "HP", "Lenovo", "MSI", "Razer"
]

LAPTOP_TYPES = [
    "Notebook",
    "Gaming",
    "Ultrabook",
    "2 in 1 Convertible",
    "Workstation",
    "Netbook",
]

OPERATING_SYSTEMS = [
    "Windows 11",
    "Windows 10",
    "Windows 7",
    "Linux",
    "macOS",
    "No OS",
]

RAM_OPTIONS = [2, 4, 8, 12, 16, 24, 32, 64]

CPU_FREQUENCIES = [
    1.0, 1.2, 1.4, 1.6, 1.8,
    2.0, 2.2, 2.4, 2.6, 2.8,
    3.0, 3.2, 3.4,
]

SSD_OPTIONS = [
    0,
    128,
    256,
    512,
    1024,
    2048,
]

WEIGHT_OPTIONS = [
    0.8,
    1.0,
    1.2,
    1.4,
    1.6,
    1.8,
    2.0,
    2.2,
    2.4,
    2.6,
    2.8,
    3.0,
]

SCREEN_SIZES = [
    11.6,
    12.5,
    13.3,
    14.0,
    15.6,
    17.3,
]

RESOLUTIONS = [
    "1366x768",
    "1600x900",
    "1920x1080",
    "2560x1440",
    "3200x1800",
    "3840x2160",
]

YES_NO = [
    "No",
    "Yes",
]


# ---------- Page ----------

st.set_page_config(
    page_title="Laptop Price Prediction",
    page_icon="💻",
    layout="wide",
)

st.title("💻 Laptop Price Prediction")

st.caption(
    "Estimate laptop prices using a trained Machine Learning model."
)

st.write(
    """
Fill in the laptop specifications from the left sidebar.

The application will predict the laptop price using
the trained Machine Learning model.
"""
)


# ---------- Sidebar ----------

st.sidebar.header("💻 Laptop Specifications")

st.sidebar.subheader("📄 General Information")

company = st.sidebar.selectbox(
    "Company",
    COMPANIES,
)

laptop_type = st.sidebar.selectbox(
    "Laptop Type",
    LAPTOP_TYPES,
)

operating_system = st.sidebar.selectbox(
    "Operating System",
    OPERATING_SYSTEMS,
)

st.sidebar.divider()

st.sidebar.subheader("⚙️ Hardware")

ram = st.sidebar.selectbox(
    "RAM (GB)",
    RAM_OPTIONS,
)

cpu_frequency = st.sidebar.selectbox(
    "CPU Frequency (GHz)",
    CPU_FREQUENCIES,
)

ssd = st.sidebar.selectbox(
    "SSD Storage (GB)",
    SSD_OPTIONS,
)

weight = st.sidebar.selectbox(
    "Weight (kg)",
    WEIGHT_OPTIONS,
)

st.sidebar.divider()

st.sidebar.subheader("🖥 Display")

screen_size = st.sidebar.selectbox(
    "Screen Size (inch)",
    SCREEN_SIZES,
)

resolution = st.sidebar.selectbox(
    "Resolution",
    RESOLUTIONS,
)

ips_panel = st.sidebar.selectbox(
    "IPS Panel",
    YES_NO,
)

touchscreen = st.sidebar.selectbox(
    "Touchscreen",
    YES_NO,
)


# ---------- Preview ----------

st.subheader("📄 Selected Specifications")

col1, col2 = st.columns(2)

with col1:

    st.metric("Company", company)

    st.metric("Laptop Type", laptop_type)

    st.metric("RAM", f"{ram} GB")

    st.metric("CPU Frequency", f"{cpu_frequency} GHz")

    st.metric("Screen Size", f"{screen_size} inch")

with col2:

    st.metric("Operating System", operating_system)

    st.metric("SSD", f"{ssd} GB")

    st.metric("Weight", f"{weight} kg")

    st.metric("Resolution", resolution)

    st.metric("IPS Panel", ips_panel)

    st.metric("Touchscreen", touchscreen)


st.divider()

st.caption("Created with ❤️ using Streamlit and Machine Learning")
