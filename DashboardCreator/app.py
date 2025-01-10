st.subheader("Generated Visualization")
if chart_type == "Heatmap":
    if color in num_cols:  # Ensure "Color Dimension" is numerical
        heatmap_fig = px.density_heatmap(
            df, 
            x=x_axis, 
            y=y_axis, 
            z=color, 
            histfunc="sum", 
            color_continuous_scale="Viridis",
            title=f"Heatmap of {color} by {x_axis} and {y_axis}"
        )
        st.plotly_chart(heatmap_fig, use_container_width=True)
    else:
        st.warning(
            "Heatmap requires a numerical column for the color dimension. "
            "Please select a valid numerical column for 'Color Dimension (Optional)'."
        )
elif chart_type == "Boxplot":
    boxplot_fig = px.box(
        df, 
        x=x_axis, 
        y=y_axis, 
        color=color,
        title=f"Boxplot of {y_axis} by {x_axis}"
    )
    st.plotly_chart(boxplot_fig, use_container_width=True)
elif chart_type == "Bar Graph":
    bar_fig = px.bar(
        df, 
        x=x_axis, 
        y=y_axis, 
        color=color,
        title=f"Bar Graph of {y_axis} by {x_axis}"
    )
    st.plotly_chart(bar_fig, use_container_width=True)
else:
    st.info("Select a valid chart type.")
