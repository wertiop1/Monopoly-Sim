import numpy as np
import matplotlib.pyplot as plt
tiles = ["Go", "Mediterranean", "Community", "Baltic", "IncomeTax", 
         "ReadingRail", "Oriental", "Chance", "Vermont", "Connecticut", 
         "Visiting", "Charles", "Electric", "States", "Virginia", 
         "PennRail", "James", "Community", "Tennessee", "NY", 
         "FreePark", "Kentucky", "Chance", "Indiana", "Illinois", 
         "B&ORail", "Atlantic", "Ventnor", "Water", "Marvin", 
         "GOTOJAIL", "Pacific", "NorthCarolina", "Community", "PennAve", 
         "ShortLine", "Chance", "ParkPlace", "LuxuryTax", "Boardwalk",
            "Jail1", "Jail2", "Jail3"]
chanceCards = ["Go", "Illinois", "Charles", "Utiliy", "Railroad", "Back3", "Jail", "Reading", "Boardwalk"]
communityCards = ["Go","Jail"]
#16 of each card
prob = {2: 0.0, 3: 0.05555555555555555, 4: 0.05555555555555555, 5: 0.1111111111111111, 6: 0.1111111111111111, 7: 0.16666666666666666, 8: 0.1111111111111111, 9: 0.1111111111111111, 10: 0.05555555555555555, 11: 0.05555555555555555, 12: 0.0}
doubleProb = {2: 0.027777777777777776, 4: 0.027777777777777776, 6: 0.027777777777777776, 8: 0.027777777777777776, 10: 0.027777777777777776, 12: 0.027777777777777776}
nCards = 16
stochasticMatrix = np.zeros((len(tiles), len(tiles)))
for i in range(40):
    for key in prob:
        if(tiles[(i+key)%40] == "Chance"):
            stochasticMatrix[i,0] += prob[key]/nCards
            stochasticMatrix[i,24] += prob[key]/nCards
            stochasticMatrix[i,11] += prob[key]/nCards
            stochasticMatrix[i,40] += prob[key]/nCards
            stochasticMatrix[i,5] += prob[key]/nCards
            stochasticMatrix[i,39] += prob[key]/nCards
            if((i+key%40)!= 33):    
                stochasticMatrix[i,(i+key-3)%40] += prob[key]/nCards
            else:
                stochasticMatrix[i,0] += prob[key]/nCards/nCards
                stochasticMatrix[i,40] += prob[key]/nCards/nCards
                stochasticMatrix[i,(i+key)%40] = prob[key]*(nCards-len(communityCards))/nCards/nCards
            j = 0
            while(tiles[(i+key+j)%40] != "Electric" and tiles[(i+key+j)%40] != "Water"):
                j += 1
            stochasticMatrix[i,(i+key+j)%40] += prob[key]/nCards
            j = 0
            while(tiles[(i+key+j)%40] != "ReadingRail" and tiles[(i+key+j)%40] != "PennRail" and tiles[(i+key+j)%40] != "B&ORail" and tiles[(i+key+j)%40] != "ShortLine"):
                j += 1
            stochasticMatrix[i,(i+key+j)%40] += prob[key]/nCards
            stochasticMatrix[i,(i+key)%40] = prob[key]*(nCards-len(chanceCards))/nCards
        elif(tiles[(i+key)%40] == "Community"):
            stochasticMatrix[i,0] += prob[key]/nCards
            stochasticMatrix[i,40] += prob[key]/nCards
            stochasticMatrix[i,(i+key)%40] = prob[key]*(nCards-len(communityCards))/nCards
        elif((i+key) == 30):
            stochasticMatrix[i,40] += prob[key]
        else:
            stochasticMatrix[i,(i+key)%40] += prob[key]
stochasticMatrix[40,41] = 5/6
stochasticMatrix[41,42] = 5/6
stochasticMatrix[42,10] = 5/6
for i in range(40,43):
    for key in doubleProb:
        if(key != 12):
            stochasticMatrix[i,10+key] = 1/36
        else:
            stochasticMatrix[i,0] += 1/(36*nCards)
            stochasticMatrix[i,24] += 1/(36*nCards)
            stochasticMatrix[i,11] += 1/(36*nCards)
            stochasticMatrix[i,40] += 1/(36*nCards)
            stochasticMatrix[i,5] += 1/(36*nCards)
            stochasticMatrix[i,39] += 1/(36*nCards)
            stochasticMatrix[i,(i+key-3)%40] += 1/(36*nCards)
            while(tiles[(10+key+j)%40] != "Electric" and tiles[(10+key+j)%40] != "Water"):
                j += 1
            stochasticMatrix[i,(10+key+j)%40] += 1/(36*nCards)
            j = 0
            while(tiles[(10+key+j)%40] != "ReadingRail" and tiles[(10+key+j)%40] != "PennRail" and tiles[(10+key+j)%40] != "B&ORail" and tiles[(10+key+j)%40] != "ShortLine"):
                j += 1
            stochasticMatrix[i,(10+key+j)%40] += 1/(36*nCards)
            stochasticMatrix[i,(10+key)%40] += (nCards-len(chanceCards))/nCards * 1/36
finalMatrix = stochasticMatrix.copy()
finalMatrix[:40,40] += 1/6 
doubleMatrix = stochasticMatrix.copy()
for i in range(40):
    for key in doubleProb:
        doubleMatrix[i] += finalMatrix[(i+key)%40]*doubleProb[key]
for i in range(40):
    for key in doubleProb:
        stochasticMatrix[i] += doubleMatrix[(i+key)%40]*doubleProb[key]
        
finalMatrix = finalMatrix.T
stochasticMatrix = stochasticMatrix.T
doubleMatrix = doubleMatrix.T

#print('[',end="")
#for i in stochasticMatrix:
#    print('[',end="")
#    for j in i[:-1]:
#        print(round(j,5),end=",")
#    print(round(i[-1],5),end="")
#    print(']',end=",")
#print(']',end="")
for i in range(41):
    print("'a"+str(i+1)+"':" + "1",end=",")
eigenvalues, eigenvectors = np.linalg.eig(stochasticMatrix)
if __name__=="__main__":
    #for i in eigenvectors[:,0].real:
    #    print(round(i,5),end=",")
    print(eigenvectors[:0])
    np.savetxt("finalMatrix.csv", finalMatrix, delimiter=",")
    np.savetxt("doubleMatrix.csv", doubleMatrix, delimiter=",")
    np.savetxt("stochasticMatrix.csv", stochasticMatrix, delimiter=",")
    plt.imshow(eigenvectors[:,0].real.reshape(-1,1), interpolation="nearest")
    plt.colorbar(label="Value")
    plt.title("Stochastic Matrix Heatmap")
    plt.savefig("Stochastic_Matrix_Heatmap.png")
