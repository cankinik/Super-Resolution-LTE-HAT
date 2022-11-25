import matplotlib.pyplot as plt
import numpy as np

def running_average(x, y, N):
    y_ = np.convolve(y, np.ones(N)/N, mode='valid')
    x_ = x[N//2:-N//2+1]
    return x_, y_


log_directories = ['Training Trials/2e-4_train_swinir-lte', 'Training Trials/5e-5_train_swinir-lte', 'Training Trials/1e-3_train_swinir-lte']
all_losses = []
all_psnrs = []
for log in log_directories:
    lr = log[16:20]                                     # Get lr from folder name
    log_file = open(log + '/log.txt', "r")              # Open log.txt
    log = log_file.readlines()
    losses_over_epochs = []
    epochs = []
    psnrs = []
    epoch_counter = 1
    for line in log:                                    # Iterate over the lines in log.txt
        if line[0] == 'e':                              # Lines that start with e are the appropriate ones
            loss = float(line.split()[3][5:11])         # When spit, 3 is loss=######, 5:11 gives the ####, and and we convert to float
            losses_over_epochs.append(loss)
            epochs.append(epoch_counter)
            epoch_counter += 1
            psnr = float(line.split()[5][5:11])
            psnrs.append(psnr)

    log_file.close()                                    # Close the file when done reading it
    all_losses.append((lr, epochs, losses_over_epochs))
    all_psnrs.append((lr, epochs, psnrs))

# Loss plot
for lr, epochs, losses_over_epochs in all_losses:
    plt.plot(epochs, losses_over_epochs, label=lr)
    N = 20
    epoch_average, loss_average = running_average(epochs, losses_over_epochs, N)
    plt.plot(epoch_average, loss_average, label=str(lr) + ' over ' + str(N))
plt.legend()
plt.show()

# PSNR plot
for lr, epochs, psnrs in all_psnrs:
    plt.plot(epochs, psnrs, label=lr)
    N = 20
    epoch_average, psnr_average = running_average(epochs, psnrs, N)
    plt.plot(epoch_average, psnr_average, label=str(lr) + ' over ' + str(N))
plt.legend()
plt.show()
