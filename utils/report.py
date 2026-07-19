import streamlit as st


def display_list(items):
    if not items:
        st.write("No data available.")
        return

    for item in items:
        st.markdown(f"✅ {item}")

def display_report(result):
    score = result.get("ats_score", 0)
    st.markdown("# 📊 ATS Score")
    st.progress(score / 100)

    if score >= 80:
        st.success("Excellent Resume")
    elif score >= 60:
        st.warning("Good Resume")
    else:
        st.error("Needs Improvement")
    st.metric("Overall Score", f"{score}%")
    st.divider()
    st.header("📝 Summary")
    st.write(result.get("summary", ""))
    tab1, tab2 = st.tabs(["Strengths", "Suggestions"])
    with tab1:
        st.subheader("💪 Strengths")
        display_list(result.get("strengths", []))
        st.subheader("🚀 Missing Skills")
        display_list(result.get("missing_skills", []))
    with tab2:
        st.subheader("⚠ Weaknesses")
        display_list(result.get("weaknesses", []))
        st.subheader("💡 Improvement Tips")
        display_list(result.get("improvement_tips", []))

def display_jd_report(result):
    score = result.get("match_score", 0)
    st.header("🎯 Job Description Match")
    st.progress(score / 100)
    st.metric(
        "Match Score",
        f"{score}%"
    )
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("✅ Matched Skills")
        matched = result.get("matched_skills", [])
        if matched:
            for skill in matched:
                st.success(skill)
        else:
            st.write("No matched skills found.")
    with col2:
        st.subheader("❌ Missing Skills")
        missing = result.get("missing_skills", [])
        if missing:
            for skill in missing:
                st.error(skill)
        else:
            st.write("No missing skills.")
    st.subheader("Recruiter's Feedback")
    st.info(result.get("feedback", ""))
    st.subheader("Recommendation")
    st.write(result.get("recommendation", ""))