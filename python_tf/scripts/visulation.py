from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt


class TfVisulator:
    def __init__(self):

        #simulation params
        self.time_stamp = 0.1

        # Initialize common plot veriables
        self.fig = plt.figure(figsize=(10,10))
        ax  = plt.axes(projection='3d')

      
        for i in np.arange(0,1,0.05):

            self.create_link([1.1+i,2,1.3-i],[2,2.1-i,1],[1,1.1,3+i],ax)
        
        

    def create_link(self,p_x:list,p_y:list,p_z:list,ax_obj):

        # Data for a three-dimensional line
        
        zline = np.array(p_x)
        xline = np.array(p_y)
        yline = np.array(p_z)
        ax_obj.plot3D(xline, yline, zline, 'gray')

        ax_obj.set_zlim(0, 5)
        ax_obj.set_xlim(0, 5)
        ax_obj.set_ylim(0, 5)

        self.crate_joint(p_x,p_y,p_z,ax_obj)
        
        
        plt.pause(self.time_stamp)
        plt.cla()

    def crate_joint(self,p_x:list,p_y:list,p_z:list,ax_obj):
        ax_obj.scatter(p_x,p_y,p_z)
        



def main():
    vs_obj = TfVisulator()






if __name__ == '__main__':
    main()



