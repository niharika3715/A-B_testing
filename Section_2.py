import streamlit as st
from scipy import stats

def ab_test(control_visitors, control_conversions, treatment_visitors, treatment_conversions, confidence_level):

    # Calculate conversion rates for control and treatment groups
    control_rate = control_conversions / control_visitors
    treatment_rate = treatment_conversions / treatment_visitors
    
    # Calculate pooled standard error
    p_pool = (control_conversions + treatment_conversions) / (control_visitors + treatment_visitors)
    se_pooled = (p_pool * (1 - p_pool) * ((1 / control_visitors) + (1 / treatment_visitors))) ** 0.5
    
    # Calculate z-score
    z_score = (treatment_rate - control_rate) / se_pooled
    
    # Determine critical z-value based on confidence level
    if confidence_level == 90:
        critical_z = 1.645
    elif confidence_level == 95:
        critical_z = 1.96
    elif confidence_level == 99:
        critical_z = 2.576
    else:
        raise ValueError("Invalid confidence level. Choose from 90, 95, or 99.")
    
    # Compare z-score with critical z-value and make the decision
    if z_score > critical_z:
        return "Experiment Group is Better"
    elif z_score < -critical_z:
        return "Control Group is Better"
    else:
        return "Indeterminate"
        

# Create Streamlit app
def main():
    st.title('A/B Test Hypothesis Testing App')

    # User inputs
    control_visitors = st.number_input('Enter Control Group Visitors:', min_value=1)
    control_conversions = st.number_input('Enter Control Group Conversions:', min_value=0)
    treatment_visitors = st.number_input('Enter Treatment Group Visitors:', min_value=1)
    treatment_conversions = st.number_input('Enter Treatment Group Conversions:', min_value=0)
    confidence_level = st.selectbox('Select Confidence Level:', [90, 95, 99])

    # Perform A/B test
    if st.button('Perform A/B Test'):
        result = ab_test(control_visitors, control_conversions, treatment_visitors, treatment_conversions, confidence_level)
        st.write(f'Result: {result}')

if __name__ == '__main__':
    main()
    
