def check_output():
    with open("outfile.txt", "r") as outfile:
        output = outfile.readlines()
        with open("test_folder/expected_output.txt", "r") as expected_outputfile:
            expected_output = expected_outputfile.readlines()
            if output == expected_output:
                return 1
            else:
                return 0

check_output()