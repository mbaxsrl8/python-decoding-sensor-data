from datetime import date

from house_info import HouseInfo


class EnergyData(HouseInfo):
    ENERGY_PER_BULB = 0.2
    ENERGY_BITS = 0x0F0

    # This method will help us extract the energy data information from energy_usage data field
    # The rec parameter is a string. This string represents the energy_usage in hexadecimal notation form.
    # The energy_usage field comes as a three-digit hexadecimal (hex) number (12 bits), for example "0xfef".
    def _get_energy(self, rec):
        energy = int(rec, base=16)
        energy = energy & self.ENERGY_BITS
        energy = energy >> 4
        return energy

    # This method will help us convert the energy data.
    # The data parameter is a list of strings. These strings represent energy usage in hexadecimal form.
    def _convert_data(self, data):
        recs = []
        for rec in data:
            recs.append(self._get_energy(rec))
        return recs

    def get_data_by_area(self, rec_area=0):
        recs = super().get_data_by_area("energy_usage", rec_area)
        return self._convert_data(recs)

    def get_data_by_date(self, rec_date=date.today()):
        recs = super().get_data_by_date("energy_usage", rec_date)
        return self._convert_data(recs)

    # The purpose of this method is to take a list of energy usage values,
    # calculate the cost per light bulb usage, and return the sum of all the values in the data list.
    def calculate_energy_usage(self, data):
        total_energy = sum([field * self.ENERGY_PER_BULB for field in data])
        return total_energy
