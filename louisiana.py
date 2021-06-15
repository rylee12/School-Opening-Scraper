from tableauscraper import TableauScraper as TS
from datetime import datetime
import logging

def main():
    logging.basicConfig(filename='app.log', filemode='a', format='%(asctime)s - %(message)s', level=logging.INFO)
    
    url="https://analytics.la.gov/t/DOE/views/DigitalLearningModel/SchoolLevelModeofLearning/P00338204A@swe.la.gov/29ea44c5-4c98-44e0-87dc-2c2b907e7ac3?%3Adisplay_count=n&%3AshowVizHome=n&%3Aorigin=viz_share_link&%3AisGuestRedirectFromVizportal=y&%3Aembed=y"
    ts = TS()
    ts.loads(url)
    logging.info("Received LA Data", exc_info=False);
    
    ws = ts.getWorksheet("Site Map (2)")
    ws.data.to_csv("out/LA_" + datetime.now().strftime('%Y%m%d') + ".csv")
    logging.info("Wrote LA Data", exc_info=False);

# main()
