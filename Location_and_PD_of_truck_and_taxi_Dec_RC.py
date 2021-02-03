import numpy as np
from matplotlib import pyplot as plt

def create_data_model():
    data = {}
    
    data['Location'] = np.array([
    (20, 20), # location 0 - the depot
    (2.56, 4.84),    # location 1
    (4.59, 17.26),    # location 2
    (16.34, 18.11),    # location 3
    (12.01, 15.31),    # location 4
    (18.27, 3.32),    # location 5
    (14.84, 10.43),    # location 6
    (8.20, 9.46),    # location 7
    (37.78, 1.89),    # location 8
    (15.03, 0.67),    # location 9
    (2.27, 15.45),    # location 10
    (22.12, 37.35),    # location 11
    (7.96, 25.06),    # location 12
    (36.22, 30.21),    # location 13
    (33.00, 20.93),    # location 14
    (26.07, 21.29),    # location 15
    (28.84, 38.06),    # location 16
    (28.34, 31.68),    # location 17
    (1.09, 37.15),    # location 18
    (22.98, 25.97),    # location 19
    (33.84, 37.06),    # location 20
    (1.63 ,27.02),    # location 21
    (5.17, 9.34),    # location 22
    (10.38, 32.09),    # location 23
    (34.80, 8.99),    # location 24
    (31.86, 2.05),    # location 25
    (12.57, 3.13),    # location 26
    (37.12, 14.62),    # location 27
    (38.63, 27.26),    # location 28
    (15.08, 39.05),    # location 29
    (29.68, 23.97),    # location 30
    (18.12, 12.39),    # location 31
    (28.76, 8.76),    # location 32
    (22.00, 30.14),    # location 33
    (26.37, 35.47),    # location 34
    (9.01, 16.31),    # location 35
    (32.88, 31.42),    # location 36
    (34.74, 13.68),    # location 37
    (5.09, 1.00),    # location 38
    (8.23, 39.62),    # location 39
    (12.22, 24.30)    # location 40
    ])
    
    data['Locationw'] = np.array([
    (20, 20), # location 0 - the depot
    (2.56, 4.84),    # location 1
    (4.59, 17.26),    # location 2
    (16.34, 18.11),    # location 3
    (12.01, 15.31),    # location 4
    (18.27, 3.32),    # location 5
    (14.84, 10.43),    # location 6
    (8.20, 9.46),    # location 7
    (37.78, 1.89),    # location 8
    (15.03, 0.67),    # location 9
    (2.27, 15.45),    # location 10
    (22.12, 37.35),    # location 11
    (7.96, 25.06),    # location 12
    (36.22, 30.21),    # location 13
    (33.00, 20.93),    # location 14
    (26.07, 21.29),    # location 15
    (28.84, 38.06),    # location 16
    (28.34, 31.68),    # location 17
    (1.09, 37.15),    # location 18
    (22.98, 25.97),    # location 19
    (33.84, 37.06)    # location 20
    ])
    
    data['Locationh'] = np.array([
    (20, 20), # location 0 - the depot
    (1.63 ,27.02),    # location 21
    (5.17, 9.34),    # location 22
    (10.38, 32.09),    # location 23
    (34.80, 8.99),    # location 24
    (31.86, 2.05),    # location 25
    (12.57, 3.13),    # location 26
    (37.12, 14.62),    # location 27
    (38.63, 27.26),    # location 28
    (15.08, 39.05),    # location 29
    (29.68, 23.97),    # location 30
    (18.12, 12.39),    # location 31
    (28.76, 8.76),    # location 32
    (22.00, 30.14),    # location 33
    (26.37, 35.47),    # location 34
    (9.01, 16.31),    # location 35
    (32.88, 31.42),    # location 36
    (34.74, 13.68),    # location 37
    (5.09, 1.00),    # location 38
    (8.23, 39.62),    # location 39
    (12.22, 24.30)    # location 40
    ])
        
    data['pickups_deliveriesw'] =  np.array([
        [1, 2],
        [3, 4],
        [5, 6],
        [7, 8],
        [9, 10],
        [11, 12],
        [13, 14],
        [15, 16],
        [17, 18],
        [19, 20]
    ])
        
    data['pickups_deliveriesh'] =  np.array([
        [21, 22],
        [23, 24],
        [25, 26],
        [27, 28],
        [29, 30],
        [31, 32],
        [33, 34],
        [35, 36],
        [37, 38],
        [39, 40]
    ])
    
    # Assign capacity Old way
    # data['demandsh'] = np.array([0, -1, 0, -1, 0, 0, -1, 1, 1, -1, 0, 0, 0, 0, 0, 1, 1])
    
    positive_demandh = np.array([1,1,1,1,1,1,1,1,1,1])
    data['demandsh'] = np.zeros(41)
    data['demandsh'][data['pickups_deliveriesh'][:,0]] = positive_demandh
    data['demandsh'][data['pickups_deliveriesh'][:,1]] = -positive_demandh
    
    positive_demandw = np.array([1,2,3,2,3,3,2,1,3,2])
    data['demandsw'] = np.zeros(41)
    data['demandsw'][data['pickups_deliveriesw'][:,0]] = positive_demandw
    data['demandsw'][data['pickups_deliveriesw'][:,1]] = -positive_demandw
    
    data['demand'] = data['demandsh'] + data['demandsw']
    
    return data


def main():
    
    data = create_data_model()
    '''
    order = [0,4,2,6,1]
    order += [order[0]]
    x_rout = data['Location'][order, 0]
    y_rout = data['Location'][order, 1]
    '''
    
    #plt.plot()
    for idxs in data['pickups_deliveriesw']:
        line = data['Location'][idxs].T
        plt.plot(line[0],line[1], c='red')
        
    for idxs in data['pickups_deliveriesh']:
        line = data['Location'][idxs].T
        plt.plot(line[0],line[1], c='blue')
     
    plt.axvline(20)
    plt.axhline(20)

       
    '''    
    plt.plot((228,798),(0,160))
    plt.plot((912,912),(0,400))
    plt.plot((114,0),(80,80))
    plt.plot((570,570),(160,400))
    plt.plot((342,684),(240,240))
    plt.plot((0,114),(640,480))
    plt.plot((342,228),(560,480))
    plt.plot((798,684),(640,560))
    '''
    
    '''
    for idx in order:
        x_rout.append(data['Location'][idx][0])
        y_rout.append(data['Location'][idx][1])
    '''
    
    #Label
    for n in range (len(data['Location'])):
       plt.annotate(str(n),(data['Location'][n]))


    #for n in range (len(data['Location'])):
     #   plt.annotate(f"{n} ({int(data['demand'][n])})",(data['Location'][n]))
        
        #print(data[n][0])
    
    #Point
    x, y = data['Locationh'].T
    plt.scatter(x,y, c='blue')
    
    x, y = data['Locationw'].T
    plt.scatter(x,y, c='red')
    
    plt.scatter(20, 20, c = 'grey')
    
    #plt.plot((456, 684, 798, 912, 570, 456),(320, 240, 160, 0, 160, 320))
    
    #plt.plot((456, 342, 228, 114, 0, 456),(320, 240, 0, 80, 80, 320))
    
    plt.show()
    
    
if __name__ == '__main__':
    main()