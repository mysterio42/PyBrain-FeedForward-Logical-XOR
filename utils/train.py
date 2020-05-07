from pybrain.supervised.trainers.backprop import BackpropTrainer


def train_model(net, data, epochs=20000, lr=0.01, momentum=0.06):
    trainer = BackpropTrainer(net, dataset=data, learningrate=lr, momentum=momentum)

    for i in range(epochs):
        error = trainer.train()

        if i % 1000 == 0:
            print(f'it: {i}, error: {error} \n'
                  f'[0,0]: {net.activate([0, 0])[0]}\n'
                  f'[0,1]: {net.activate([0, 1])[0]} \n'
                  f'[1,0]: {net.activate([1, 0])[0]} \n'
                  f'[1,1]: {net.activate([1, 1])[0]} \n'
                  f'{"-" * 100}\n')
    del trainer

    print(f'Training ends \n'
          f'[0,0]: {net.activate([0, 0])[0]}\n'
          f'[0,1]: {net.activate([0, 1])[0]} \n'
          f'[1,0]: {net.activate([1, 0])[0]} \n'
          f'[1,1]: {net.activate([1, 1])[0]} \n'
          f'{"-" * 100}\n')
