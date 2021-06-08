import os
import numpy as np
import pandas as pd


class Loader:
    """
    Klasa pozwalajająca na załadowanie danych
    i pobranie konkretnych fragmentów sygnałów EKG i BR
    """

    def __init__(self, case_dir='VP06/', ):
        """
        Przypisanie bazowej ścieżki do folderu z katalogami pacjentów.
        :param case_dir: ścieżka do folderu pacjenta
        """
        self.base_dir = 'electrocardiogram-skin-conductance-and-respiration-from-spider-fearful-individuals-watching-spider-video-clips-1.0.0'
        self.case_dir = os.path.join(self.base_dir, case_dir)
        self.available_border_points = self._get_available_border_points()
    
    def _load_data(self, dir):
        """
        Metoda ładująca dane z pliku txt do macierzy.
        :param dir: odpowiedni plik z danymi BR/ECG
        :return: np.array
        """
        data = np.loadtxt(dir, delimiter='\t', skiprows=1, dtype=str)
        data = np.delete(data, 2, 1)
        data = data.astype(np.float32)
        return data

    def load_ECG(self, is_dataframe=False):
        """
        Metoda ładująca dane EKG, wykorzystuje _load_data()
        :param is_dataframe: czy zwrócić pandas.dataframe
        :return:  np.array/pd.dataframe dane EKG
        """
        ecg_data_dir = os.path.join(self.case_dir, 'BitalinoECG.txt')
        ecg_data = self._load_data(ecg_data_dir)

        if is_dataframe:
            df = pd.DataFrame({'Time': ecg_data[:, 1], 'Amp': ecg_data[:, 0]})
            return df
        return ecg_data

    def load_BR(self, is_dataframe=False):
        """
        Metoda ładująca dane BR, wykorzystuje _load_data()
        :param is_dataframe: czy zwrócić pandas.dataframe
        :return: np.array/pd.dataframe dane oddechowe
        """
        br_data_dir = os.path.join(self.case_dir, 'BitalinoBR.txt')
        br_data = self._load_data(br_data_dir)

        if is_dataframe:
            df = pd.DataFrame({'Time': br_data[:, 1], 'Amp': br_data[:, 0]})
            return df
        return br_data

    def _get_available_border_points(self):
        """
        Metoda zwracająca nazwy klipów i  ich sygnatury czasowe z pliku Triggers.txt
        :return: pd.dataframe
        """
        trigger_dir = os.path.join(self.case_dir, 'Triggers.txt')
        border_data = np.loadtxt(trigger_dir, delimiter='\t', skiprows=0, dtype=str)
        df = pd.DataFrame({'Event': border_data[:, 0], 'Started': border_data[:, 1], 'Ended': border_data[:, 2]})
        return df
    
    def get_index_of_border_points(self, event_id, data):
        """
        Metoda zwracająca numery próbek dla konkretnego nagrania.
        :param event_id: klucz obiektu pd.dataframe self.available_border_points
        :param data: Obiekt danych BR lub EKG
        :return: dict zawierający numery próbek dla danej sygnatury czasowej pliku.
        """
        row = self.available_border_points.loc[event_id]
        started_vl = float(row['Started'])
        ended_vl = float(row['Ended'])
        if type(data) is np.ndarray:
            try:
                started = np.where(data[:,1] == float(started_vl))
                started = started[0][0] + 1
                ended = np.where(data[:,1] == float(ended_vl))
                ended = ended[0][0]
            except IndexError:
                return {}
        else:
            started = data[data['Time'].gt(started_vl)].index[0]
            ended = data[data['Time'].gt(ended_vl)].index[0] - 1

        return {'started': started, 'ended': ended}


            







    


