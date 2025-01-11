import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio
import base64
import io

# Ensure Kaleido is recognized for PNG export
pio.kaleido.scope.default_format = "png"
pio.kaleido.scope.default_width = 1200
pio.kaleido.scope.default_height = 700

st.set_page_config(page_title="Sankey Diagrams for FP&A", layout="wide")

# ----------------
# Helper Functions
# ----------------
def parse_flow_text(flow_text: str):
    flows = []
    lines = flow_text.strip().split("\n")
    for line in lines:
        if not line.strip():
            continue
        try:
            parts = line.strip().split("[")
            source_part = parts[0].strip()
            remainder = parts[1].split("]")
            amount_part = remainder[0].strip()
            target_part = remainder[1].strip()

            source = source_part
            target = target_part
            amount = float(amount_part)
            flows.append((source, amount, target))
        except:
            st.warning(f"Could not parse line: {line}")
    return flows


def load_data_from_file(uploaded_file):
    if uploaded_file is None:
        return []

    file_name = uploaded_file.name.lower()
    if file_name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    required_cols = {"Source", "Amount", "Target"}
    if not required_cols.issubset(df.columns):
        st.error(f"Uploaded file must contain columns: {required_cols}")
        return []

    flows = [(row["Source"], row["Amount"], row["Target"]) for _, row in df.iterrows()]
    return flows


def build_sankey(
    flows,
    node_color_map=None,
    node_thickness=20,
    node_padding=20,
    opacity=0.6
):
    labels = []
    for source, amount, target in flows:
        if source not in labels:
            labels.append(source)
        if target not in labels:
            labels.append(target)

    label_to_index = {label: i for i, label in enumerate(labels)}

    sources = [label_to_index[s] for s, _, _ in flows]
    targets = [label_to_index[t] for _, _, t in flows]
    values = [a for _, a, _ in flows]

    colors = []
    for label in labels:
        if node_color_map and label in node_color_map:
            colors.append(node_color_map[label])
        else:
            colors.append("#1f77b4")

    node = dict(
        pad=node_padding,
        thickness=node_thickness,
        line=dict(color="black", width=0.5),
        label=labels,
        color=colors
    )

    link = dict(
        source=sources,
        target=targets,
        value=values,
        color=[f"rgba(153, 204, 255, {opacity})"] * len(values)
    )

    fig = go.Figure(data=[go.Sankey(node=node, link=link, arrangement="snap")])
    return fig


def generate_download_link(fig, file_format="png"):
    buffer = io.BytesIO()
    fig.write_image(buffer, format=file_format)
    b64 = base64.b64encode(buffer.getvalue()).decode()

    if file_format == "png":
        href = f'<a href="data:image/png;base64,{b64}" download="sankey_diagram.png">Download PNG</a>'
    else:
        href = f'<a href="data:image/svg+xml;base64,{b64}" download="sankey_diagram.svg">Download SVG</a>'
    return href

