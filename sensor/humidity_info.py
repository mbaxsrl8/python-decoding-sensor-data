from datetime import date

from house_info import HouseInfo


class HumidityData(HouseInfo):

    # This method will help us convert the humidity data.
    # data is a list of str
    def _convert_data(self, data):
        recs = []
        for rec in data:
            recs.append(float(rec) * 100)
        return recs

    # The purpose of this method is to filter the humidity data by the "area" field
    # The default value of rec_area translates to all records
    def get_data_by_area(self, rec_area=0):
        recs = super().get_data_by_area("humidity", rec_area)
        return self._convert_data(recs)

    # The purpose of this method is to filter the humidity data by the "date" field
    def get_data_by_date(self, rec_date=date.today()):
        recs = super().get_data_by_date("humidity", rec_date)
        return self._convert_data(recs)