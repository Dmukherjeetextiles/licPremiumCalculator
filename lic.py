import streamlit as st

# Dictionary to store plan-specific details 
plan_data = {
    "Bima Jyoti": {
        "min_sum_assured": 100000,
        "min_age": 0,
        "max_age": 60,
        "min_term": 15,
        "max_term": 20,
        "premium_factor": 0.078  # Replace with actual calculation logic
    },
    "Jeevan Lakshya": {
        "min_sum_assured": 100000,
        "min_age": 18,
        "max_age": 50,
        "min_term": 13,
        "max_term": 25,
        "premium_factor": 0.043  # Replace with actual calculation logic
    },
    "Jeevan Umang": {
        "min_sum_assured": 200000,
        "min_age": 90,  # Days for age less than 1 year
        "max_age": 55,
        "min_term": 15,  # Assuming minimum term is 15 years
        "max_term": 35,
        "premium_factor": 0.072  # Replace with actual calculation logic 
    },
    # Add data for more plans here...
}

def calculate_premium(plan, sum_assured, age, term):
  """Calculates premium based on plan and input values."""
  plan_info = plan_data.get(plan)
  if not plan_info:
    return 0  # Return 0 for unrecognized plans

  # Placeholder: Replace with actual calculation logic for each plan
  premium = plan_info["premium_factor"] * sum_assured
  return premium

def get_plan_input_options(plan):
  """Returns min/max values for sum assured, age, and term based on plan."""
  plan_info = plan_data.get(plan)
  if not plan_info:
    return {}, {}, {}
  return {
      "min_value": plan_info["min_sum_assured"],
      "value": plan_info["min_sum_assured"] * 10
  }, {
      "min_value": plan_info["min_age"], 
      "max_value": plan_info["max_age"], 
      "value": 30
  }, {
      "min_value": plan_info["min_term"], 
      "max_value": plan_info["max_term"],
      "value": 20
  }

st.title("LIC Premium Calculator")

selected_plan = st.selectbox("Choose a plan:", list(plan_data.keys()))

sum_assured_options, age_options, term_options = get_plan_input_options(selected_plan)

sum_assured = st.number_input("Enter Sum Assured (₹):", **sum_assured_options)
age = st.number_input("Enter Age (years):", **age_options)
term = st.number_input("Enter Policy Term (years):", **term_options)

if st.button("Calculate Premium"):
  premium = calculate_premium(selected_plan, sum_assured, age, term)
  st.write(f"Estimated Premium for {selected_plan}: ₹{premium:.2f}")

st.write("**Disclaimer:** This is an approximate premium calculation. " 
         "Please contact LIC for exact premium amounts.")