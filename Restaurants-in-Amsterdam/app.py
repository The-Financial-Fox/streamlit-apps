import streamlit as st
from streamlit-extras.clickable_images import clickable_images

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
st.write("Welcome! Click on a food category below to see Christian's recommended spots.")

# ---------- RESTAURANT DATA (FULL LIST) ----------
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
        {
            "name": "Bar du Champagne",
            "link": "https://barduchampagne.nl/",
            "location": "Ruysdaelkade 41, Amsterdam",
            "menu_highlights": "Champagne & Sparkling Wines, Small Bites",
            "price_range": "€€€"
        },
        {
            "name": "Gertrude",
            "link": "https://www.gertrudeamsterdam.nl/",
            "location": "De Pijp, Amsterdam",
            "menu_highlights": "Seasonal Shared Dishes, Natural Wines",
            "price_range": "€€-€€€"
        },
        {
            "name": "Bar Fisk",
            "link": "https://amsterdamwonderland.com/bar-fisk/",
            "location": "De Pijp, Amsterdam",
            "menu_highlights": "Tel Aviv-Inspired Seafood, Meze Plates",
            "price_range": "€€-€€€"
        },
        {
            "name": "Cornerstore",
            "link": "https://csnoord.com/",
            "location": "Gedempt Hamerkanaal 201, Amsterdam-Noord",
            "menu_highlights": "Modern Shared Plates, Chef-Driven Menu",
            "price_range": "€€€"
        },
        {
            "name": "Bar Bambino",
            "link": "https://bambinobar.nl/en/",
            "location": "Ferdinand Bolstraat 9, Amsterdam",
            "menu_highlights": "Italian-Inspired Small Plates, Cocktails",
            "price_range": "€€-€€€"
        },
        {
            "name": "VRR",
            "link": "https://vrr.rest/",
            "location": "Oostenburg, Amsterdam",
            "menu_highlights": "Modern European Plates, Wine Selection",
            "price_range": "€€€"
        },
        {
            "name": "Helling 7",
            "link": "https://www.helling7.nl/",
            "location": "NDSM, Amsterdam-Noord",
            "menu_highlights": "Shared Courses, Modern Dutch Cuisine",
            "price_range": "€€€"
        },
        {
            "name": "Bar Beurre",
            "link": "https://www.cafebeurreamsterdam.nl/",
            "location": "Utrechtsedwarsstraat 131, Amsterdam",
            "menu_highlights": "French-Inspired Small Plates, Wines",
            "price_range": "€€-€€€"
        },
        {
            "name": "Appolonia",
            "link": "No official link",
            "location": "Amsterdam (various)",
            "menu_highlights": "Seasonal or Bistro Plates (Limited info)",
            "price_range": "€€-€€€"
        },
        {
            "name": "De Willem",
            "link": "No official link",
            "location": "Amsterdam (various)",
            "menu_highlights": "Bistro or Shared Dining Style",
            "price_range": "€€"
        },
        {
            "name": "Alba",
            "link": "No official link",
            "location": "Amsterdam-Noord? (Limited info)",
            "menu_highlights": "Seasonal Plates, Wine",
            "price_range": "€€-€€€"
        },
        {
            "name": "Coba",
            "link": "No official link",
            "location": "Amsterdam-Noord (Likely)",
            "menu_highlights": "Contemporary Mexican, Mezcal",
            "price_range": "€€-€€€"
        },
        {
            "name": "Metro",
            "link": "No official link",
            "location": "Amsterdam (Limited info)",
            "menu_highlights": "Contemporary Casual Dining",
            "price_range": "€€"
        },
        {
            "name": "Wijmpje Beukers",
            "link": "No official link",
            "location": "Kinkerstraat area, Amsterdam",
            "menu_highlights": "Modern Bistro Plates, Wine",
            "price_range": "€€-€€€"
        },
        {
            "name": "Chateau Amsterdam",
            "link": "No official link",
            "location": "Gedempt Hamerkanaal, Amsterdam-Noord",
            "menu_highlights": "Urban Winery, Tasting Menus",
            "price_range": "€€-€€€"
        },
    ],
    "Buzzing Places": [
        {
            "name": "Klaproos",
            "link": "No official link",
            "location": "Amsterdam-Noord",
            "menu_highlights": "Pizza or Modern Bar Scene",
            "price_range": "€€"
        },
        {
            "name": "Kikkie",
            "link": "No official link",
            "location": "Amsterdam (Limited info)",
            "menu_highlights": "Modern Bar or Restaurant Concept",
            "price_range": "€€"
        },
        {
            "name": "Twee Prinsen",
            "link": "No official link",
            "location": "Amsterdam (Limited info)",
            "menu_highlights": "Bar/Restaurant with Local Vibe",
            "price_range": "€€"
        },
        {
            "name": "Murmur",
            "link": "No official link",
            "location": "Amsterdam",
            "menu_highlights": "Lively Bar, Possibly Small Bites",
            "price_range": "€€"
        },
        {
            "name": "Skatecafe",
            "link": "No official link",
            "location": "Gedempt Hamerkanaal 42, Amsterdam-Noord",
            "menu_highlights": "Skate Ramp + Café, Casual Food",
            "price_range": "€€"
        },
    ],
    "Always Good": [
        {
            "name": "Petit Caron",
            "link": "https://petitcaron.nl/",
            "location": "Gerard Douplein, Amsterdam",
            "menu_highlights": "French Bistro Staples, Wine",
            "price_range": "€€-€€€"
        },
        {
            "name": "Pastis",
            "link": "No official link",
            "location": "Likely Jordaan, Amsterdam",
            "menu_highlights": "Classic French Bistro Dishes",
            "price_range": "€€"
        },
        {
            "name": "Donna Sofia",
            "link": "No official link",
            "location": "Amsterdam",
            "menu_highlights": "Italian Trattoria Fare",
            "price_range": "€€"
        },
        {
            "name": "Cradam",
            "link": "No official link",
            "location": "Amsterdam",
            "menu_highlights": "Local Bar/Restaurant (Limited info)",
            "price_range": "€€"
        },
        {
            "name": "De Plantage",
            "link": "No official link",
            "location": "Plantage Kerklaan, near Artis Zoo",
            "menu_highlights": "Refined Brasserie, Glasshouse Setting",
            "price_range": "€€-€€€"
        },
        {
            "name": "Pekelharing",
            "link": "No official link",
            "location": "De Pijp area (likely)",
            "menu_highlights": "Dutch or Mediterranean-Inspired",
            "price_range": "€€"
        },
        {
            "name": "Cantine de Caron",
            "link": "No official link",
            "location": "Amsterdam",
            "menu_highlights": "French/Euro Bistro, Caron Family",
            "price_range": "€€-€€€"
        },
        {
            "name": "Alex + Pinard",
            "link": "No official link",
            "location": "Amsterdam",
            "menu_highlights": "Wine-Focused Bistro, Small Plates",
            "price_range": "€€-€€€"
        },
        {
            "name": "Chez Nina",
            "link": "No official link",
            "location": "Amsterdam",
            "menu_highlights": "French or Modern Fusion (Limited info)",
            "price_range": "€€"
        },
        {
            "name": "Goudfazant",
            "link": "No official link",
            "location": "Meeuwenlaan 98, Amsterdam-Noord",
            "menu_highlights": "French-Dutch Cuisine, Industrial Space",
            "price_range": "€€-€€€"
        },
        {
            "name": "Toscanini",
            "link": "No official link",
            "location": "Lindengracht, Jordaan",
            "menu_highlights": "Classic Italian Dishes, Fresh Pasta",
            "price_range": "€€€"
        },
    ],
    "Very Good but Expensive ($$)": [
        {
            "name": "4850",
            "link": "No official link",
            "location": "Amsterdam (likely East)",
            "menu_highlights": "Specialty Coffee by Day, Tasting Menu Dinner",
            "price_range": "€€€"
        },
        {
            "name": "La Fiorita",
            "link": "No official link",
            "location": "Amsterdam",
            "menu_highlights": "Upscale Italian Cuisine",
            "price_range": "€€€"
        },
        {
            "name": "Gouden Reaal",
            "link": "No official link",
            "location": "Near Haarlemmerdijk? Amsterdam",
            "menu_highlights": "Classic Dutch/French Dishes, Cozy Vibe",
            "price_range": "€€€"
        },
        {
            "name": "Parlotte",
            "link": "No official link",
            "location": "Amsterdam",
            "menu_highlights": "Wine Bar + Bistro Plates",
            "price_range": "€€€"
        },
        {
            "name": "Scheepskameel",
            "link": "No official link",
            "location": "Kattenburgerstraat, Marineterrein",
            "menu_highlights": "Modern Dutch Menu, Extensive Wine List",
            "price_range": "€€€"
        },
        {
            "name": "Domenica",
            "link": "No official link",
            "location": "Amsterdam",
            "menu_highlights": "Modern Italian or Mediterranean",
            "price_range": "€€€"
        },
        {
            "name": "Cafe de Klepel",
            "link": "No official link",
            "location": "Jordaan, Amsterdam",
            "menu_highlights": "Classic French Cuisine, Great Wines",
            "price_range": "€€€"
        },
        {
            "name": "Entrepot",
            "link": "No official link",
            "location": "Entrepotdok, Amsterdam",
            "menu_highlights": "Seasonal Local Produce, Creative Plates",
            "price_range": "€€€"
        },
        {
            "name": "Gebroeders Hartering",
            "link": "No official link",
            "location": "Peperstraat 10, Amsterdam",
            "menu_highlights": "Refined Dutch-French, Tasting Menus",
            "price_range": "€€€"
        },
        {
            "name": "Watergang",
            "link": "No official link",
            "location": "Watergang (just north of Amsterdam)",
            "menu_highlights": "Farm-to-Table or Local Produce",
            "price_range": "€€€"
        },
    ],
    "Really Good but Very Expensive ($$$)": [
        {
            "name": "Rijsel",
            "link": "No official link",
            "location": "Marcusstraat 52, Amsterdam (East)",
            "menu_highlights": "French-Flemish Cuisine, Set Menu",
            "price_range": "€€€-€€€€"
        },
        {
            "name": "Choux",
            "link": "No official link",
            "location": "De Ruijterkade 128, Amsterdam",
            "menu_highlights": "Modern Creative Cuisine, Seasonal",
            "price_range": "€€€-€€€€"
        },
        {
            "name": "De Zoldering",
            "link": "No official link",
            "location": "Amsterdam (info limited)",
            "menu_highlights": "High-End Dining (Likely Michelin-level)",
            "price_range": "€€€-€€€€"
        },
        {
            "name": "Cafe de Parel",
            "link": "No official link",
            "location": "Jordaan, Amsterdam",
            "menu_highlights": "Modern Bistro Tasting Menu, Upscale Pub Feel",
            "price_range": "€€€-€€€€"
        },
        {
            "name": "Juwelier",
            "link": "No official link",
            "location": "Amsterdam (9 Streets? Info limited)",
            "menu_highlights": "High-End Bistro/Fine Dining",
            "price_range": "€€€-€€€€"
        },
        {
            "name": "Wils",
            "link": "No official link",
            "location": "Stadionplein, Amsterdam",
            "menu_highlights": "Michelin-Star Concept, Open-Fire Cooking",
            "price_range": "€€€€"
        },
        {
            "name": "Breda",
            "link": "No official link",
            "location": "Singel 210, Amsterdam",
            "menu_highlights": "Modern European Tasting Menus",
            "price_range": "€€€€"
        },
    ],
    "Other": [
        {
            "name": "Kyo",
            "link": "No official link",
            "location": "Amsterdam",
            "menu_highlights": "Possibly Japanese Concept",
            "price_range": "€€-€€€"
        },
        {
            "name": "Thai Thai Poppetje",
            "link": "No official link",
            "location": "Amsterdam",
            "menu_highlights": "Thai Street-Food Style",
            "price_range": "€€"
        },
        {
            "name": "Kaagman & Kortekaas",
            "link": "No official link",
            "location": "Amsterdam Center",
            "menu_highlights": "Seasonal, Creative Dutch-French",
            "price_range": "€€€-€€€€"
        },
        {
            "name": "Public Space",
            "link": "No official link",
            "location": "Overhoeksplein 2, Amsterdam-Noord",
            "menu_highlights": "Café & Bar, Pastries, Brunch",
            "price_range": "€-€€"
        },
        {
            "name": "Barentsz",
            "link": "No official link",
            "location": "Barentszstraat, Amsterdam",
            "menu_highlights": "Contemporary Bistro or Bar",
            "price_range": "€€"
        },
        {
            "name": "Vander Veen",
            "link": "No official link",
            "location": "Amsterdam-Noord",
            "menu_highlights": "Possibly Concept Store + Café",
            "price_range": "€-€€"
        },
        {
            "name": "Stork",
            "link": "No official link",
            "location": "Gedempt Hamerkanaal, Amsterdam-Noord",
            "menu_highlights": "Fish/Seafood Restaurant, Large Terrace",
            "price_range": "€€-€€€"
        },
        {
            "name": "Pllek",
            "link": "No official link",
            "location": "NDSM Wharf, Amsterdam-Noord",
            "menu_highlights": "International Menu, Beach Vibe",
            "price_range": "€€"
        },
        {
            "name": "Noorderlicht Cafe",
            "link": "No official link",
            "location": "NDSM Wharf, Amsterdam-Noord",
            "menu_highlights": "Organic, Vegetarian-Friendly, Live Music",
            "price_range": "€€"
        },
        {
            "name": "Skatecafe",
            "link": "No official link",
            "location": "Amsterdam-Noord",
            "menu_highlights": "Skate Ramp + Café, Events",
            "price_range": "€€"
        },
        {
            "name": "De Ceuvel",
            "link": "No official link",
            "location": "Korte Papaverweg 4, Amsterdam-Noord",
            "menu_highlights": "Eco-Friendly Café, Cultural Space",
            "price_range": "€-€€"
        },
    ],
    "For Drinks 🍺": [
        {
            "name": "Cafe Thijssen",
            "link": "No official link",
            "location": "Brouwersgracht area, Amsterdam",
            "menu_highlights": "Dutch Bar Vibe, Local Beers, Snacks",
            "price_range": "€-€€"
        },
        {
            "name": "Noorderlicht Cafe",
            "link": "No official link",
            "location": "NDSM Wharf, Amsterdam-Noord",
            "menu_highlights": "Organic Beers, Live Music",
            "price_range": "€€"
        },
        {
            "name": "Fabus",
            "link": "https://www.fabusamsterdam.com/",
            "location": "De Pijp, Amsterdam",
            "menu_highlights": "Wine Bar, Small Bites",
            "price_range": "€€-€€€"
        },
        {
            "name": "Murmur",
            "link": "No official link",
            "location": "Amsterdam",
            "menu_highlights": "Cocktails, Possible Small Plates",
            "price_range": "€€"
        },
        {
            "name": "QV Winebar",
            "link": "https://maps.app.goo.gl/uwVxrFDG94Jj5uEJ9",
            "location": "Huidenstraat area, Amsterdam",
            "menu_highlights": "Extensive Wine List, Charcuterie",
            "price_range": "€€-€€€"
        },
        {
            "name": "Wijnbar Paulus",
            "link": "https://www.wijnbarpaulus.nl/",
            "location": "De Pijp, Amsterdam",
            "menu_highlights": "Wines from Small Producers, Nibbles",
            "price_range": "€€-€€€"
        },
        {
            "name": "Pllek",
            "link": "No official link",
            "location": "NDSM, Amsterdam-Noord",
            "menu_highlights": "Beers, Cocktails, International Bites",
            "price_range": "€€"
        },
        {
            "name": "De Ceuvel",
            "link": "No official link",
            "location": "Amsterdam-Noord",
            "menu_highlights": "Craft Beers, Eco-Friendly Venue",
            "price_range": "€€"
        },
        {
            "name": "Cafe de Magere Brug",
            "link": "No official link",
            "location": "Near Magere Brug (Skinny Bridge)",
            "menu_highlights": "Classic Amsterdam Café, Canal View",
            "price_range": "€€"
        },
        {
            "name": "Hendrix",
            "link": "No official link",
            "location": "Amsterdam",
            "menu_highlights": "Gin & Tonics, Cocktails",
            "price_range": "€€"
        },
        {
            "name": "Bar Bonnie",
            "link": "No official link",
            "location": "Amstelveenseweg area, Amsterdam",
            "menu_highlights": "Cocktails, Bites, Modern Interior",
            "price_range": "€€"
        },
        {
            "name": "Bar Arie",
            "link": "No official link",
            "location": "Amsterdam (possibly West)",
            "menu_highlights": "Neighborhood Bar, Craft Beers, Pub Food",
            "price_range": "€€"
        },
        {
            "name": "Volt",
            "link": "No official link",
            "location": "Ferdinand Bolstraat, De Pijp, Amsterdam",
            "menu_highlights": "Cocktails, Modern Bar Vibe",
            "price_range": "€€"
        },
        {
            "name": "Gambrinus",
            "link": "No official link",
            "location": "De Pijp? Amsterdam",
            "menu_highlights": "Traditional Café, Beers on Tap",
            "price_range": "€-€€"
        },
        {
            "name": "Cafe Kiebert",
            "link": "No official link",
            "location": "Amsterdam (limited info)",
            "menu_highlights": "Classic Dutch Cafe, Local Beer",
            "price_range": "€€"
        },
        {
            "name": "De Walvis",
            "link": "No official link",
            "location": "Spaarndammerbuurt, Amsterdam",
            "menu_highlights": "Cozy Bar, Beers, Snacks",
            "price_range": "€€"
        },
        {
            "name": "Ceppi’s",
            "link": "No official link",
            "location": "Amsterdam (info limited)",
            "menu_highlights": "Wine Bar or Café (Possibly Italian-Inspired)",
            "price_range": "€€-€€€"
        },
    ],
    "For Coffee": [
        {
            "name": "Distrikt Coffee",
            "link": "No official link",
            "location": "Amsterdam (various)",
            "menu_highlights": "Specialty Coffee, Pastries",
            "price_range": "€"
        },
        {
            "name": "Black and Bloom",
            "link": "No official link",
            "location": "Amsterdam (origin in Groningen?)",
            "menu_highlights": "Specialty Coffee Roasters",
            "price_range": "€"
        },
        {
            "name": "Caffenation",
            "link": "No official link",
            "location": "Ferdinand Bolstraat, Amsterdam",
            "menu_highlights": "Belgian Roaster, Espresso & Filter",
            "price_range": "€"
        },
        {
            "name": "Anne & Max",
            "link": "No official link",
            "location": "Multiple Locations, Amsterdam",
            "menu_highlights": "Coffee, Breakfast, Lunch",
            "price_range": "€-€€"
        },
        {
            "name": "Uncommon",
            "link": "No official link",
            "location": "Amsterdam",
            "menu_highlights": "Specialty Coffee, Unique Origins",
            "price_range": "€"
        },
        {
            "name": "Bocca",
            "link": "No official link",
            "location": "Kerkstraat 96, Amsterdam",
            "menu_highlights": "Specialty Roaster, Pour-Over, Espresso",
            "price_range": "€"
        },
        {
            "name": "Badeta",
            "link": "No official link",
            "location": "Amsterdam (Limited info)",
            "menu_highlights": "Coffee + Small Bites",
            "price_range": "€"
        },
        {
            "name": "Toki",
            "link": "No official link",
            "location": "Jordaan area, Amsterdam",
            "menu_highlights": "Specialty Coffee, Pastries",
            "price_range": "€"
        },
        {
            "name": "Yusu",
            "link": "No official link",
            "location": "Amsterdam (Limited info)",
            "menu_highlights": "Espresso, Cappuccino, Possibly Brunch",
            "price_range": "€"
        },
    ],
}

