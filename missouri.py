from tableauscraper import TableauScraper as TS
from datetime import datetime
import logging

def main():
    logging.basicConfig(filename='app.log', filemode='a', format='%(asctime)s - %(message)s', level=logging.INFO)

    url="https://results.mo.gov/t/DESE/views/LearningMethods-Opening-Enrollment-Public/LearningMethods?:showAppBanner=false&:display_count=n&:showVizHome=n&:origin=viz_share_link%22%20title%3D%22open%20Enrollment%20Public&:isGuestRedirectFromVizportal=y&:embed=y&:toolbar=no"
    ts = TS()
    ts.loads(url)
    logging.info("Received MO Data", exc_info=False);

    lea_on_map = ts.getWorksheet("MOmap-AllCategory").data
    lea_not_on_map = ts.getWorksheet("MOmap-AllCategory (2)").data
    result = lea_on_map.append(lea_not_on_map)
    result = result.reset_index(drop=True)
    result.to_csv("out/MO_" + datetime.now().strftime('%Y%m%d') + ".csv")

#main()