# ---------------
# Streamlit App
# ---------------
def main():
    st.title("Sankey Diagrams for FP&A")

    # Add an introductory section
    st.markdown("""
    **What is a Sankey Diagram?**  
    A Sankey diagram is a type of **flow diagram** where the width of each arrow (link)
    is proportional to the amount or quantity of that flow. It provides a clear, visually
    compelling way to see how resources move or distribute among various categories.
    """)

    # Add text and image
    st.title("Do you know what is a Sankey Diagram? Let me show you some examples:")
    image_url = "https://raw.githubusercontent.com/The-Financial-Fox/streamlit-apps/refs/heads/main/sankey/Sankey%20Diagram%20for%20Finance.png"
    st.image(image_url, caption="Example of a Sankey Diagram", use_container_width=True)

    st.markdown("""
    **Why is this useful for FP&A?**  
    In **Financial Planning & Analysis (FP&A)**, Sankey diagrams help you:
    - Clearly understand the **allocation** of budgets across different departments and cost centers.
    - Quickly spot **high-impact** cost drivers and areas where efficiency could be improved.
    - Visualize end-to-end **money flows** from revenue sources through to expenses or savings.
    
    By seeing the entire flow in one place, FP&A teams can make **better-informed decisions**
    and communicate financial insights more effectively to stakeholders.
    """)

    # Sidebar controls
    st.sidebar.header("Data Input Options")
    uploaded_file = st.sidebar.file_uploader(
        "Upload CSV or Excel (with columns: Source, Amount, Target)",
        type=["csv", "xlsx", "xls"]
    )

    manual_flows_text = st.sidebar.text_area(
        "Or input flows manually in the format:\n\nSource [Amount] Target",
        height=150
    )

    node_thickness = st.sidebar.slider("Node Thickness", 10, 50, 20)
    node_padding = st.sidebar.slider("Node Padding", 10, 50, 20)
    link_opacity = st.sidebar.slider("Link Opacity", 0.1, 1.0, 0.6)

    st.sidebar.header("Title Settings")
    chart_title = st.sidebar.text_input("Chart Title", value="Sankey Diagram")
    title_font_family = st.sidebar.selectbox(
        "Title Font Family",
        ["Arial", "Times New Roman", "Courier New", "Verdana", "Helvetica"],
        index=0
    )
    title_font_size = st.sidebar.slider("Title Font Size", 12, 36, 20)

    st.sidebar.header("Node Label Font")
    node_label_font_family = st.sidebar.selectbox(
        "Node Label Font Family",
        ["Arial", "Times New Roman", "Courier New", "Verdana", "Helvetica"],
        index=0
    )
    node_label_font_size = st.sidebar.slider("Node Label Font Size", 8, 24, 12)

    flows = []
    if uploaded_file:
        file_flows = load_data_from_file(uploaded_file)
        flows.extend(file_flows)

    if manual_flows_text.strip():
        text_flows = parse_flow_text(manual_flows_text)
        flows.extend(text_flows)

    if not flows:
        st.info("No flows available. Upload a file or input flows manually.")
        return

    unique_nodes = set()
    for s, amt, t in flows:
        unique_nodes.add(s)
        unique_nodes.add(t)
    unique_nodes = sorted(list(unique_nodes))

    st.sidebar.header("Node Color Customization")
    st.sidebar.write("Pick a color for each node:")
    node_color_map = {}
    for node in unique_nodes:
        color_default = "#1f77b4"
        chosen_color = st.sidebar.color_picker(f"{node}", color_default)
        node_color_map[node] = chosen_color

    fig = build_sankey(
        flows,
        node_color_map=node_color_map,
        node_thickness=node_thickness,
        node_padding=node_padding,
        opacity=link_opacity
    )

    fig.update_layout(
        title=dict(
            text=chart_title,
            font=dict(family=title_font_family, size=title_font_size)
        ),
        hovermode="x",
        margin=dict(l=50, r=50, t=50, b=50),
        width=1200,
        height=700,
        font=dict(
            family=node_label_font_family,
            size=node_label_font_size,
            color="black"
        )
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Export Diagram")
    col1, col2 = st.columns(2)

    with col1:
        if st.button("Download as PNG"):
            png_link = generate_download_link(fig, file_format="png")
            st.markdown(png_link, unsafe_allow_html=True)

    with col2:
        if st.button("Download as SVG"):
            svg_link = generate_download_link(fig, file_format="svg")
            st.markdown(svg_link, unsafe_allow_html=True)

    st.markdown("""
    ---
    **Technical Integration**  
    - **Plotly** (with Kaleido) for PNG/SVG export  
    - **Streamlit** for UI  
    - **GitHub** for version control  
    ---
    """)


if __name__ == "__main__":
    main()

st.markdown("""
---
### Built with ChatGPT by Christian Martinez  
Learn here how: [Click this link](https://www.linkedin.com/in/christianmartinezthefinancialfox/)
""", unsafe_allow_html=True)
