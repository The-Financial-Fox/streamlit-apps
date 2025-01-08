import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import base64
import io

st.set_page_config(page_title="Sankey Diagrams for FP&A", layout="wide")

# ---------------
# Helper Functions
# ---------------
def parse_flow_text(flow_text: str):
    """
    Parse manual flow input of the form:
    Source [Amount] Target
    Returns a list of tuples (source, amount, target).
    """
    flows = []
    lines = flow_text.strip().split("\n")
    for line in lines:
        if not line.strip():
            continue
        # Example line: "Marketing [100000] Advertising"
        # We'll find the brackets and split accordingly
        try:
            # Splitting around brackets
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
    """
    Load CSV or Excel and expect columns: [Source, Amount, Target]
    Returns a list of tuples (source, amount, target).
    """
    if uploaded_file is None:
        return []

    file_name = uploaded_file.name.lower()
    if file_name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        # assume Excel
        df = pd.read_excel(uploaded_file)

    # Make sure we have the right columns
    required_cols = {"Source", "Amount", "Target"}
    if not required_cols.issubset(df.columns):
        st.error(f"Uploaded file must contain columns: {required_cols}")
        return []

    # Convert to list of tuples
    flows = [
        (row["Source"], row["Amount"], row["Target"]) for _, row in df.iterrows()
    ]
    return flows


def build_sankey(flows, node_color_map=None, node_thickness=20, node_padding=20, opacity=0.6):
    """
    Build a Plotly Sankey diagram given flows (list of (source, amount, target)).
    node_color_map can override default node colors. (dict node->color)
    Returns a Plotly figure.
    """
    # Gather node labels
    labels = []
    for source, amount, target in flows:
        if source not in labels:
            labels.append(source)
        if target not in labels:
            labels.append(target)

    # Build index mapping
    label_to_index = {label: i for i, label in enumerate(labels)}

    # Build source/target arrays
    sources = [label_to_index[s] for s, _, _ in flows]
    targets = [label_to_index[t] for _, _, t in flows]
    values = [a for _, a, _ in flows]

    # Decide node colors
    colors = []
    for label in labels:
        if node_color_map and label in node_color_map:
            colors.append(node_color_map[label])
        else:
            # default color
            colors.append("blue")  

    link = dict(source=sources, target=targets, value=values)

    # You can customize link color or use an array. For simplicity, we use "rgba(..., opacity)"
    # Setting alpha channel below for link color
    link_colors = [f"rgba(153, 204, 255, {opacity})"] * len(values)
    link["color"] = link_colors

    node = dict(
        pad=node_padding,
        thickness=node_thickness,
        line=dict(color="black", width=0.5),
        label=labels,
        color=colors
    )

    fig = go.Figure(
        data=[
            go.Sankey(
                node=node,
                link=link,
                arrangement="snap"  # or "freeform", "fixed", "snap"
            )
        ]
    )

    fig.update_layout(
        hovermode="x",
        margin=dict(l=50, r=50, t=50, b=50),
        width=1200,
        height=700,
    )
    return fig


def generate_download_link(fig, file_format="png"):
    """
    Generate a download link for the Plotly figure as an image (PNG or SVG).
    """
    # Convert figure to image data in memory
    buffer = io.BytesIO()
    if file_format == "png":
        fig.write_image(buffer, format="png")
        b64 = base64.b64encode(buffer.getvalue()).decode()
        href = f'<a href="data:image/png;base64,{b64}" download="sankey_diagram.png">Download PNG</a>'
    else:
        fig.write_image(buffer, format="svg")
        b64 = base64.b64encode(buffer.getvalue()).decode()
        href = f'<a href="data:image/svg+xml;base64,{b64}" download="sankey_diagram.svg">Download SVG</a>'
    return href


# ---------------
# Streamlit App
# ---------------
def main():
    st.title("Sankey Diagrams for FP&A")
    st.markdown("""
    Empower your Financial Planning & Analysis (FP&A) team to visualize and analyze budget flows using interactive Sankey diagrams.
    """)

    # Sidebar for input selection
    st.sidebar.header("Data Input Options")

    # 1) Upload file
    uploaded_file = st.sidebar.file_uploader("Upload CSV/Excel with columns: Source, Amount, Target", type=["csv", "xlsx", "xls"])

    # 2) Manual text input
    manual_flows_text = st.sidebar.text_area(
        "Or input flows manually in the format:\n\nSource [Amount] Target",
        height=200
    )

    # 3) Node thickness, node padding, link opacity
    node_thickness = st.sidebar.slider("Node Thickness", min_value=10, max_value=50, value=20)
    node_padding = st.sidebar.slider("Node Padding", min_value=10, max_value=50, value=20)
    link_opacity = st.sidebar.slider("Link Opacity", min_value=0.1, max_value=1.0, value=0.6)

    # Collect flows
    flows = []
    if uploaded_file is not None:
        file_flows = load_data_from_file(uploaded_file)
        flows.extend(file_flows)

    if manual_flows_text.strip():
        text_flows = parse_flow_text(manual_flows_text)
        flows.extend(text_flows)

    if not flows:
        st.info("No flows available. Upload a file or input flows manually.")
        return

    # Build Sankey diagram
    fig = build_sankey(
        flows,
        node_thickness=node_thickness,
        node_padding=node_padding,
        opacity=link_opacity
    )

    st.plotly_chart(fig, use_container_width=True)

    # Export options
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
    - **Plotly** is used for generating the Sankey diagram.  
    - **Streamlit** for UI.  
    - **GitHub** for version control and collaboration.  
    ---
    """)


if __name__ == "__main__":
    main()
