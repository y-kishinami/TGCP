import pickle
import argparse
from os import path


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--start_utter', type=path.abspath, help='Path to start utterance pool file')
    parser.add_argument('--target_word', type=path.abspath, help='Path to target word pool file')
    parser.add_argument('--id', type=path.abspath, help='Path to id file')
    parser.add_argument('--output', type=path.abspath, help='Path to output file')
    return parser


def load_id2data(path):
    id2data = dict()
    with open(path, "rb") as f:
        for i, data in enumerate(pickle.load(f)):
            id2data[str(i)] = data
    return id2data


def main():
    parser = create_parser()
    args = parser.parse_args()
    id2start_utter = load_id2data(args.start_utter)
    id2target_word = load_id2data(args.target_word)

    with open(args.id) as f, open(args.output, 'w') as out_f:
        for line in f:
            start_utter_id, target_word_id = line.strip().split('\t')
            print(id2start_utter[start_utter_id], id2target_word[target_word_id], sep='\t', file=out_f)


if __name__ == "__main__":
    main()