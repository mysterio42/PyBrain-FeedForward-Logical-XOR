from pybrain.structure.connections.full import FullConnection
from pybrain.structure.modules.biasunit import BiasUnit
from pybrain.structure.modules.linearlayer import LinearLayer
from pybrain.structure.modules.sigmoidlayer import SigmoidLayer
from pybrain.structure.networks.feedforward import FeedForwardNetwork


def build_feedforward(in_dim, hidden_dim, out_dim, bias):
    net = FeedForwardNetwork()

    net.addInputModule(
        LinearLayer(in_dim, name='in'))
    net.addModule(
        SigmoidLayer(hidden_dim, name='hidden'))
    net.addOutputModule(
        LinearLayer(out_dim, name='out'))

    net.addConnection(FullConnection(
        net['in'], net['hidden']))
    net.addConnection(FullConnection(
        net['hidden'], net['out']))

    if bias:
        net.addModule(
            BiasUnit(name='bias'))
        net.addConnection(FullConnection(
            net['bias'], net['hidden']))
        net.addConnection(FullConnection(
            net['bias'], net['out']))

    net.sortModules()

    return net
