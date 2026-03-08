import streamlit as st


class View:
    def __init__(self):
        self.alert_origin = None
        self.partner_impact = None
        self.assess_alert_all_checked = False

    def header_detection(self):
        st.header("1. Detection Stage.")

    def subheader_discover_alert(self):
        st.subheader("1.1 Discover Alert")

    def step_determine_alert_origin(self):
        alert_origin_options = (
            "Existing Zendesk",
            "Splunk/Rootly paged",
            "Internal slack tags",
            "Prometheus alerts",
            "Incident screening in #wp-incident-chatter",
        )
        st.subheader("1.1.1 Determine Alert Origin")
        self.alert_origin = st.selectbox(
            "alert origin:", alert_origin_options, label_visibility="hidden"
        )

        st.info(f"Origin of alert: {self.alert_origin}")

    def subheader_assess_alert(self):
        st.subheader("1.2 Assess Alert")

    def step_investigate_alert(self):
        determine_non_live_incident_parter_impact_steps = (
            "Reproduce the issue",
            "Investigate logs",
        )
        determine_live_incident_parter_impact_steps = (
            "Assess impacted component used by partner?",
            "Clarify impacted transferIds belong to partner?",
        )
        checked_options = list()

        st.subheader("1.2.1 Assess")

        if "incident" in self.alert_origin:
            for i, step in enumerate(determine_live_incident_parter_impact_steps):
                is_checked = st.checkbox(step, key=f"step_{i}")
                if step == "Investigate logs":
                    st.text_input("Logs:", "")
                checked_options.append(is_checked)
        else:
            is_ack_checked = st.checkbox(
                "Acknowledge the alert/issue/tag", key=f"step_acknowledge"
            )
            checked_options.append(is_ack_checked)

            for i, step in enumerate(determine_non_live_incident_parter_impact_steps):
                is_checked = st.checkbox(step, key=f"step_{i}")
                if step == "Investigate logs":
                    st.text_area(
                        "Logs", placeholder="Enter logs here", label_visibility="hidden"
                    )
                checked_options.append(is_checked)

        if not False in checked_options:
            self.assess_alert_all_checked = True

    def step_determine_partner_impact(self):
        partner_impact_options = ("", "Yes", "No", "Unsure")

        st.subheader("1.2.2 Determine partner impact")

        if self.assess_alert_all_checked:
            self.partner_impact = st.selectbox(
                "partner impact:", partner_impact_options, label_visibility="hidden"
            )

    def subheader_triage_alert(self):
        st.subheader("1.3 Triage Alert")

    def step_triage(self):
        st.subheader("1.3.1 Triage")

        if self.partner_impact:
            if self.partner_impact == "No":
                st.balloons()
                st.success(
                    "You've reach the end: No partner impact continue BAU", icon="✅"
                )

            if self.partner_impact == "Yes":
                st.error(
                    "Please assess impact severity and create a live incident",
                    icon="🔥",
                )

            if "incident" in self.alert_origin and "Unsure" in self.partner_impact:
                st.warning("Clarify partner impact with incident manager", icon="⚠️")

            if not "incident" in self.alert_origin and "Unsure" in self.partner_impact:
                st.warning(
                    "Reach out to partner technical contact to clarify impact", icon="⚠️"
                )
