from views.detection.view import View
from views.common.prop import Prop

# Root
root_view = View()
prop = Prop()

# Detection

## Discover alert
detection_view = View()
detection_view.header_detection()
detection_view.subheader_discover_alert()
detection_view.step_determine_alert_origin()

prop.divider()

## Access alert
detection_view.subheader_assess_alert()
detection_view.step_investigate_alert()
detection_view.step_determine_partner_impact()

prop.divider()

## Triage alert
detection_view.subheader_triage_alert()
detection_view.step_triage()