# ---------- ICONS FOR EACH CATEGORY ----------
# These are example emojis or random icons you can replace with your own images/URLs
category_list = [
    "Best Mexican Eats 🫔🌮",
    "Best Pizzas 🍕",
    "Shared Dining Favorites",
    "Buzzing Places",
    "Always Good",
    "Very Good but Expensive ($$)",
    "Really Good but Very Expensive ($$$)",
    "Other",
    "For Drinks 🍺",
    "For Coffee"
]

category_icons = [
    "https://em-content.zobj.net/thumbs/240/apple/354/taco_1f32e.png",       # Best Mexican
    "https://em-content.zobj.net/thumbs/240/apple/354/pizza_1f355.png",     # Best Pizza
    "https://em-content.zobj.net/thumbs/240/apple/354/fork-and-knife_1f374.png",  # Shared Dining
    "https://em-content.zobj.net/thumbs/240/apple/354/collision_1f4a5.png",       # Buzzing Places
    "https://em-content.zobj.net/thumbs/240/apple/354/star_2b50.png",             # Always Good
    "https://em-content.zobj.net/thumbs/240/apple/354/heavy-dollar-sign_1f4b2.png",  # Very Good but Expensive
    "https://em-content.zobj.net/thumbs/240/apple/354/banknote-with-dollar-sign_1f4b5.png", # Really Good but Very Expensive
    "https://em-content.zobj.net/thumbs/240/apple/354/gear_2699-fe0f.png",        # Other
    "https://em-content.zobj.net/thumbs/240/apple/354/beer-mug_1f37a.png",        # For Drinks
    "https://em-content.zobj.net/thumbs/240/apple/354/hot-beverage_2615.png",     # For Coffee
]

# ---------- CLICKABLE IMAGES FOR HOME PAGE ----------
clicked_index = clickable_images(
    paths=category_icons,
    titles=category_list,  # hover-text for each image
    div_style={
        "display": "flex",
        "justify-content": "center",
        "flex-wrap": "wrap",
        "gap": "25px"
    },
    img_style={
        "margin": "10px",
        "height": "100px",
        "border": "2px solid #444",
        "border-radius": "10%"
    }
)

# ---------- DISPLAY RESTAURANTS FOR SELECTED CATEGORY ----------
if clicked_index > -1:
    selected_category = category_list[clicked_index]
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
