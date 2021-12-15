
matice = [[[1,2,3],[4,5,6],[7,8,9]]

print
# kosik = []
# kosik.append(jabka)
# kosik.append(hrusky)

for radek in range(len(matice)):
    for sloupec in range(len(matice)):
        if(matice[radek][sloupec] == 5):
            matice[radek][sloupec].setTrue()
            print("jupí, je to " + str(matice[radek][sloupec]))