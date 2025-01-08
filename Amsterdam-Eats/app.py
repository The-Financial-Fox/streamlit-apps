import streamlit as st

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Where The Nest Eats in Amsterdam",
    page_icon="🍴",
    layout="wide"
)

# ---------- CUSTOM CSS FOR DARK STYLE (optional) ----------
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
    #MainMenu {visibility: hidden;} /* Hide Streamlit hamburger menu */
    footer {visibility: hidden;}     /* Hide "Made with Streamlit" footer */
    </style>
    """,
    unsafe_allow_html=True
)

# ---------- APP TITLE / HEADER ----------
st.title("Where Christian Eats in Amsterdam")
st.write("Welcome! Select a **food category** below to explore the recommended spots.")

# ---------- RESTAURANT DATA (COMPLETE) ----------
# Organized by Category, each entry includes: Name, Website, Location, Key Menu Items, Price Range, Notes
restaurants_data = {
    "Best Mexican Eats 🫔🌮": [
        {
            "name": "Bacalar",
            "website": "https://bacalar.amsterdam",
            "location": "Hugo de Grootkade 13, Amsterdam",
            "menu_items": "Tacos al Pastor, Guacamole, Margaritas",
            "price_range": "€€",
            "notes": "Modern Mexican concept, cozy atmosphere"
        },
        {
            "name": "Los Pilones",
            "website": "https://lospilones.com",
            "location": "Various locations in Amsterdam",
            "menu_items": "Authentic Mexican tacos, enchiladas, tequila",
            "price_range": "€€",
            "notes": "Several branches around the city"
        },
        {
            "name": "LUPE",
            "website": "https://www.lupemexmex.com",
            "location": "Van Woustraat 89, Amsterdam",
            "menu_items": "Tacos, burritos, quesadillas, margaritas",
            "price_range": "€€",
            "notes": "Casual Mexican with a Tex-Mex touch"
        },
    ],
    "Best Pizzas 🍕": [
        {
            "name": "nNea",
            "website": "https://www.nneapizza.com",
            "location": "Bilderdijkstraat 92, Amsterdam",
            "menu_items": "Neapolitan-style pizza, antipasti",
            "price_range": "€€-€€€",
            "notes": "Known for high-quality dough & innovative toppings"
        },
        {
            "name": "Pizza Project",
            "website": "https://www.pizzaproject.nl",
            "location": "Czaar Peterstraat 45, Amsterdam",
            "menu_items": "Creative pizza varieties, classic Italian combos",
            "price_range": "€€",
            "notes": "Modern pizzeria vibe"
        },
        {
            "name": "Mangia Pizza",
            "website": "https://mangiapizzagroup.nl",
            "location": "Several locations in Amsterdam",
            "menu_items": "Traditional Italian pizzas, homemade sauces",
            "price_range": "€€",
            "notes": "Family-friendly atmosphere"
        },
        {
            "name": "La Perla",
            "website": "https://pizzaperla.nl",
            "location": "Jordaan area, Amsterdam",
            "menu_items": "Wood-fired pizza, fresh mozzarella",
            "price_range": "€€",
            "notes": "Popular neighborhood spot, often busy"
        },
        {
            "name": "Euro Pizza",
            "website": "https://www.europizza.rest",
            "location": "Nieuwe Hemweg, Amsterdam (Houthavens)",
            "menu_items": "Gourmet pizza, fresh ingredients",
            "price_range": "€€",
            "notes": "Trendy location in developing area"
        },
    ],
    "Shared Dining Favorites": [
        {
            "name": "Cafe Binnenvisser",
            "website": "https://binnenvisser.nl",
            "location": "De Clercqstraat 82, Amsterdam",
            "menu_items": "Seasonal small plates, natural wines",
            "price_range": "€€-€€€",
            "notes": "Known for cozy, minimalist vibe"
        },
        {
            "name": "Bar Parry",
            "website": "https://barparry.nl",
            "location": "Spaarndammerstraat 52, Amsterdam",
            "menu_items": "Shared plates, bistro fare, cocktails",
            "price_range": "€€-€€€",
            "notes": "Friendly neighborhood atmosphere"
        },
        {
            "name": "Petit Caron",
            "website": "https://petitcaron.nl",
            "location": "Gerard Douplein 8, Amsterdam",
            "menu_items": "French bistro dishes, charcuterie, wine",
            "price_range": "€€-€€€",
            "notes": "Offshoot of the Caron family restaurants"
        },
        {
            "name": "Bar du Champagne",
            "website": "https://barduchampagne.nl",
            "location": "Ruysdaelkade 41, Amsterdam",
            "menu_items": "Champagne & sparkling wines, small plates",
            "price_range": "€€€",
            "notes": "Chic, intimate bar"
        },
        {
            "name": "Gertrude",
            "website": "https://www.gertrudeamsterdam.nl",
            "location": "De Pijp area, Amsterdam",
            "menu_items": "Seasonal shared dishes, natural wines",
            "price_range": "€€-€€€",
            "notes": "Laid-back vibe, rotating menu"
        },
        {
            "name": "Bar Fisk",
            "website": "https://amsterdamwonderland.com/bar-fisk/",
            "location": "De Pijp, Amsterdam",
            "menu_items": "Tel Aviv-inspired seafood, meze plates",
            "price_range": "€€-€€€",
            "notes": "Mediterranean flair, lively atmosphere"
        },
        {
            "name": "Cornerstore",
            "website": "https://csnoord.com",
            "location": "Gedempt Hamerkanaal 201, Amsterdam-Noord",
            "menu_items": "Shared plates, innovative chef-driven menu",
            "price_range": "€€€",
            "notes": "Industrial-chic setting"
        },
        {
            "name": "Bar Bambino",
            "website": "https://bambinobar.nl",
            "location": "Ferdinand Bolstraat 9, Amsterdam",
            "menu_items": "Italian-inspired small plates, cocktails",
            "price_range": "€€-€€€",
            "notes": "Cozy bar & eatery"
        },
        {
            "name": "VRR",
            "website": "https://vrr.rest",
            "location": "Oostenburg, Amsterdam",
            "menu_items": "Modern European plates, wine",
            "price_range": "€€€",
            "notes": "Stylish interior, seasonal menu"
        },
        {
            "name": "Helling 7",
            "website": "https://www.helling7.nl",
            "location": "NDSM, Amsterdam-Noord",
            "menu_items": "Shared courses, modern Dutch cuisine",
            "price_range": "€€€",
            "notes": "Waterfront location, industrial vibe"
        },
        {
            "name": "Bar Beurre",
            "website": "https://www.cafebeurreamsterdam.nl",
            "location": "Utrechtsedwarsstraat 131, Amsterdam",
            "menu_items": "French-inspired small plates, wines",
            "price_range": "€€-€€€",
            "notes": "Neighborhood bistro feel"
        },
        {
            "name": "Appolonia",
            "website": None,
            "location": "Amsterdam (various)",
            "menu_items": "Seasonal or bistro plates (info limited)",
            "price_range": "€€-€€€",
            "notes": "Possibly a local hidden gem"
        },
        {
            "name": "De Willem",
            "website": None,
            "location": "Amsterdam (various)",
            "menu_items": "Bistro or shared dining style (info limited)",
            "price_range": "€€",
            "notes": "Little public info—check locally"
        },
        {
            "name": "Alba",
            "website": None,
            "location": "Possibly Amsterdam-Noord",
            "menu_items": "Seasonal plates, wine (info limited)",
            "price_range": "€€-€€€",
            "notes": "Word-of-mouth favorite"
        },
        {
            "name": "Coba",
            "website": None,
            "location": "Amsterdam-Noord?",
            "menu_items": "Contemporary Mexican cuisine, mezcal? (info limited)",
            "price_range": "€€-€€€",
            "notes": "Rising star in Noord, if correct"
        },
        {
            "name": "Metro",
            "website": None,
            "location": "Amsterdam",
            "menu_items": "Contemporary casual dining (info limited)",
            "price_range": "€€",
            "notes": "Check local guides"
        },
        {
            "name": "Wijmpje Beukers",
            "website": None,
            "location": "Kinkerstraat area, Amsterdam",
            "menu_items": "Shared modern bistro plates, wine",
            "price_range": "€€-€€€",
            "notes": "Cozy, small interior"
        },
        {
            "name": "Chateau Amsterdam",
            "website": None,
            "location": "Gedempt Hamerkanaal, Amsterdam-Noord",
            "menu_items": "Urban winery, tasting menus",
            "price_range": "€€-€€€",
            "notes": "Winery + restaurant concept"
        },
    ],
    "Buzzing Places": [
        {
            "name": "Klaproos",
            "website": None,
            "location": "Amsterdam-Noord",
            "menu_items": "Pizza or modern bar scene?",
            "price_range": "€€",
            "notes": "Known for nightlife & events"
        },
        {
            "name": "Kikkie",
            "website": None,
            "location": "Amsterdam (info limited)",
            "menu_items": "Possibly modern bar or restaurant concept (info limited)",
            "price_range": "€€",
            "notes": "Trendy, new or local secret"
        },
        {
            "name": "Twee Prinsen",
            "website": None,
            "location": "Amsterdam (info limited)",
            "menu_items": "Bar/restaurant with local vibe (info limited)",
            "price_range": "€€",
            "notes": "Potential hidden gem"
        },
        {
            "name": "Murmur",
            "website": None,
            "location": "Amsterdam",
            "menu_items": "Lively bar or café, possible bites",
            "price_range": "€€",
            "notes": "Also appears for drinks"
        },
        {
            "name": "Skatecafe",
            "website": None,
            "location": "Gedempt Hamerkanaal 42, Amsterdam-Noord",
            "menu_items": "Skate ramp + café, casual food",
            "price_range": "€€",
            "notes": "Unique setting, often events"
        },
    ],
    "Always Good": [
        {
            "name": "Petit Caron",
            "website": "https://petitcaron.nl",
            "location": "Gerard Douplein, Amsterdam",
            "menu_items": "French bistro staples, wine",
            "price_range": "€€-€€€",
            "notes": "Repeated listing (Shared Dining, too)"
        },
        {
            "name": "Pastis",
            "website": None,
            "location": "Amsterdam (likely Jordaan)",
            "menu_items": "Classic French bistro dishes",
            "price_range": "€€",
            "notes": "Traditional brasserie style"
        },
        {
            "name": "Donna Sofia",
            "website": None,
            "location": "Amsterdam",
            "menu_items": "Italian trattoria fare",
            "price_range": "€€",
            "notes": "Neighborhood favorite for Italian"
        },
        {
            "name": "Cradam",
            "website": None,
            "location": "Amsterdam",
            "menu_items": "Info limited—possibly local bar/restaurant",
            "price_range": "€€",
            "notes": "Local casual spot"
        },
        {
            "name": "De Plantage",
            "website": None,
            "location": "Plantage Kerklaan, near Artis Zoo",
            "menu_items": "Refined brasserie, large glasshouse setting",
            "price_range": "€€-€€€",
            "notes": "Beautiful interior near Artis"
        },
        {
            "name": "Pekelharing",
            "website": None,
            "location": "Amsterdam (De Pijp area?)",
            "menu_items": "Dutch or Mediterranean-inspired fare",
            "price_range": "€€",
            "notes": "Neighborhood gem"
        },
        {
            "name": "Cantine de Caron",
            "website": None,
            "location": "Amsterdam",
            "menu_items": "French or Euro bistro, part of Caron family",
            "price_range": "€€-€€€",
            "notes": "Sister to Petit Caron"
        },
        {
            "name": "Alex + Pinard",
            "website": None,
            "location": "Amsterdam",
            "menu_items": "Wine-focused bistro, small plates",
            "price_range": "€€-€€€",
            "notes": "Good wine selection"
        },
        {
            "name": "Chez Nina",
            "website": None,
            "location": "Amsterdam",
            "menu_items": "Possibly French or modern fusion (info limited)",
            "price_range": "€€",
            "notes": "Word-of-mouth spot"
        },
        {
            "name": "Goudfazant",
            "website": None,
            "location": "Meeuwenlaan 98, Amsterdam-Noord",
            "menu_items": "French-Dutch cuisine, large industrial space",
            "price_range": "€€-€€€",
            "notes": "Iconic venue in Noord"
        },
        {
            "name": "Toscanini",
            "website": None,
            "location": "Lindengracht, Jordaan area",
            "menu_items": "Classic Italian dishes, fresh pasta",
            "price_range": "€€€",
            "notes": "Well-established Italian restaurant"
        },
    ],
    "Very Good but Expensive ($$)": [
        {
            "name": "4850",
            "website": None,
            "location": "Amsterdam",
            "menu_items": "Specialty coffee by day, tasting menu dinner",
            "price_range": "€€€",
            "notes": "Notable for coffee & wine"
        },
        {
            "name": "La Fiorita",
            "website": None,
            "location": "Amsterdam",
            "menu_items": "Upscale Italian cuisine",
            "price_range": "€€€",
            "notes": "Refined take on Italian dishes"
        },
        {
            "name": "Gouden Reaal",
            "website": None,
            "location": "Amsterdam (near Haarlemmerdijk?)",
            "menu_items": "Classic Dutch/French dishes",
            "price_range": "€€€",
            "notes": "Historic building, cozy vibe"
        },
        {
            "name": "Parlotte",
            "website": None,
            "location": "Amsterdam",
            "menu_items": "Wine bar + bistro plates",
            "price_range": "€€€",
            "notes": "Elegant, intimate setting"
        },
        {
            "name": "Scheepskameel",
            "website": None,
            "location": "Kattenburgerstraat, near Marineterrein",
            "menu_items": "Modern Dutch menu, extensive wine list",
            "price_range": "€€€",
            "notes": "Bright, minimal interior"
        },
        {
            "name": "Domenica",
            "website": None,
            "location": "Amsterdam",
            "menu_items": "Possibly modern Italian or Mediterranean",
            "price_range": "€€€",
            "notes": "Upscale vibe"
        },
        {
            "name": "Cafe de Klepel",
            "website": None,
            "location": "Amsterdam (Jordaan)",
            "menu_items": "Classic French cuisine, top-notch wines",
            "price_range": "€€€",
            "notes": "Intimate, reservations recommended"
        },
        {
            "name": "Entrepot",
            "website": None,
            "location": "Entrepotdok, Amsterdam",
            "menu_items": "Seasonal local produce, creative plates",
            "price_range": "€€€",
            "notes": "Industrial-chic, open kitchen"
        },
        {
            "name": "Gebroeders Hartering",
            "website": None,
            "location": "Peperstraat 10, Amsterdam",
            "menu_items": "Refined Dutch-French, tasting menus",
            "price_range": "€€€",
            "notes": "Known for communal tables, open kitchen"
        },
        {
            "name": "Watergang",
            "website": None,
            "location": "Watergang, just north of Amsterdam",
            "menu_items": "Farm-to-table or local produce-based menu (info limited)",
            "price_range": "€€€",
            "notes": "Countryside setting close to city"
        },
    ],
    "Really Good but Very Expensive ($$$)": [
        {
            "name": "Rijsel",
            "website": None,
            "location": "Marcusstraat 52, Amsterdam (East)",
            "menu_items": "French-Flemish cuisine, set menu",
            "price_range": "€€€-€€€€",
            "notes": "Beloved local gem, reservation needed"
        },
        {
            "name": "Choux",
            "website": None,
            "location": "De Ruijterkade 128, Amsterdam",
            "menu_items": "Modern creative cuisine, seasonal",
            "price_range": "€€€-€€€€",
            "notes": "Michelin Bib Gourmand; innovative menu"
        },
        {
            "name": "De Zoldering",
            "website": None,
            "location": "Amsterdam",
            "menu_items": "High-end dining (info limited)",
            "price_range": "€€€-€€€€",
            "notes": "Possibly Michelin-level"
        },
        {
            "name": "Cafe de Parel",
            "website": None,
            "location": "Amsterdam (Jordaan)",
            "menu_items": "Modern bistro tasting menu, upscale pub interior",
            "price_range": "€€€-€€€€",
            "notes": "Acclaimed hidden gem"
        },
        {
            "name": "Juwelier",
            "website": None,
            "location": "Amsterdam (9 Streets?)",
            "menu_items": "High-end bistro/fine dining",
            "price_range": "€€€-€€€€",
            "notes": "Part of the same owners as other top spots?"
        },
        {
            "name": "Wils",
            "website": None,
            "location": "Stadionplein, Amsterdam",
            "menu_items": "Michelin-starred concept (open-fire cooking)",
            "price_range": "€€€€",
            "notes": "1 Michelin star (as of recent years)"
        },
        {
            "name": "Breda",
            "website": None,
            "location": "Singel 210, Amsterdam",
            "menu_items": "Modern European tasting menus",
            "price_range": "€€€€",
            "notes": "Sister restaurant to Guts & Glory, etc."
        },
    ],
    "Other": [
        {
            "name": "Kyo",
            "website": None,
            "location": "Amsterdam",
            "menu_items": "Possibly Japanese concept (info limited)",
            "price_range": "€€-€€€",
            "notes": "Check local guides"
        },
        {
            "name": "Thai Thai Poppetje",
            "website": None,
            "location": "Amsterdam",
            "menu_items": "Thai street-food style",
            "price_range": "€€",
            "notes": "Popular takeout or casual spot"
        },
        {
            "name": "Kaagman & Kortekaas",
            "website": None,
            "location": "Amsterdam center",
            "menu_items": "Seasonal, creative Dutch-French",
            "price_range": "€€€-€€€€",
            "notes": "Chef-driven small menu"
        },
        {
            "name": "Public Space",
            "website": None,
            "location": "Overhoeksplein 2, Amsterdam-Noord",
            "menu_items": "Café & bar, pastries, brunch, coffee",
            "price_range": "€-€€",
            "notes": "Modern minimal interior"
        },
        {
            "name": "Barentsz",
            "website": None,
            "location": "Barentszstraat, Amsterdam",
            "menu_items": "Contemporary bistro or bar (info limited)",
            "price_range": "€€",
            "notes": "Neighborhood place"
        },
        {
            "name": "Vander Veen",
            "website": None,
            "location": "Amsterdam-Noord",
            "menu_items": "Possibly concept store + café (info limited)",
            "price_range": "€-€€",
            "notes": "Multi-purpose space"
        },
        {
            "name": "Stork",
            "website": None,
            "location": "Gedempt Hamerkanaal, Amsterdam-Noord",
            "menu_items": "Fish/seafood restaurant, large terrace",
            "price_range": "€€-€€€",
            "notes": "Riverside location, nice view"
        },
        {
            "name": "Pllek",
            "website": None,
            "location": "NDSM Wharf, Amsterdam-Noord",
            "menu_items": "International menu, beach vibe",
            "price_range": "€€",
            "notes": "Popular for drinks & sunsets"
        },
        {
            "name": "Noorderlicht Cafe",
            "website": None,
            "location": "NDSM Wharf, Amsterdam-Noord",
            "menu_items": "Organic, vegetarian-friendly, live music",
            "price_range": "€€",
            "notes": "Artistic/cultural hotspot"
        },
        {
            "name": "Skatecafe",
            "website": None,
            "location": "Amsterdam-Noord",
            "menu_items": "Skate ramp, casual eats, events",
            "price_range": "€€",
            "notes": "Unique, buzzing location"
        },
        {
            "name": "De Ceuvel",
            "website": None,
            "location": "Korte Papaverweg 4, Amsterdam-Noord",
            "menu_items": "Eco-friendly café, cultural space",
            "price_range": "€-€€",
            "notes": "Sustainably focused"
        },
    ],
    "For Drinks 🍺": [
        {
            "name": "Cafe Thijssen",
            "website": None,
            "location": "Brouwersgracht area, Amsterdam",
            "menu_items": "Dutch bar vibe, local beers, snacks",
            "price_range": "€-€€",
            "notes": "Classic brown café"
        },
        {
            "name": "Noorderlicht Cafe",
            "website": None,
            "location": "Amsterdam-Noord",
            "menu_items": "Organic beers, cocktails, live music",
            "price_range": "€€",
            "notes": "Listed under “Other” too"
        },
        {
            "name": "Fabus",
            "website": "https://www.fabusamsterdam.com",
            "location": "De Pijp, Amsterdam",
            "menu_items": "Wine bar, small bites",
            "price_range": "€€-€€€",
            "notes": "Cozy, curated wine list"
        },
        {
            "name": "Murmur",
            "website": None,
            "location": "Amsterdam",
            "menu_items": "Cocktails, music, possible small bites",
            "price_range": "€€",
            "notes": "Also in “Buzzing Places”"
        },
        {
            "name": "QV Winebar",
            "website": "https://maps.app.goo.gl/uwVxrFDG94Jj5uEJ9",
            "location": "Huidenstraat area, Amsterdam",
            "menu_items": "Extensive wine list, cheese & charcuterie",
            "price_range": "€€-€€€",
            "notes": "Small, intimate interior"
        },
        {
            "name": "Wijnbar Paulus",
            "website": "https://www.wijnbarpaulus.nl",
            "location": "De Pijp, Amsterdam",
            "menu_items": "Wines from small producers, simple nibbles",
            "price_range": "€€-€€€",
            "notes": "Neighborhood favorite"
        },
        {
            "name": "Pllek",
            "website": None,
            "location": "NDSM, Amsterdam-Noord",
            "menu_items": "Beers, cocktails, international bites",
            "price_range": "€€",
            "notes": "Also in “Other”"
        },
        {
            "name": "De Ceuvel",
            "website": None,
            "location": "Amsterdam-Noord",
            "menu_items": "Craft beers, snacks, eco-friendly venue",
            "price_range": "€€",
            "notes": "Also in “Other”"
        },
        {
            "name": "Cafe de Magere Brug",
            "website": None,
            "location": "Near Magere Brug (Skinny Bridge)",
            "menu_items": "Classic Amsterdam café, canal view",
            "price_range": "€€",
            "notes": "Historic location"
        },
        {
            "name": "Hendrix",
            "website": None,
            "location": "Amsterdam",
            "menu_items": "Gin & tonics, cocktails",
            "price_range": "€€",
            "notes": "Music-themed bar"
        },
        {
            "name": "Bar Bonnie",
            "website": None,
            "location": "Amstelveenseweg area, Amsterdam",
            "menu_items": "Cocktails, bites, modern interior",
            "price_range": "€€",
            "notes": "Popular local hangout"
        },
        {
            "name": "Bar Arie",
            "website": None,
            "location": "Amsterdam (possibly West)",
            "menu_items": "Neighborhood bar, craft beers, pub food",
            "price_range": "€€",
            "notes": "Casual hangout"
        },
        {
            "name": "Volt",
            "website": None,
            "location": "Ferdinand Bolstraat, Amsterdam",
            "menu_items": "Cocktail bar, modern vibe",
            "price_range": "€€",
            "notes": "Part of De Pijp nightlife"
        },
        {
            "name": "Gambrinus",
            "website": None,
            "location": "Amsterdam (De Pijp?)",
            "menu_items": "Traditional cafe, beers on tap",
            "price_range": "€-€€",
            "notes": "Local ‘brown café’ style"
        },
        {
            "name": "Cafe Kiebert",
            "website": None,
            "location": "Amsterdam (info limited)",
            "menu_items": "Possibly classic Dutch cafe, beers",
            "price_range": "€€",
            "notes": "Neighborhood spot"
        },
        {
            "name": "De Walvis",
            "website": None,
            "location": "Spaarndammerbuurt, Amsterdam",
            "menu_items": "Cozy bar, beers, snacks",
            "price_range": "€€",
            "notes": "Residential neighborhood vibe"
        },
        {
            "name": "Ceppi’s",
            "website": None,
            "location": "Amsterdam",
            "menu_items": "Wine bar or café (info limited)",
            "price_range": "€€-€€€",
            "notes": "Possibly Italian-inspired"
        },
    ],
    "For Coffee": [
        {
            "name": "Distrikt Coffee",
            "website": None,
            "location": "Amsterdam (several)",
            "menu_items": "Specialty coffee, pastries",
            "price_range": "€",
            "notes": "Chain known in some EU cities (Berlin, etc.)?"
        },
        {
            "name": "Black and Bloom",
            "website": None,
            "location": "Amsterdam (origin in Groningen??)",
            "menu_items": "Specialty coffee roasters",
            "price_range": "€",
            "notes": "Possibly a pop-up or new location in AMS"
        },
        {
            "name": "Caffenation",
            "website": None,
            "location": "Ferdinand Bolstraat, Amsterdam",
            "menu_items": "Belgian roaster, specialty coffee",
            "price_range": "€",
            "notes": "Cozy, small interior"
        },
        {
            "name": "Anne & Max",
            "website": None,
            "location": "Multiple locations in Amsterdam",
            "menu_items": "Coffee, breakfast, lunch",
            "price_range": "€-€€",
            "notes": "Popular local chain"
        },
        {
            "name": "Uncommon",
            "website": None,
            "location": "Amsterdam",
            "menu_items": "Specialty coffee, unique origins",
            "price_range": "€",
            "notes": "Minimalist coffee bar"
        },
        {
            "name": "Bocca",
            "website": None,
            "location": "Kerkstraat 96, Amsterdam",
            "menu_items": "Specialty roaster, pour-over, espresso",
            "price_range": "€",
            "notes": "Pioneer in Amsterdam coffee scene"
        },
        {
            "name": "Badeta",
            "website": None,
            "location": "Amsterdam (info limited)",
            "menu_items": "Possibly coffee + small bites",
            "price_range": "€",
            "notes": "Undersung local spot"
        },
        {
            "name": "Toki",
            "website": None,
            "location": "Jordaan area, Amsterdam",
            "menu_items": "Specialty coffee, pastries",
            "price_range": "€",
            "notes": "Popular among coffee aficionados"
        },
        {
            "name": "Yusu",
            "website": None,
            "location": "Amsterdam (info limited)",
            "menu_items": "Espresso, cappuccino, maybe brunch?",
            "price_range": "€",
            "notes": "Possibly a small café"
        },
    ],
}

# ---------- CATEGORY ORDER & (OPTIONAL) ICONS ----------
# List them in the order you want them displayed
category_list = list(restaurants_data.keys())

# Optional icons (shorter or longer than category_list is okay; we handle it safely)
icons = [
    "https://em-content.zobj.net/thumbs/240/apple/354/taco_1f32e.png",      # Mexican
    "https://em-content.zobj.net/thumbs/240/apple/354/pizza_1f355.png",     # Pizza
    "https://em-content.zobj.net/thumbs/240/apple/354/fork-and-knife_1f374.png",  # Shared Dining
    "https://em-content.zobj.net/thumbs/240/apple/354/collision_1f4a5.png",       # Buzzing Places
    "https://em-content.zobj.net/thumbs/240/apple/354/star_2b50.png",             # Always Good
    "https://em-content.zobj.net/thumbs/240/apple/354/heavy-dollar-sign_1f4b2.png",  # Very Good but Expensive
    "https://em-content.zobj.net/thumbs/240/apple/354/banknote-with-dollar-sign_1f4b5.png", # Really Good but Very Expensive
    "https://em-content.zobj.net/thumbs/240/apple/354/gear_2699-fe0f.png",        # Other
    "https://em-content.zobj.net/thumbs/240/apple/354/beer-mug_1f37a.png",        # For Drinks
    "https://em-content.zobj.net/thumbs/240/apple/354/hot-beverage_2615.png",     # For Coffee
]

selected_category = None

# Number of columns per row (adjust as you like)
cols_per_row = 3

# ---------- RENDER CATEGORY BUTTONS IN ROWS ----------
for i, category in enumerate(category_list):
    # Start a new row every 'cols_per_row' categories
    if i % cols_per_row == 0:
        columns = st.columns(cols_per_row)

    col = columns[i % cols_per_row]

    # Show an icon if available
    if i < len(icons):
        col.image(icons[i], width=60)
    else:
        # fallback if no icon
        col.write("📝")

    # Button for the category
    if col.button(category):
        selected_category = category

# ---------- IF USER SELECTED A CATEGORY, SHOW THE RESTAURANTS ----------
if selected_category:
    st.subheader(f"**{selected_category}**")
    for r in restaurants_data[selected_category]:
        st.markdown(f"### {r['name']}")
        # If website is present, make it a clickable link
        if r["website"]:
            st.markdown(f"- **Website**: [{r['website']}]({r['website']})")
        else:
            st.markdown("- **Website**: *No official link*")
        st.markdown(f"- **Location**: {r['location']}")
        st.markdown(f"- **Key Menu Items**: {r['menu_items']}")
        st.markdown(f"- **Price Range**: {r['price_range']}")
        st.markdown(f"- **Notes**: {r['notes']}")
        st.markdown("---")
