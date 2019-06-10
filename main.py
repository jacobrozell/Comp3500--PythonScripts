
def create_files(fileIn, fileOut, csvFileOut):
    with open(fileOut, 'w') as parsedFile:
        with open(fileIn) as file1:
            for line in file1:
                if line.startswith("J") or line.startswith('*') \
                        or line.startswith("P") or line.startswith("N") \
                        or line.startswith("A"):
                    parsedFile.write(line)

    unknowns = ""
    pids = ""
    jats = ""
    tjds = ""
    mems = ""
    comma = ","

    with open(csvFileOut, 'w') as csv:
        with open(fileOut) as file1:
            for line in file1:
                if line.startswith("*") or line.startswith("P") or line.startswith("N") or line.startswith("A"):
                    continue
                else:
                    # make line look like PID, JAT, TJD
                    unknownValue = line[1:12].replace(" ", "") + ","
                    pidValue = line[19:22].replace(" ", "") + ","
                    jatValue = line[29:39].replace(" ", "") + ","
                    tjdValue = line[45:55].replace(" ", "") + ","
                    memValue = line[63:67].replace(" ", "") + ","

                    unknowns += unknownValue
                    pids += pidValue
                    jats += jatValue
                    tjds += tjdValue
                    mems += memValue

            else:
                csv.write(unknowns)
                csv.write("\n")
                csv.write(pids)
                csv.write("\n")
                csv.write(jats)
                csv.write("\n")
                csv.write(tjds)
                csv.write("\n")
                csv.write(mems)
                csv.write("\n")

