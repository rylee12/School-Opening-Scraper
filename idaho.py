import pandas as pd
from arcgis import GIS
from datetime import datetime
import logging

def main():
    #logging.basicConfig(filename='app.log', filemode='a', format='%(asctime)s - %(message)s', level=logging.INFO)
    gis = GIS()
    item = gis.content.get("2d0c7fa5ea95405d8e8761801a456c4d")
    flayer = item.layers[0]
    #logging.info("Received Idaho Data", exc_info=False);

    sdf = pd.DataFrame.spatial.from_layer(flayer)
    sdf = sdf.drop(["shape_leng","globalid","created_user","last_edited_user","Shape__Length","Shape__Area", "SHAPE"],axis=1)
    sdf.to_csv("out/ID_" + datetime.now().strftime('%Y%m%d') + ".csv")
    #logging.info("Wrote Idaho Data", exc_info=False);

# main()
