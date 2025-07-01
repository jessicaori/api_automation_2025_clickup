import pymsteams

from config.config import web_hook

teams_message = pymsteams.connectorcard(web_hook)
teams_message.title("Jessica Orihuela - Pytest Project Report")
with open("reports/markdown/md-report.md") as f:
    report = f.read()
teams_message.text(report)
teams_message.send()