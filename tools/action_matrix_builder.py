# =========================================
# ACTION MATRIX BUILDER
# =========================================

def build_action_matrix(actions):

    html = """

    <table class='comparison-table'>

        <tr>

            <th>Priority</th>

            <th>Recommended Action</th>

            <th>Impact</th>

            <th>Effort</th>

            <th>Timeline</th>

        </tr>

    """

    for action in actions:

        priority = action.get(
            "priority",
            "Medium"
        )

        recommendation = action.get(
            "action",
            "No recommendation provided."
        )

        # =================================
        # AUTO-GENERATE BUSINESS VALUES
        # =================================

        if priority == "Critical":

            impact = "Very High"
            effort = "High"
            timeline = "Immediate"

        elif priority == "High":

            impact = "High"
            effort = "Medium"
            timeline = "1-2 Weeks"

        elif priority == "Medium":

            impact = "Moderate"
            effort = "Medium"
            timeline = "2-4 Weeks"

        else:

            impact = "Low"
            effort = "Low"
            timeline = "Long Term"

        html += f"""

        <tr>

            <td>{priority}</td>

            <td>{recommendation}</td>

            <td>{impact}</td>

            <td>{effort}</td>

            <td>{timeline}</td>

        </tr>

        """

    html += "</table>"

    return html