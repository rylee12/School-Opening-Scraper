import pandas as pd

from datetime import datetime

from arcgis import GIS


def main():
    gis = GIS()
    item = gis.content.get("75b42ab2b2c2664d9771c48bd4dcd536")
    flayer = item.layers[0]

    sdf = pd.DataFrame.spatial.from_layer(flayer)
    sdf = sdf.drop(["shape_leng","globalid","created_user","last_edited_user","Shape__Length","Shape__Area", "SHAPE"],axis=1)
    sdf.to_csv("out/NYC_" + datetime.now().strftime('%Y%m%d') + ".csv")