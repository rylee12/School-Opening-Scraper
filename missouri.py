from tableauscraper import TableauScraper as TS
from datetime import datetime
import logging

def main():
    logging.basicConfig(filename='app.log', filemode='a', format='%(asctime)s - %(message)s', level=logging.INFO)

    url="https://results.mo.gov/t/DESE/views/LearningMethods-Opening-Enrollment-Public/LearningMethods?:showAppBanner=false&:display_count=n&:showVizHome=n&:origin=viz_share_link%22%20title%3D%22open%20Enrollment%20Public&:isGuestRedirectFromVizportal=y&:embed=y&:toolbar=no"
    ts = TS()
    ts.loads(url)
    logging.info("Received MO Data", exc_info=False);

    ws = ts.getWorksheet("MOmap-AllCategory")
    ws.data.to_csv("out/MO_" + datetime.now().strftime('%Y%m%d') + ".csv")
    logging.info("Wrote MO Data", exc_info=False);

main()
