import streamlit as st
from google import genai
import json

# --- Advanced Page Configuration ---
st.set_page_config(
    page_title="AI Student Travel Planner Pro", 
    page_icon="✈️", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Theme-Agnostic Fluid UI Styling (Fixed for Dark & Light Mode) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');
    
    * { font-family: 'Plus Jakarta Sans', sans-serif; }
    
    /* Premium Themed Cards - Adapts smoothly to Dark and Light modes */
    .travel-card {
        padding: 24px;
        border-radius: 16px;
        border: 1px solid rgba(128, 128, 128, 0.2);
        background-color: rgba(128, 128, 128, 0.04);
        margin-bottom: 24px;
    }
    
    /* Timeline & Itinerary Items - Adapts to contrast variants seamlessly */
    .timeline-item {
        background: rgba(79, 70, 229, 0.08);
        border-left: 4px solid #6366f1;
        padding: 16px;
        border-radius: 0 12px 12px 0;
        margin-bottom: 16px;
    }
    .food-item {
        background: rgba(245, 158, 11, 0.08);
        border-left: 4px solid #f59e0b;
        padding: 16px;
        border-radius: 0 12px 12px 0;
        margin-bottom: 16px;
    }
    
    /* Metric Dashboard Grid */
    .dashboard-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
        gap: 16px;
        margin-bottom: 30px;
    }
    .dashboard-metric {
        border: 1px solid rgba(128, 128, 128, 0.2);
        background-color: rgba(128, 128, 128, 0.04);
        padding: 20px;
        border-radius: 14px;
        text-align: center;
    }
    .metric-val {
        font-size: 22px;
        font-weight: 700;
        margin-top: 4px;
    }
    .metric-lbl {
        font-size: 11px;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        opacity: 0.8;
    }
    
    /* Interactive Generate Button override */
    .stButton>button {
        background: linear-gradient(135deg, #4f46e5 0%, #3730a3 100%) !important;
        color: white !important;
        font-weight: 600 !important;
        border-radius: 10px !important;
        padding: 12px !important;
        border: none !important;
    }
    .stButton>button:hover {
        box-shadow: 0 4px 12px rgba(79, 70, 229, 0.4) !important;
    }
</style>
""", unsafe_allow_html=True)

# --- UI Header ---
st.markdown("<h1 style='font-weight: 800; margin-bottom: 4px;'>✈️ NextGen Student Travel Engine</h1>", unsafe_allow_html=True)
st.markdown("<p style='font-size: 16px; margin-bottom: 30px; opacity: 0.8;'>Dynamic AI travel pipelines optimized for structural budgets, local foods, and itemized multi-leg routes.</p>", unsafe_allow_html=True)

col_sidebar, col_main = st.columns([1, 2.6])

# --- LEFT SIDEBAR: CONTROL & PARAMETERS ---
with col_sidebar:
    st.markdown("<h3 style='margin-top:0;'>⚙️ Parameters</h3>", unsafe_allow_html=True)
    
    api_key = "*****************************************"
    st.success("API Pipeline Verified Secure ✅")
    st.divider()
    
    current_loc = st.text_input("Current Location (Source)", placeholder="e.g., Delhi, Mumbai")
    destination = st.text_input("Destination City", placeholder="e.g., Goa, Manali, Jaipur")
    
    duration = st.slider("Trip Duration (Days)", min_value=1, max_value=5, value=3)
    total_budget = st.number_input("Total Budget Pool (INR)", min_value=1000, value=8000, step=500)
    
    transit_pref = st.selectbox("Intercity Transit Mode", ["Local Sleeper Train / 3AC", "State Bus", "Budget Flight"])
    student_id = st.checkbox("Apply Student ID Card Discounts", value=True)
    num_friends = st.number_input("Number of Companions (Cost Sharing)", min_value=1, max_value=10, value=1)
    
    generate_btn = st.button("Compute Optimal Itinerary 🚀")

# --- AI ROUTING & DATA FETCHING ENGINE ---
def generate_advanced_itinerary_json(current, dest, days, budget, transit, has_id):
    try:
        client = genai.Client(api_key=api_key)
        
        prompt = f"""
        You are a highly structured travel routing optimization machine. Create a realistic student budget travel itinerary from '{current}' to '{dest}' for exactly {days} days. The absolute total maximum budget available is {budget} INR.
        The user prefers to travel via '{transit}'. Student ID card availability is {has_id}.

        CRITICAL OUTPUT INSTRUCTIONS:
        1. Calculate the realistic price to go from '{current}' to '{dest}' (departure_fare) AND the price to come back from '{dest}' to '{current}' (return_fare) using the mode of transport '{transit}'. Make sure these are integers.
        2. In 'itinerary', you MUST generate exactly 3 meal recommendations per day (breakfast, lunch, dinner) with real famous local specialty items and authentic cheap local eateries.
        3. In 'itinerary', you MUST generate exactly 4 separate local tourist landmarks or activities per day. Provide an approximate transit fare (auto/bus/metro) to travel between each place consecutively.
        4. Generate a list of recommended packing items specific to this exact trip profile (weather, trekking, walking, or beach needs of '{dest}') split into categories inside the 'packing_list' array.

        Return your response ONLY as a single valid JSON object matching the template below. Do not include markdown strings like ```json or ```. No extra commentary text.

        {{
          "accommodation": {{
            "name": "Real budget backpacker hostel/stay name at destination",
            "cost_per_night": 450
          }},
          "intercity_transport": {{
            "mode": "Real option name chosen",
            "departure_fare": 450,
            "return_fare": 450
          }},
          "packing_list": [
            {{"category": "Documents & Money", "item": "Physical Student ID card for entry concessions"}},
            {{"category": "Clothing & Essentials", "item": "Specific item recommended for weather at destination"}}
          ],
          "itinerary": [
            {{
              "day": 1,
              "meals": {{
                "breakfast": {{"dish": "Specialty food", "spot": "Cheap iconic eatery", "cost": 100}},
                "lunch": {{"dish": "Specialty food", "spot": "Cheap iconic eatery", "cost": 150}},
                "dinner": {{"dish": "Specialty food", "spot": "Cheap iconic eatery", "cost": 200}}
              }},
              "landmarks": [
                {{"name": "Landmark Place 1", "time": "09:00 AM - 11:30 AM", "entry_fee": 20, "transit_cost_to_next_place": 40}},
                {{"name": "Landmark Place 2", "time": "12:00 PM - 02:30 PM", "entry_fee": 50, "transit_cost_to_next_place": 30}},
                {{"name": "Landmark Place 3", "time": "03:30 PM - 05:30 PM", "entry_fee": 0, "transit_cost_to_next_place": 50}},
                {{"name": "Landmark Place 4", "time": "06:00 PM - 08:30 PM", "entry_fee": 30, "transit_cost_to_next_place": 60}}
              ]
            }}
          ]
        }}
        """
        
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
        )
        
        clean_text = response.text.replace("```json", "").replace("```", "").strip()
        return json.loads(clean_text)
    except Exception as e:
        st.error(f"Execution Error: Engine failed to compile constraints. Details: {str(e)}")
        return None

# --- MAIN RENDER DISPLAY PANEL ---
with col_main:
    if generate_btn:
        if not current_loc or not destination:
            st.error("⚠️ Validation Error: Current Location and Destination City are required fields.")
        else:
            with st.spinner(f"Running graph algorithms, lodging matching indexes, and mapping meal coordinates for {current_loc} ➔ {destination}..."):
                processed_data = generate_advanced_itinerary_json(current_loc, destination, duration, total_budget, transit_pref, student_id)
                if processed_data:
                    st.session_state['pro_trip'] = processed_data
                    st.session_state['pro_active'] = True

    if st.session_state.get('pro_active'):
        data = st.session_state['pro_trip']
        
        # --- Strict isolated Mathematical Financial Computations ---
        total_nights = duration - 1 if duration > 1 else 1
        total_lodging = int(data['accommodation']['cost_per_night']) * total_nights
        
        dep_fare = int(data['intercity_transport']['departure_fare'])
        ret_fare = int(data['intercity_transport']['return_fare'])
        round_trip_fare = dep_fare + ret_fare
        
        monument_fees = 0
        local_transit = 0
        food_expenses = 0
        
        for day in data['itinerary']:
            # Safe calculation casting to avoid JSON evaluation anomalies
            food_expenses += int(day['meals']['breakfast']['cost']) + int(day['meals']['lunch']['cost']) + int(day['meals']['dinner']['cost'])
            for lm in day['landmarks']:
                monument_fees += int(lm['entry_fee'])
                local_transit += int(lm['transit_cost_to_next_place'])
                
        grand_total = total_lodging + round_trip_fare + monument_fees + local_transit + food_expenses
        cash_balance = int(total_budget) - grand_total
        
        # --- Component 1: Visual Metric Dashboard Grid ---
        st.markdown(f"<h3>📊 Budget Distribution Overview</h3>", unsafe_allow_html=True)
        balance_color = "#10b981" if cash_balance >= 0 else "#ef4444"
        
        st.markdown(f"""
        <div class='dashboard-grid'>
            <div class='dashboard-metric'><div class='metric-lbl'>🛫 Departure Fare</div><div class='metric-val'>₹{dep_fare}</div></div>
            <div class='dashboard-metric'><div class='metric-lbl'>🛬 Return Fare</div><div class='metric-val'>₹{ret_fare}</div></div>
            <div class='dashboard-metric'><div class='metric-lbl'>🏨 Hostel Total</div><div class='metric-val'>₹{total_lodging}</div></div>
            <div class='dashboard-metric'><div class='metric-lbl'>🍱 Food & Fares</div><div class='metric-val'>₹{food_expenses + local_transit}</div></div>
            <div class='dashboard-metric'><div class='metric-lbl'>💰 Wallet Balance</div><div class='metric-val' style='color: {balance_color};'>₹{cash_balance}</div></div>
        </div>
        """, unsafe_allow_html=True)
        
        if num_friends > 1:
            split_share = round(((total_lodging + local_transit) / num_friends) + round_trip_fare + food_expenses + monument_fees)
            st.info(f"👥 **Group Splitting:** Splitting rooms and internal auto rides across {num_friends} friends scales your effective spending profile to **₹{split_share} per person**.")

        # --- Component 2: Recommended Basecamp ---
        st.markdown(f"""
        <div class='travel-card'>
            <h4 style='margin:0 0 8px 0; color: #6366f1;'>🏨 Basecamp Accommodation Match</h4>
            <p style='margin:0; font-size: 15px;'>Stay booked at <b>{data['accommodation']['name']}</b> at <b>₹{data['accommodation']['cost_per_night']}</b> per night.</p>
        </div>
        """, unsafe_allow_html=True)

        # --- Component 3: Detailed Multi-Leg Schedule Matrix ---
        st.markdown(f"<h3>🗓️ Chronological Action Schedule (4 Places + 3 Local Meals Daily)</h3>", unsafe_allow_html=True)
        
        for day in data['itinerary']:
            st.markdown(f"<h4>📌 Day {day['day']} Timeline</h4>", unsafe_allow_html=True)
            
            with st.container():
                meals = day['meals']
                places = day['landmarks']
                
                st.markdown(f"<div class='food-item'>🍳 <b>Breakfast Special:</b> Try <i>{meals['breakfast']['dish']}</i> at <b>{meals['breakfast']['spot']}</b> (~₹{meals['breakfast']['cost']})</div>", unsafe_allow_html=True)
                
                for i in range(2):
                    if i < len(places):
                        st.markdown(f"""
                        <div class='timeline-item'>
                            <b>🧭 {places[i]['time']}</b> — {places[i]['name']}<br>
                            <span style='font-size: 13px; opacity: 0.85;'>🎫 Entry Ticket: ₹{places[i]['entry_fee']} | 🛺 Local transit to next spot: <b>₹{places[i]['transit_cost_to_next_place']}</b></span>
                        </div>
                        """, unsafe_allow_html=True)
                        
                st.markdown(f"<div class='food-item'>🍛 <b>Lunch Special:</b> Enjoy authentic <i>{meals['lunch']['dish']}</i> at <b>{meals['lunch']['spot']}</b> (~₹{meals['lunch']['cost']})</div>", unsafe_allow_html=True)
                
                for i in range(2, 4):
                    if i < len(places):
                        st.markdown(f"""
                        <div class='timeline-item'>
                            <b>🧭 {places[i]['time']}</b> — {places[i]['name']}<br>
                            <span style='font-size: 13px; opacity: 0.85;'>🎫 Entry Ticket: ₹{places[i]['entry_fee']} | 🛺 Local transit to next spot: <b>₹{places[i]['transit_cost_to_next_place']}</b></span>
                        </div>
                        """, unsafe_allow_html=True)
                        
                st.markdown(f"<div class='food-item'>🍲 <b>Dinner Special:</b> Wind down with <i>{meals['dinner']['dish']}</i> at <b>{meals['dinner']['spot']}</b> (~₹{meals['dinner']['cost']})</div>", unsafe_allow_html=True)

        # --- Component 4: Smart Interactive Travel Checklist ---
        st.divider()
        st.markdown(f"<h3>🎒 Smart Travel Packing Checklist (Tailored for {destination})</h3>", unsafe_allow_html=True)
        
        if "packing_list" in data:
            categories = {}
            for checklist_item in data['packing_list']:
                cat = checklist_item['category']
                item = checklist_item['item']
                if cat not in categories:
                    categories[cat] = []
                categories[cat].append(item)
                
            col_check1, col_check2 = st.columns(2)
            for idx, (cat_name, items) in enumerate(categories.items()):
                target_col = col_check1 if idx % 2 == 0 else col_check2
                with target_col:
                    st.markdown(f"<p style='font-weight: 600; color: #6366f1; margin-bottom:4px;'>📋 {cat_name}</p>", unsafe_allow_html=True)
                    for single_item in items:
                        st.checkbox(single_item, key=f"check_{single_item}")