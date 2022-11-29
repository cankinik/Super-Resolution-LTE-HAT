import matplotlib.pyplot as plt
import numpy as np
import os

def running_average(x, y, N):
    # TODO: Get delta between x, and divide N by that, so that if the validation frequency is 10, it will do N/10 = 5
    y_ = np.convolve(y, np.ones(N)/N, mode='valid')
    x_ = x[N//2:-N//2+1]
    return x_, y_


log_directories = [
                    # '1e-3_4x6_300_train_swinir-lte', 
                    # '1e-4_4x6_300_train_swinir-lte', 
                    # '2e-4_6x6_300_train_swinir-lte', 
                    # '5e-5_4x6_300_train_swinir-lte', 
                    '2e-4_3x6_600_Final_HAT_train_hat-lte',
                    '2e-4_2x6_900_train_swinir-lte'
                    # '2e-4_6x2_900_train_swinir-lte'
                    ]
all_losses = []
all_psnrs = []
for log in log_directories:
    descriptor = log[0:12]                                     # Get lr from folder name
    log_file = open(os.path.join('Training Trials', log, 'log.txt'), "r")              # Open log.txt
    log = log_file.readlines()
    losses_over_epochs = []
    epochs = []                                         # TODO: Get epoch from the logs as well. Also check fpr the existence of PSNR for different validation frequencies.
    psnrs = []
    epoch_counter = 1
    for line in log:                                    # Iterate over the lines in log.txt
        if line[0] == 'e':                              # Lines that start with e are the appropriate ones
            loss = float(line.split()[3][5:11])         # When spit, 3 is loss=######, 5:11 gives the ####, and and we convert to float
            losses_over_epochs.append(loss)
            epochs.append(epoch_counter)
            epoch_counter += 1
            # psnr = float(line.split()[5][5:11])
            # psnrs.append(psnr)

    log_file.close()                                    # Close the file when done reading it
    all_losses.append((descriptor, epochs, losses_over_epochs))
    # all_psnrs.append((descriptor, epochs, psnrs))

# Loss plot
for descriptor, epochs, losses_over_epochs in all_losses:
    # plt.plot(epochs, losses_over_epochs, label=descriptor)
    N = 3
    epoch_average, loss_average = running_average(epochs, losses_over_epochs, N)
    plt.plot(epoch_average, loss_average, label=str(descriptor) + ' over ' + str(N))
plt.legend()
plt.show()

# # PSNR plot
# for descriptor, epochs, psnrs in all_psnrs:
#     # plt.plot(epochs, psnrs, label=descriptor)
#     N = 50
#     epoch_average, psnr_average = running_average(epochs, psnrs, N)
#     plt.plot(epoch_average, psnr_average, label=str(descriptor) + ' over ' + str(N))
# plt.legend()
# plt.show()
