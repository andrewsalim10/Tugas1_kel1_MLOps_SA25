import gradio as gr
import skops.io  as sio
import pandas as pd

unknown_types = sio.get_untrusted_types(file="Model/credit_loan_detection.skops")
pipe = sio.load("Model/credit_loan_detection.skops", trusted = unknown_types)
def predict_credit_risk(person_age, person_income, person_home_ownership,person_emp_length, loan_intent, loan_amnt, loan_int_rate, loan_percent_income, cb_person_default_on_file, cb_person_cred_hist_length):
    """Predict credit risk based on person information.
    Args:
        person_age (int): Age of the person.
        person_income (float): Income of the person.
        person_emp_length (float: Length of employment in years.
        loan_intent (int): Intent of the loan.
        loan_amnt (int): Amount of the loan.
        loan_int_rate (float): Interest rate of the loan.
        loan_percent_income (float): Percentage of income for the loan.
        cb_person_default_on_file (int): Default status on file.
        cb_person_cred_hist_length (int): Length of credit history in months.

    Returns:
        str: Prediction result indicating if the person is granted load or not.
    """
    features = [person_age, person_income, person_home_ownership, person_emp_length, loan_intent, loan_amnt, loan_int_rate, loan_percent_income, cb_person_default_on_file, cb_person_cred_hist_length]
    
    features[1] = features[1] // 1000  # Convert income to millions for consistency
    features[5] = features[5] // 1000  # Convert loan amount to millions for consistency
    
    features = [features]
    prediction = pipe.predict(features)[0]

    # print(prediction)

    label = f"Predicted Loan Status: {'Not Granted' if prediction == 1 else 'Granted'}"
    return label

inputs = [
    gr.Number(minimum=18, maximum=55, label="Umur"),
    gr.Number(minimum = 4000000, maximum = 600000000, label="Penghasilan Tahunan (Rp)"),
    gr.Dropdown(choices=[0, 1, 2, 3], label="Tempat tinggal (Kredit/KPR : 0, Lainnya : 1, Pribadi: 2, Menyewa : 3)"),
    gr.Number(label="Lama Bekerja (Tahun)"),
    gr.Dropdown(choices=[0, 1, 2, 3, 4, 5], label="Tujuan Pinjaman (Perhutangan : 0, Edukasi : 1, Renovasi Rumah : 2, Kesehatan : 3, Pribadi : 4, Bisnis: 5)"),
    gr.Number(label="Jumlah Pinjaman (Rp)"),
    gr.Slider (minimum = 5.42,maximum = 23.22, label="Suku Bunga Pinjaman Tahunan(%)"),
    gr.Number(label="Persentase pendapatan yang akan disisihkan untuk melunasi (%)"),
    gr.Dropdown(choices=[0, 1], label="Apakah pernah mengalami Gagal Bayar (0: No, 1: Yes)"),
    gr.Number(label="Lama Peminjaman Kredit (Bulan)"),
]

outputs = [gr.Label(num_top_classes=1, label="Hasil Prediksi")]

examples = [
    [30, 4000000, 5, 0, 10000, 7.0, 20, 0, 6],
    [45, 10000000, 10, 1, 20000, 8.5, 25, 1, 12],
]

title = "Prediksi Risiko Kredit"
description = "Aplikasi ini memprediksi apakah pinjaman akan diberikan atau tidak berdasarkan informasi pribadi dan pinjaman."
article = "Anggota Kelompok: \n- Andrew Salim 1\n- Nama Anggota 2\n- Nama Anggota 3\n\nAplikasi ini menggunakan model machine learning untuk memprediksi risiko kredit."

# print()
# print(inputs)
# print()

gr.Interface(
    fn=predict_credit_risk,
    inputs=inputs,
    outputs=outputs,
    examples=None,
    title=title,
    description=description,
    article=article,
    allow_flagging="never",
).launch()
