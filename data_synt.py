# from sdv.metadata import SingleTableMetadata
from sdv.metadata import Metadata
from sdv.single_table import GaussianCopulaSynthesizer
import pandas as pd

# baca data
data = pd.read_csv('Data\credit_risk_dataset.csv')

# buat metadata
metadata = Metadata()
metadata.detect_from_dataframe(data)

# buat sintesis data
synthesizer = GaussianCopulaSynthesizer(metadata)
synthesizer.fit(data=data)

synthetic_data = synthesizer.sample(num_rows=500)

# simpan data baru
previous_data = data.copy()
previous_data.to_csv('Data\previous_credit_risk_dataset.csv', index=False)
synthetic_data.to_csv('Data\credit_risk_dataset.csv', index=False)