import joblib
import pandas as pd
import streamlit as st

# ---------------------------
# CONFIG
# ---------------------------
st.set_page_config(
    page_title="Credit Risk Decision System",
    page_icon="💳",
    layout="centered"
)

MODEL_PATH = "credit_risk_pipeline.joblib"  # ✅ fixed: this file exists in your folder
THRESHOLD = 0.37

# ---------------------------
# LOAD MODEL
# ---------------------------
@st.cache_resource
def load_model(path: str):
    return joblib.load(path)

clf = load_model(MODEL_PATH)

# ---------------------------
# UI
# ---------------------------
st.markdown("## 🏦 Elif Bank")
st.markdown("### Credit Risk Decision System")
st.divider()
st.caption("Please fill in the applicant information to receive a credit decision.")

with st.form("credit_form"):
    st.subheader("👤 Applicant Information")

    name = st.text_input("Full Name")

    person_age = st.number_input("Age", min_value=18, max_value=100, value=30)
    person_income = st.number_input("Annual Income", min_value=0, value=50000, step=1000)

    person_home_ownership = st.selectbox(
        "Home Ownership",
        ["RENT", "OWN", "MORTGAGE", "OTHER"]
    )

    person_emp_length = st.number_input(
        "Employment Length (years)",
        min_value=0.0, max_value=60.0, value=5.0, step=0.5
    )

    loan_intent = st.selectbox(
        "Loan Purpose",
        ["PERSONAL", "EDUCATION", "MEDICAL", "VENTURE", "HOMEIMPROVEMENT", "DEBTCONSOLIDATION"]
    )

    loan_amnt = st.number_input("Loan Amount", min_value=0, value=10000, step=500)

    loan_int_rate = st.number_input(
        "Interest Rate (%)",
        min_value=0.0, max_value=50.0, value=13.5, step=0.1
    )

    # ✅ We calculate this automatically
    st.info("✅ Loan / Income Ratio is calculated automatically (loan_amount / annual_income).")

    cb_person_default_on_file = st.selectbox(
        "Previous Default?",
        ["N", "Y"]
    )

    cb_person_cred_hist_length = st.number_input(
        "Credit History Length (years)",
        min_value=0, max_value=50, value=6
    )

    submitted = st.form_submit_button("Evaluate Credit")

# ---------------------------
# PREDICTION
# ---------------------------
if submitted:
    if name.strip() == "":
        st.error("Please enter your full name.")
    elif person_income <= 0:
        st.error("Annual Income must be greater than 0 to calculate Loan / Income Ratio.")
    else:
        # ✅ Auto-calculated feature
        loan_percent_income = loan_amnt / person_income

        applicant = {
            "person_age": person_age,
            "person_income": person_income,
            "person_home_ownership": person_home_ownership,
            "person_emp_length": person_emp_length,
            "loan_intent": loan_intent,
            "loan_amnt": loan_amnt,
            "loan_grade": "C",
            "loan_int_rate": loan_int_rate,
            "loan_percent_income": loan_percent_income,  # ✅ computed by us
            "cb_person_default_on_file": cb_person_default_on_file,
            "cb_person_cred_hist_length": cb_person_cred_hist_length
        }

        X_new = pd.DataFrame([applicant])
        p_default = clf.predict_proba(X_new)[0, 1]

        st.subheader("📊 Credit Evaluation Result")

        st.write(f"**Applicant:** {name}")
        st.write(f"**Loan / Income Ratio (auto):** `{loan_percent_income:.3f}`")
        st.write(f"**Estimated Default Probability:** `{p_default:.2%}`")
        st.write(f"**Decision Threshold:** `{THRESHOLD:.2%}`")

        if p_default >= THRESHOLD:
            st.error(
                f"❌ **We’re sorry, {name}.**\n\n"
                "Based on our current evaluation, you are **not eligible for credit at this time**. "
                "You may consider reapplying in the future as your financial profile improves."
            )
        else:
            st.success(
                f"✅ **Congratulations, {name}!**\n\n"
                "Based on our assessment, **your credit application is approved**. "
                "Our team may contact you for further steps."
            )
