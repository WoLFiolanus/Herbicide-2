# Επαναδημιουργία του αρχείου Python με τον ενημερωμένο κώδικα

file_path = "/mnt/data/herbicide_ranking_app.py"

code = """\
import pandas as pd
import streamlit as st

# Φόρτωση δεδομένων από Excel
@st.cache_data
def load_data():
    path_vineyard = "herbicides_VINE.xlsx"
    path_peach = "ΦΥΣΙΚΟΧΗΜΙΚΑ_ΖΙΖΑΝΙΟΚΤΌΝΑ_ΡΟΔΑΚΙΝΑ.xlsx"
    df_vineyard = pd.read_excel(path_vineyard)
    df_peach = pd.read_excel(path_peach)
    return df_vineyard, df_peach

df_vineyard, df_peach = load_data()

# Συνδυασμός δεδομένων
all_herbicides = pd.concat([df_vineyard, df_peach])
herbicide_names = all_herbicides["Δραστική Ουσία1"].dropna().unique()

# Streamlit App
st.title("Herbicide Ranking System")
st.write("Επιλέξτε καλλιέργεια και ζιζανιοκτόνο για να δείτε τις λεπτομέρειες.")

# Επιλογή καλλιέργειας
crop = st.selectbox("Επιλέξτε καλλιέργεια:", ["Αμπέλι", "Ροδακινιά"])

# Επιλογή ζιζανιοκτόνου
selected_herbicide = st.selectbox("Επιλέξτε ζιζανιοκτόνο:", herbicide_names)

# Input για φυσική θέση καλλιέργειας (επικινδυνότητα μόλυνσης υδάτων)
water_proximity = st.slider("Εγγύτητα σε όγκους υδάτων (0: Μακριά, 1: Πολύ κοντά)", 0.0, 1.0, 0.5)

# Φιλτράρισμα δεδομένων για το επιλεγμένο ζιζανιοκτόνο
herbicide_data = all_herbicides[all_herbicides["Δραστική Ουσία1"] == selected_herbicide]

if not herbicide_data.empty:
    st.write(f"### Πληροφορίες για το {selected_herbicide}")
    st.dataframe(herbicide_data)
    
    # Υπολογισμός τελικού Herbicide Score
    pollution_index = herbicide_data.get("Pollution Index", 0).values[0]
    resistance_index = herbicide_data.get("Resistance Index", 0).values[0]
    herbicide_score = pollution_index + resistance_index + water_proximity
    
    st.write(f"### Herbicide Score: {herbicide_score:.2f}")
else:
    st.write("Δεν βρέθηκαν δεδομένα για το επιλεγμένο ζιζανιοκτόνο.")
"""



file_path
