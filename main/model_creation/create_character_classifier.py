import os
import sys

from main.character.character_classifier import CharacterClassifier
from main.feature.simple_image_feature_extrator import SimpleImageFeatureExtractor
from main.feature.specialized_hmm import SpecializedHMM


def create_character_classifier(save_to_file_path, factor, overlap, extract_mode):
    # example_dir = os.path.join(os.path.abspath('../..'), 'new_training_data')
    example_dir = os.path.join(os.path.abspath('../..'), 'character_examples')
    nr_of_training_examples = 90
    nr_of_test_examples = 10

    extractor = SimpleImageFeatureExtractor(nr_of_divisions=11,
                                            size_classification_factor=factor,
                                            overlap=overlap,
                                            extract_mode=extract_mode)

    training_examples, test_examples = extractor.extract_training_and_test_examples(example_dir,
                                                                                    nr_of_training_examples,
                                                                                    nr_of_test_examples)

    print training_examples
    print test_examples

    classifier = CharacterClassifier(training_examples,
                                     nr_of_hmms_to_try=1,
                                     fraction_of_examples_for_test=0,
                                     train_with_examples=False,
                                     initialisation_method=SpecializedHMM.InitMethod.count_based,
                                     feature_extractor=extractor)
    test_result = str(classifier.test(test_examples))
    print(test_result)
    classifier_string = classifier.to_string()
    file = open(save_to_file_path + ".dat", 'w')
    file.write(classifier_string)
    file.close()


if __name__ == '__main__':
    old_rec = sys.getrecursionlimit()
    sys.setrecursionlimit(10000)

    create_character_classifier("character_classifier_full", 4.6, 0.5,
                                SimpleImageFeatureExtractor.full_extract)

    sys.setrecursionlimit(old_rec)
