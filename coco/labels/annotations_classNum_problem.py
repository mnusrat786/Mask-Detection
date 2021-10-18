import os

arr = os.listdir("Train/")
for aa in arr:
    # print(aa)

    extensionns = aa.split('.')[-1]
    if(extensionns == "txt"):
        try:
            lines = []
            with open(f'Train/{aa}') as f:
                lines = f.readlines()

            for line in lines:
                aaaaaaa = line.split(" ")[0]
                if (int(aaaaaaa) > 1):
                    with open(f"AnnotationsClassesProblem.txt", "a") as file_object:
                        file_object.write(f"{aa}")
                    with open(f"AnnotationsClassesProblem.txt", "a") as file_object:
                        file_object.write(f"    {aaaaaaa} \n")


        except:
            pass