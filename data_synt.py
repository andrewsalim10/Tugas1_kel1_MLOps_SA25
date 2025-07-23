# from sdv.metadata import SingleTableMetadata
from sdv.metadata import Metadata
from sdv.single_table import GaussianCopulaSynthesizer
import pandas as pd

# baca data
data = pd.read_csv("Data\credit_risk_dataset.csv")

# buat metadata
metadata = Metadata()
the_metadata = metadata.detect_from_dataframe(data)

# buat sintesis data
synthesizer = GaussianCopulaSynthesizer(the_metadata)
synthesizer.fit(data)

synthetic_data = synthesizer.sample(num_rows=1000)

# simpan data baru
previous_data = data.copy()
previous_data.to_csv("Data\previous_credit_risk_dataset.csv", index=False)
synthetic_data.to_csv("Data\credit_risk_dataset.csv", index=False)
