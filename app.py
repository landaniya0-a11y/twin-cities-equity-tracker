import streamlit as st

# Custom page styling to make it look sleek
st.set_page_config(page_title="Twin Cities Equity Tracker", page_icon="📊", layout="centered")

st.title("📊 Twin Cities Infrastructure & Equity Tracker")
st.write(
    "This platform cross-references historical 20th-century racial covenants against "
    "the current location of high-energy industrial infrastructure and data centers in the Metro area."
)

st.write("---")

# Dropdown selector for regional analysis
neighborhood = st.selectbox(
    "Select a Twin Cities Metro Sub-Market:",
    ["North Minneapolis / Near North", "Edina / Country Club District", "South Minneapolis / Powderhorn", "Dayton / Champlin Industrial Zone"]
)

st.subheader(f"Regional Analysis: {neighborhood}")

# Real historical data integration points
if neighborhood == "North Minneapolis / Near North":
    st.error("Infrastructure Risk Status: High Environmental Burden")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Historical Racial Deeds (1910-1955)", value="82% Block Density")
    with col2:
        st.metric(label="Modern Industrial Zoning Grid", value="9/10 Intensity")
        
    st.markdown("""
    **Core Metrics & Infrastructure Impacts:**
    * **Historical Redlining:** Deemed 'Hazardous' (Grade D) by HOLC maps, preventing generational housing investments.
    * **Modern Facility Footprint:** Houses heavy manufacturing and waste processing facilities near residential zones.
    * **Data Center Suitability:** Targeted for low-cost commercial land conversions due to depressed historical property values.
    """)

elif neighborhood == "Edina / Country Club District":
    st.success("Infrastructure Risk Status: Excluded / Low Burden")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Historical Racial Deeds (1910-1955)", value="100% Exclusionary")
    with col2:
        st.metric(label="Modern Industrial Zoning Grid", value="0/10 Intensity")
        
    st.markdown("""
    **Core Metrics & Infrastructure Impacts:**
    * **Historical Redlining:** Covenants strictly mandated exclusive housing development for decades.
    * **Modern Facility Footprint:** Zone strictly restricted to high-value residential and light retail properties.
    * **Data Center Suitability:** Zero industrial infrastructure deployment; heavy energy routing is banned by local municipal codes.
    """)

elif neighborhood == "South Minneapolis / Powderhorn":
    st.warning("Infrastructure Risk Status: Moderate Environmental Burden")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Historical Racial Deeds (1910-1955)", value="34% Block Density")
    with col2:
        st.metric(label="Modern Industrial Zoning Grid", value="5/10 Intensity")
        
    st.markdown("""
    **Core Metrics & Infrastructure Impacts:**
    * **Historical Redlining:** Highly fragmented historical deeds leading to rapid pocket development.
    * **Modern Facility Footprint:** Contains a mix of light commercial businesses and commercial avenues bordering residential streets.
    * **Data Center Suitability:** High fiber-optic transit connectivity, but limited footprint size for massive server warehouse farms.
    """)

elif neighborhood == "Dayton / Champlin Industrial Zone":
    st.info("Infrastructure Risk Status: Emerging Infrastructure Hub")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Historical Racial Deeds (1910-1955)", value="< 5% (Agricultural)")
    with col2:
        st.metric(label="Modern Industrial Zoning Grid", value="6/10 Intensity")
        
    st.markdown("""
    **Core Metrics & Infrastructure Impacts:**
    * **Historical Redlining:** Outside the original urban core, avoiding early housing deed restrictions.
    * **Modern Facility Footprint:** Experiencing rapid transitions from farm acreage into massive industrial parks.
    * **Data Center Suitability:** High-priority development zone due to close proximity to high-voltage power transmission lines and affordable open land footprints.
    """)

# Main footer section - perfectly aligned outside of the neighborhood logic streams
st.write("---")
st.subheader("📋 Academic Disclosure & Data Citations")
st.caption("""
This application is a sophomore data synthesis prototype built for educational purposes. 
The regional analysis and socioeconomic logic frameworks are derived from the following primary research sources:
""")

st.markdown("""
* **Historical Covenant Data:** Sourced from the *Mapping Prejudice Project*, University of Minnesota Libraries. [View Live Interactive Covenants Map](https://umn.edu)
* **Environmental Disparity Statistics:** Baseline air pollution and tract exposure metrics sourced from the *Environmental Justice Framework*, Minnesota Pollution Control Agency (MPCA). [View MPCA EJ Framework](https://pca.state.mn.us)
* **Infrastructure Context:** Regional utility capacities and data center development footprints tracked via public municipal filings and the *Minnesota Center for Environmental Advocacy (MCEA)*. [View MCEA Reports](https://mncenter.org)
""")
