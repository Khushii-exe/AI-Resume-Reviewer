import streamlit as st
def load_css():
    st.markdown(
        """
<style>

.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
}

div[data-testid="metric-container"]{

    border:1px solid #d9d9d9;

    border-radius:12px;

    padding:15px;

    text-align:center;

}

.stProgress > div > div > div > div{

    background:#4CAF50;

}

</style>
""",
        unsafe_allow_html=True
    )