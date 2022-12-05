import matplotlib.pyplot as plt
import numpy as np
import os

def running_average(x, y, N):
    y_ = np.convolve(y, np.ones(N)/N, mode='valid')
    x_ = x[N//2:-N//2+1]
    return x_, y_


log_directories = [
                        # '1e-4_4x6_300_LTE-SwinIR',
                        # '2e-4_2x6_600_LTE-SwinIR', 
                        # '2e-4_2x6_900_LTE-SwinIR', 
                        '2e-4_3x6_600_LTE-HAT_Final',
                        '2e-4_3x6_600_LTE-SwinIR_Final',
                        # '2e-4_6x2_900_LTE-SwinIR',
                        # '2e-4_6x6_300_LTE-SwinIR',
                        '5e-5_4x6_300_LTE-SwinIR' 
                  ]

all_losses = []
for log in log_directories:
    descriptor = log                                    # The name of the folder is the descriptor
    log_file = open(os.path.join('Training Trials', log, 'log.txt'), "r")              # Open log.txt
    log = log_file.readlines()
    losses_over_epochs = []
    epochs = []                                         
    psnrs = []
    epoch_counter = 1
    for line in log:                                    # Iterate over the lines in log.txt
        if line[0] == 'e':                              # Lines that start with e are the appropriate ones
            loss = float(line.split()[3][5:11])         # When spit, 3 is loss=######, 5:11 gives the ####, and then we convert to float
            losses_over_epochs.append(loss)
            epochs.append(epoch_counter)
            epoch_counter += 1

    log_file.close()                                    # Close the file when done reading it
    all_losses.append((descriptor, epochs, losses_over_epochs))

# Loss plot
N = 50
for descriptor, epochs, losses_over_epochs in all_losses:
    # plt.plot(epochs, losses_over_epochs, label=descriptor)    # Raw data
    epoch_average, loss_average = running_average(epochs, losses_over_epochs, N)
    plt.plot(epoch_average, loss_average, label=str(descriptor))
plt.title('Training loss over epochs (Running Average of %d)' % N)
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()
plt.show()
