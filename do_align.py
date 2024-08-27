from pathlib import Path
import shutil

def align_mt():
    new_path = shutil.copy('./data/mt1.csv', './data_aligned/')
def align_my():
    new_path = shutil.copy('./data/my1.csv', './data_aligned/')

def align_df():
    contents = []
    input_file = Path("./data/df1.csv")
    with open(input_file, mode='r', encoding='utf-8') as f:
        for i, line in enumerate(f, 1):
            if i in [173, 175]:
                line = ',,,' + line
            if i in [3, 77, 86, 97, 104, 159, 160, 161, 163, 164, 166, 167, 168, 170\
                     , 171, 174, 176]:
                line = ',,' + line
            if i in [5, 7, 9, 24, 26, 27, 28, 29, 31, 32, 33, 34, 36, 37, 38, 39, 41\
                     ,43, 44, 45, 46, 48, 49, 50, 51, 53, 54, 55, 56, 61, 62, 63, 64\
                     ,65, 66, 68, 69, 70, 71, 72, 73, 79, 81, 83, 85, 88, 90, 92, 112\
                     ,114, 116, 119, 122, 125, 128, 133, 134, 135, 136, 137, 138, 140\
                     ,141, 142, 143, 144, 145, 147, 148, 149, 150, 151, 152, 153, 154\
                     ,155, 156, 162, 169]:
                line = ',' + line
            contents.append(line)

    # 1行ずつ書き込み
    output_file = Path("./data_aligned/df1.csv")
    with open(output_file, mode='w') as f:
        for content in contents:
            f.write(content)
def align_nw():
    contents = []
    input_file = Path("./data/nw1.csv")
    with open(input_file, mode='r', encoding='utf-8') as f:
        for i, line in enumerate(f, 1):
            if i in [2, 11, 13, 14, 16, 17,21,22,24,25,27,28\
                    ,30,31,33,34,36,38,42,43,46,54,59,63,68\
                    ,73,78,83,91,102,113,118,123,125,127,130,132,134,145,152\
                     ,157,162,167,172,177]:
                line = ',' + line
            contents.append(line)

    # 1行ずつ書き込み
    output_file = Path("./data_aligned/nw1.csv")
    with open(output_file, mode='w') as f:
        for content in contents:
            f.write(content)

def main():
    align_df()
    align_mt()
    align_nw()
    align_my()


if __name__ == '__main__':
    main()
