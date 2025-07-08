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
    person_income = person_income // 1000
    match(person_home_ownership): # Kredit/KPR : 0, Lainnya : 1, Pribadi: 2, Menyewa : 3
        case "Kredit/KPR":
            person_home_ownership = 0
        case "Lainnya":
            person_home_ownership = 1
        case "Pribadi":
            person_home_ownership = 2
        case _:
            person_home_ownership = 3
    
    match(loan_intent):
        case "Perhutangan":
            loan_intent = 0
        case "Edukasi":
            loan_intent = 1
        case "Perabotan":
            loan_intent = 2
        case "Kesehatan":
            loan_intent = 3
        case "Pribadi":
            loan_intent = 4
        case _:
            loan_intent = 5

    loan_amnt = loan_amnt // 1000
    match(cb_person_default_on_file):
        case "Tidak":
            cb_person_default_on_file = 0
        case _:
            cb_person_default_on_file = 1

    features = [person_age, person_income, person_home_ownership, person_emp_length, loan_intent, loan_amnt, loan_int_rate, loan_percent_income, cb_person_default_on_file, cb_person_cred_hist_length]
    
    features = [features]
    prediction = pipe.predict(features)[0]

    label = f"Status Pinjaman: {'Ditolak' if prediction == 1 else 'Diterima'}"
    return label

inputs = [
    gr.Number(minimum=18, maximum=55, label="Umur"),
    gr.Number(minimum = 4_000_000, maximum = 600_000_000, label="Penghasilan Tahunan (Rp)"),
    gr.Dropdown(choices=["Kredit/KPR", "Menyewa", "Pribadi", "Lainnya"], label="Tempat tinggal"),
    gr.Number(minimum=1, label="Lama Bekerja (Tahun)"),
    gr.Dropdown(choices=["Perhutangan", "Edukasi", "Perabotan", "Kesehatan", "Pribadi", "Bisnis"], label="Tujuan Pinjaman"),
    gr.Number(minimum=1_000_000, label="Jumlah Pinjaman (Rp)"),
    gr.Slider (minimum = 5.42,maximum = 23.22, label="Suku Bunga Pinjaman Tahunan(%)"),
    gr.Number(minimum= 0.05, label="Persentase pendapatan yang akan disisihkan untuk melunasi (%)"),
    gr.Dropdown(choices=["Tidak", "Iya"], label="Apakah pernah mengalami Gagal Bayar?"),
    gr.Number(minimum=1, label="Lama Peminjaman Kredit (Bulan)"),
]

outputs = [gr.Label(num_top_classes=1, label="Hasil Prediksi")]

examples = [
    [23,95_000_000,"Menyewa",2.0,"Bisnis",35_000_000,7.9,0.37,"Tidak",2],
    [26,108_160_000,"Menyewa",4.0,"Edukasi",35_000_000,18.39,0.32,"Tidak",4],
    [23,115_000_000,"Menyewa",2.0,"Edukasi",35_000_000,7.9,0.3,"Tidak",4],
    [23,500_000_000,"Kredit/KPR",7.0,"Perhutangan",30_000_000,10.65,0.06,"Tidak",3],
    [23,120_000_000,"Menyewa",1.0,"Edukasi",35_000_000,7.9,0.29,"Tidak",4]
]

title = "Prediksi Risiko Kredit"
description = "Aplikasi ini memprediksi apakah pinjaman akan diberikan atau tidak berdasarkan informasi pribadi dan pinjaman."
article = "Anggota Kelompok: " \
"\n- Andrew Salim (205150207111048)" \
"\n- Bagus Jati Pramono (215150200111012)" \
"\n- Daffa Daniswara Kodrihan (195150200111052)" \
"\n- Sonia Anindhiya (225150200111045)" \
"\n\nAplikasi ini menggunakan model machine learning untuk memprediksi risiko kredit."

gr.Interface(
    fn=predict_credit_risk,
    inputs=inputs,
    outputs=outputs,
    examples=examples,
    title=title,
    description=description,
    article=article,
    allow_flagging="never",
).launch()
