# == Read the monthly temperature data for Taipei station == #

import pandas as pd
import numpy as np

Taipei_monthly_temp_csv = pd.read_csv("Taipei_temp_record.csv")
print(Taipei_monthly_temp_csv)
Taipei_monthly_temp_series = np.array(Taipei_monthly_temp_csv["Temperature (deg C)"])

# =========================================================== #