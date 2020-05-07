import argparse

from utils.data import xor_data
from utils.model import build_feedforward
from utils.train import train_model


def parse_args():
    def str2bool(v):
        if isinstance(v, bool):
            return v
        if v.lower() in ('yes', 'true', 't', 'y', '1'):
            return True
        elif v.lower() in ('no', 'false', 'f', 'n', '0'):
            return False
        else:
            raise argparse.ArgumentTypeError('Boolean value expected')


    parser = argparse.ArgumentParser()

    parser.add_argument('--inp', type=int,required=True,
                        help='FeedForward network Input Dimension')
    parser.add_argument('--hidden', type=int,required=True,
                        help='FeedForward network Hidden Dimension')
    parser.add_argument('--out', type=int,required=True,
                        help='FeedForward network Output Dimension')
    parser.add_argument('--bias',type=str2bool,default=True,required=True,
                        help='Add Bias Unit to the network')

    parser.print_help()

    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()

    data = xor_data()

    net = build_feedforward(args.inp, args.hidden, args.out,args.bias)
    print(net)
    # train_model(net, data)
