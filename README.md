# Temat pracy: Wykorzystując rozkład PCA, ICA spróbować wyznaczyć składową oddechową z sygnału EKG.


Praca obejmuje próby wykorzystania metod rozkładu PCA i ICA w celu wykorzystania informacji oddechowej
z sygnału EKG, nazywanej często sygnałem EDR (ECG derived respiration). W pracy wykorzystano bazę danych
z serwisu Physionet [1, 2 ,3].

Kroki obejmujące wydobycie EDR za pomocą PCA [5, 6]:
  - Detekcja szczytów R
  - Nałożenie okna pokrywającego całe uderzenie na wykryte szczyty - na wybranej bazie 80 próbek
  - Wykorzystanie PCA i wydobycie pierwszego wektora własnego
  
Kroki obejmujące wydobycie EDR za pomocą ICA [8, 9]:
  - Detekcja szczytów R
  - Stworzenie macierzy danych oraz zastosowanie transformacji wybielającej dane (ang. whitening data)
  - Zastosowanie metody PCA do redukcji wymiarowości oraz wybranie 10-ciu PCs (ang. Principal Components) 
  - Zastosowanie algorytmu fastICA w celu uzyskania sygnałów źródłowych 
  - Obliczenie transformaty Fouriera dla powstałych IC 
  - Otrzymanie sygnału oddechowego za pomocą analizy wykresu ICs Frequency Sprectrum (12-24 bpm)
  - Przefiltrowanie wyników otrzymanych w poprzednim kroku w rozsądnych częstotliwościach 
    oddychania (0,0666-0,5 Hz), aby uzyskać sygnał oddychania ICA.

Wyniki potwierdziły możliwość wydobycia sygnału oddechowego z EKG, jednakże są znacznie niższe niż referencyjne,
przyczyny takiego zjawiska doszukuję się głównie w dobranej bazie danych, któa charakteryzuję się znacznie niższą
częstotliwością próbkowania (100 Hz)



[1] Ihmig, F. R., Gogeascoechea, A., Schäfer, S., Lass-Hennemann, J., & Michael, T. (2020).
Electrocardiogram, skin conductance and respiration from spider-fearful individuals watching
spider video clips (version 1.0.0). PhysioNet. https://doi.org/10.13026/sq6q-zg04.
[2] Ihmig, F. R., Gogeascoechea H., A., Neurohr-Parakenings, F., Schäfer, S. K.,
Lass-Hennemann, J., & Michael, T. (2020). On-line anxiety level detection from biosignals:
machine learning based on a randomized controlled trial with spider-fearful individuals. PLoS
ONE, in press.
[3] Goldberger, A., Amaral, L., Glass, L., Hausdorff, J., Ivanov, P. C., Mark, R., ... & Stanley,
H. E. (2000). PhysioBank, PhysioToolkit, and PhysioNet: Components of a new research
resource for complex physiologic signals. Circulation [Online]. 101 (23), pp. e215–e220.
[4] Dominika K, Karolina H. (2010) “Określenie osi elektrycznej załamków, wyznaczenie
sygnału oddechu z zapisu EKG”.
[5] E. J. Bowers, A. Murray, & P. Langley (2008). Respiratory rate derived from principal
component analysis of single lead electrocardiogram. In 2008 Computers in Cardiology (pp.
437-440).
[6] P. Langley, E. J. Bowers, & A. Murray (2010). Principal Component Analysis as a Tool for
Analyzing Beat-to-Beat Changes in ECG Features: Application to ECG-Derived Respiration.
IEEE Transactions on Biomedical Engineering, 57(4), 821-829.
[7] WIDJAJA, Devy, et al. Application of kernel principal component analysis for
single-lead-ECG-derived respiration. IEEE Transactions on Biomedical Engineering, 2012,
59.4: 1169-1176
[8] Tiinanen, Suvi, et al. ECG-derived respiration methods: Adapted ICA and PCA. Medical
engineering & physics, 2015, 37.5: 512-517.
[9] Kozia, Christina; Herzallah, Randa; LOWE, David. ICA-Derived Respiration Using an
Adaptive R-Peak Detector. In: International Conference on Time Series and Forecasting.
Springer, Cham, 2018. p. 363-377
