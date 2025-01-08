import streamlit as st

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Where Christian Eats in Amsterdam",
    page_icon="🍴",
    layout="wide"
)

# ---------- CUSTOM CSS FOR DARK STYLE ----------
st.markdown(
    """
    <style>
    body {
        background-color: #0F0F0F; /* Dark background */
        color: #FFFFFF;           /* White text */
    }
    .css-1n76uvr, .css-12oz5g7, .css-18e3th9, .css-hxt7ib {
        background-color: #0F0F0F !important;
    }
    /* Hide the default Streamlit hamburger menu & watermark if desired */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True
)

# ---------- APP TITLE / HEADER ----------
st.title("Where Christian Eats in Amsterdam")
st.write("Welcome! Select a food category below to see Christian's recommended spots.")

# ---------- RESTAURANT DATA ----------
restaurants_data = {
    "Best Mexican Eats 🫔🌮": [
        {
            "name": "Bacalar",
            "link": "https://bacalar.amsterdam/",
            "location": "Hugo de Grootkade 13, Amsterdam",
            "menu_highlights": "Tacos al Pastor, Guacamole, Margaritas",
            "price_range": "€€"
        },
        {
            "name": "Los Pilones",
            "link": "https://lospilones.com/",
            "location": "Various locations in Amsterdam",
            "menu_highlights": "Authentic Mexican Tacos, Tequila, Enchiladas",
            "price_range": "€€"
        },
        {
            "name": "LUPE",
            "link": "https://www.lupemexmex.com/",
            "location": "Van Woustraat 89, Amsterdam",
            "menu_highlights": "Tacos, Burritos, Quesadillas, Margaritas",
            "price_range": "€€"
        },
    ],
    "Best Pizzas 🍕": [
        {
            "name": "nNea",
            "link": "https://www.nneapizza.com/",
            "location": "Bilderdijkstraat 92, Amsterdam",
            "menu_highlights": "Neapolitan Pizza, Antipasti, Creative Toppings",
            "price_range": "€€-€€€"
        },
        {
            "name": "Pizza Project",
            "link": "https://www.pizzaproject.nl/en/",
            "location": "Czaar Peterstraat 45, Amsterdam",
            "menu_highlights": "Creative Pizza Varieties, Classic Italian Combos",
            "price_range": "€€"
        },
        {
            "name": "Mangia Pizza",
            "link": "https://mangiapizzagroup.nl/pages/about",
            "location": "Multiple locations, Amsterdam",
            "menu_highlights": "Traditional Italian Pizzas, Homemade Sauces",
            "price_range": "€€"
        },
        {
            "name": "La Perla",
            "link": "https://pizzaperla.nl/",
            "location": "Jordaan, Amsterdam",
            "menu_highlights": "Wood-Fired Pizza, Fresh Mozzarella",
            "price_range": "€€"
        },
        {
            "name": "Euro Pizza",
            "link": "https://www.europizza.rest/",
            "location": "Nieuwe Hemweg, Houthavens, Amsterdam",
            "menu_highlights": "Gourmet Pizza, Fresh Ingredients",
            "price_range": "€€"
        },
    ],
    "Shared Dining Favorites": [
        {
            "name": "Cafe Binnenvisser",
            "link": "https://binnenvisser.nl/menu",
            "location": "De Clercqstraat 82, Amsterdam",
            "menu_highlights": "Seasonal Small Plates, Natural Wines",
            "price_range": "€€-€€€"
        },
        {
            "name": "Bar Parry",
            "link": "https://barparry.nl/site/en/menu/",
            "location": "Spaarndammerstraat 52, Amsterdam",
            "menu_highlights": "Shared Plates, Bistro Fare, Cocktails",
            "price_range": "€€-€€€"
        },
        {
            "name": "Petit Caron",
            "link": "https://petitcaron.nl/",
            "location": "Gerard Douplein 8, Amsterdam",
            "menu_highlights": "French Bistro Dishes, Charcuterie, Wine",
            "price_range": "€€-€€€"
        },
        # ... truncated for brevity; put all from your data ...
    ],
    # ... Add all the rest of the categories and their data ...
}

# If you have a big dictionary, ensure all categories are included,
# or break them into smaller chunks.

# ---------- CATEGORY ORDER & ICONS ----------
category_list = list(restaurants_data.keys())

# Just some example icons or emoji placeholders. 
# Make sure the length matches or is >= the category_list length.
icons = [
    "https://em-content.zobj.net/thumbs/240/apple/354/taco_1f32e.png",   # Mexican
    "https://em-content.zobj.net/thumbs/240/apple/354/pizza_1f355.png", # Pizza
    "https://em-content.zobj.net/thumbs/240/apple/354/fork-and-knife_1f374.png", # Dining
    "https://em-content.zobj.net/thumbs/240/apple/354/collision_1f4a5.png",
    "https://em-content.zobj.net/thumbs/240/apple/354/star_2b50.png",
    # add or repeat as necessary...
]

# ---------- CREATE CATEGORY CARDS ----------
selected_category = None

# We’ll place 3 columns per row (you can adjust as you wish).
cols_per_row = 3
for i, category in enumerate(category_list):
    if i % cols_per_row == 0:
        # start a new row
        columns = st.columns(cols_per_row)

    # determine which column we’re in
    col = columns[i % cols_per_row]

    with col:
        # show an image if available, else show an emoji
        if i < len(icons):
            col.image(icons[i], width=60)
        # create a button for the category
        if col.button(category):
            selected_category = category

# ---------- IF USER SELECTED A CATEGORY, SHOW THE RESTAURANTS ----------
if selected_category:
    st.subheader(f"**{selected_category}**")
    for r in restaurants_data[selected_category]:
        st.markdown(f"### {r['name']}")
        if r["link"] and r["link"] != "No official link":
            st.markdown(f"- **Website**: [{r['link']}]({r['link']})")
        else:
            st.markdown(f"- **Website**: *No official link*")
        st.markdown(f"- **Location**: {r['location']}")
        st.markdown(f"- **Menu Highlights**: {r['menu_highlights']}")
        st.markdown(f"- **Price Range**: {r['price_range']}")
        st.markdown("---")
