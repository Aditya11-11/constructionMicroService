form_schemas = {
    "swms": """{
  "swms_title": "",
  "project": "",
  "working_area": "",
  "work_description": "",
  "hazards_and_controls": [
    {
      "hazard": "",
      "description": "",
      "risk_level": "",
      "control_measure": ""
    }
  ],
  "ppe_requirements": {
    "hard_hat": false,
    "safety_boots": false,
    "high_vis_vest": false,
    "safety_glasses": false
  },
  "required_permits": {
    "working_at_heights": false,
    "hot_work": false,
    "confined_space": false,
    "excavation": false
  }
}""",

    "IncidentReport": """{
  "incident_type": "",
  "date_time": "",
  "location": "",
  "description": "",
  "severity_level": "",
  "witnesses": [],
  "immediate_action_taken": "",
  "uploaded_evidence": []
}""",

    "ITP": """{
  "project_name": "",
  "inspection_type": "",
  "inspector": "",
  "inspection_date": "",
  "inspection_items": [
    {
      "item_description": "",
      "item_status": "pass or fail",
      "comments": ""
    }
  ],
  "attachments": [],
  "additional_notes": ""
}""",

    "RFI": """{
  "subject": "",
  "priority": "",
  "due_date": "",
  "assignee": "",
  "department": "",
  "description": "",
  "attachments": []
}"""
}




compliance_json_template = """{
  "issue_summary": "",
  "compliance_issues": [
    {
      "standard": "",
      "section": "",
      "issue": "",
      "rectification": ""
    }
  ],
  "overall_status": ""
}"""
