def table_gas(gas):
    if gas == "co": return {
    "range": {
        "low": 0,
        "medium": 10_000,
        "high": 30_000
    }, 
    "table": """
    <table border="1">
        <tr>
            <th>Health Zone</th>
            <th>CO Concentration (μg/m³)</th>
            <th>Effects on Human Health</th>
        </tr>
        <tr>
            <td style="background-color:#90EE90;">✅ Good</td>
            <td>0 – 10,000</td>
            <td>No harmful effects for the general population.</td>
        </tr>
        <tr>
            <td style="background-color:#FFD700;">⚠️ Medium</td>
            <td>10,000 – 30,000</td>
            <td>Possible mild symptoms such as headaches, dizziness, and nausea with prolonged exposure.</td>
        </tr>
        <tr>
            <td style="background-color:#FF6347;">🚨 Bad</td>
            <td>> 30,000</td>
            <td>Severe poisoning risk, leading to confusion, unconsciousness, and even death with prolonged exposure.</td>
        </tr>
    </table>"""
    }

    elif gas == "no2": return {
    "range": {
        "low": 0,
        "medium": 40,
        "high": 100
    }, 
    "table":"""
    <table border="1">
        <tr>
            <th>Health Zone</th>
            <th>NO₂ Concentration (μg/m³)</th>
            <th>Effects on Human Health</th>
        </tr>
        <tr>
            <td style="background-color:#90EE90;">✅ Good</td>
            <td>0 – 40</td>
            <td>No or minimal health effects. Safe for sensitive groups.</td>
        </tr>
        <tr>
            <td style="background-color:#FFD700;">⚠️ Medium</td>
            <td>40 – 100</td>
            <td>Increased risk of respiratory irritation, especially in children and asthmatics.</td>
        </tr>
        <tr>
            <td style="background-color:#FF6347;">🚨 Bad</td>
            <td>> 100</td>
            <td>Significant health risks, including lung inflammation, asthma aggravation, and cardiovascular effects.</td>
        </tr>
    </table>"""}
    elif gas == "o3": return {
    "range": {
        "low": 0,
        "medium": 100,
        "high": 180
    },
    "table": """
    <table border="1">
        <tr>
            <th>Health Zone</th>
            <th>O₃ Concentration (μg/m³)</th>
            <th>Effects on Human Health</th>
        </tr>
        <tr>
            <td style="background-color:#90EE90;">✅ Good</td>
            <td>0 – 100</td>
            <td>No or minimal health effects. Safe for all groups.</td>
        </tr>
        <tr>
            <td style="background-color:#FFD700;">⚠️ Medium</td>
            <td>100 – 180</td>
            <td>Increased respiratory symptoms in sensitive groups (children, elderly, people with asthma).</td>
        </tr>
        <tr>
            <td style="background-color:#FF6347;">🚨 Bad</td>
            <td>> 180</td>
            <td>Significant lung function reduction, throat irritation, coughing, and aggravation of respiratory diseases.</td>
        </tr>
    </table>"""}

    return {
    "range": {
        "low": 0,
        "medium": 50,
        "high": 125
    },
    "table": """
    <table border="1">
        <tr>
            <th>Health Zone</th>
            <th>SO₂ Concentration (μg/m³)</th>
            <th>Effects on Human Health</th>
        </tr>
        <tr>
            <td style="background-color:#90EE90;">✅ Good</td>
            <td>0 – 50</td>
            <td>No or minimal health effects. Safe for all groups.</td>
        </tr>
        <tr>
            <td style="background-color:#FFD700;">⚠️ Medium</td>
            <td>50 – 125</td>
            <td>Respiratory irritation, worsening of asthma in sensitive individuals.</td>
        </tr>
        <tr>
            <td style="background-color:#FF6347;">🚨 Bad</td>
            <td>> 125</td>
            <td>Severe respiratory distress, increased risk of lung diseases, and cardiovascular complications.</td>
        </tr>
    </table>"""}
