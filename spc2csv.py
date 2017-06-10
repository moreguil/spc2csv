import hyperspy.api as hs
import csv
import numpy as np
import os


class spc2csv():
    def convert_spc2csv(spectrum):
        """
        :return: save converted csv file with same directory of original spc file.
        """
        s = hs.load(spectrum)

        st = s.original_metadata.spc_header.startEnergy
        ed = s.original_metadata.spc_header.endEnergy
        tt = s.original_metadata.spc_header.numPts

        iteration = np.arange(0, (tt - 1))
        step = ((ed - st) / tt)

        output_path = spectrum.replace('.spc', '.csv')
        with open(output_path, 'w') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            writer.writerow(["Energy", "Intensity"])
            for i in iteration:
                data = (i * step, s.data[i])
                writer.writerow(data)

    def get_spcFile(directory):
        """
        :return: set list that contains 'name' of every .spc file in specified directory.
        """
        list = []
        for file in os.listdir(directory):
            if file.endswith(".spc"):
                list.append(os.path.join(file))
        return list

if __name__ == "__main__":
    directory = './spcfiles'
    spcl = spc2csv.get_spcFile(dir)

    for i in spcl:
        spc2csv.convert_spc2csv(str(dir) + '/' + str(i))