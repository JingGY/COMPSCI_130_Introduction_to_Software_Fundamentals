import math
import csv

# Question 01
def get_longest_common_name(vernacular_names):
    if not vernacular_names.isspace():
        name_list = vernacular_names.split("|")
        print("test", name_list)
        max_name_index = 0
        for i in range(len(name_list)):
            if len(name_list[i]) > len(name_list[max_name_index]):
                max_name_index = i
        return name_list[max_name_index]
    else:
        return None

# Question 02
def get_classification_hierarchy(classification_ranks, classifications):
    try:
        rank_list = classification_ranks.split("|")
        class_list = classifications.split("|")
        rank_len = len(rank_list)
        class_len = len(class_list)
        new_list = []
        if rank_len == class_len:
            for i in range(len(rank_list)):
                rank = rank_list[i]
                the_class = class_list[i]
                a_tuple = (rank, the_class)
                new_list.append(a_tuple)

        else:
            raise ValueError(
                "ERROR: Invalid input, classification ranks do not match classifications!")
    except ValueError as err:
        print(err)
    finally:
        return new_list

# Question 03

def get_biostatus(biostatus_string):
    a_list = ["Endemic", "Non-endemic", "Exotic", "Indigenous"]
    biostatus_list = biostatus_string.split("|")
    is_find = False
    for item in biostatus_list:
        if item in a_list:
            is_find = True
            return item
    if is_find is False:
        return "N/A"

# Question 04

class Ave:
    def __init__(self, scientific_name, common_name, biostatus, classification_hierarchy):
        self.__scientific_name = scientific_name
        self.__common_name = common_name
        self.__biostatus = biostatus
        self.__classification_hierarchy = classification_hierarchy

    def __repr__(self):
        self.__rep = "Ave<" + self.__scientific_name + ">"
        return self.__rep

    def __lt__(self, other):
        self.__isSame = False
        if self.__scientific_name < other.__scientific_name:
            self.__isSame = True
        return self.__isSame

    def __eq__(self, other):
        self.__isBirdSame = False
        if self.__lt__ and self.__common_name == other.__common_name and self.__biostatus == other.__biostatus:
            self.__isBirdSame = True
        return self.__isBirdSame

    def find_in_classification_hierarchy(self, classification_rank):
        self.__rank = None
        for item in self.__classification_hierarchy:
            if classification_rank in item:
                self.__rank = item[1]
        return self.__rank

    def lowest_classification_rank(self):
        self.__lowest_class = self.__classification_hierarchy[0][0]
        return self.__lowest_class

    def get_scientific_name(self):
        return self.__scientific_name

    def get_common_name(self):
        return self.__common_name

    def get_biostatus(self):
        return self.__biostatus

    def __str__(self):
        return self.__common_name + ", Status = " + self.__biostatus

# Question 05

class BirdDatasetReader:
    def __init__(self, filename):
        self.__csv_filename = filename
    #question 1

    def __get_longest_common_name(vernacular_names):
        trim_name = vernacular_names.lstrip()

        if len(trim_name) > 0 and any(c.isalpha() for c in trim_name):
            name_list = trim_name.split("|")
            max_name_index = 0
            for i in range(len(name_list)):
                if len(name_list[i]) > len(name_list[max_name_index]):
                    max_name_index = i
            return name_list[max_name_index]
        else:
            return None

    #question 2
    def __get_classification_hierarchy(classification_ranks, classifications):
        try:
            rank_list = classification_ranks.split("|")
            class_list = classifications.split("|")
            rank_len = len(rank_list)
            class_len = len(class_list)
            new_list = []
            if rank_len == class_len:
                for i in range(len(rank_list)):
                    rank = rank_list[i]
                    the_class = class_list[i]
                    a_tuple = (rank, the_class)
                    new_list.append(a_tuple)

            else:
                raise ValueError(
                    "ERROR: Invalid input, classification ranks do not match classifications!")
        except ValueError as err:
            print(err)
        finally:
            return new_list

    def __get_biostatus(biostatus_string):
        a_list = ["Endemic", "Non-endemic", "Exotic", "Indigenous"]
        biostatus_list = biostatus_string.split("|")
        is_find = False
        for item in biostatus_list:
            if item in a_list:
                is_find = True
                return item
        if is_find is False:
            return "N/A"

    def read_birds_dataset(self):

        try:
            csvfile = open(self.__csv_filename, mode='r')
            csv_dict_reader = csv.DictReader(csvfile)
            index = 1
            ave_list = []
            for row in csv_dict_reader:

                commen_names = row['VernacularNamesForScientific']
                common_name = BirdDatasetReader.__get_longest_common_name(
                    commen_names)
                if common_name is None:
                    common_name = row['ScientificName']
                biostatus = BirdDatasetReader.__get_biostatus(row['Biostatus'])
                classification_ranks = row["ClassificationRanks"]
                hierarchy = BirdDatasetReader.__get_classification_hierarchy(classification_ranks,
                                                                             row["Classification"])
                index += 1
                ave_list.append(Ave(row['ScientificName'], common_name,
                                    biostatus, hierarchy))

            csvfile.close()
            return ave_list
            

        except FileNotFoundError:
            print("ERROR: File '" + self.__csv_filename + "' not found!")
            return []

# Question 06
def consistency_check(all_aves):
    is_consistent = True
    for i in range(len(all_aves)):

        lowest_class = all_aves[i].lowest_classification_rank()

        scientic_name = all_aves[i].get_scientific_name()
        rank = all_aves[i].find_in_classification_hierarchy(lowest_class)
        if scientic_name != rank:
            is_consistent = False
            index = i+1
            print("Inconsistency found for bird #" + str(index) +
                  " in the list! " + scientic_name + " vs " + rank)
    return is_consistent

# Question 07
def print_histogram_of_biostatuses(list_of_aves):
    print("Histogram of biostatus entries:")
    bio_list = []
    bio_uniqe = {}
    for i in list_of_aves:
        bio_list.append(i.get_biostatus())

    for i in bio_list:
        if i not in bio_uniqe:
            bio_uniqe[i] = 1
        else:
            bio_uniqe[i] += 1
    key_list = sorted(bio_uniqe.keys())

    for key in key_list:
        space_num = 12 - len(key)
        print(key+" " * space_num + ": " + str(bio_uniqe[key]))

# Question 08

def get_birds_with_specific_classification(list_of_aves, classification_rank, classification):
    specific_aves = []
    for i in list_of_aves:
        the_classification = i.find_in_classification_hierarchy(
            classification_rank)
        if the_classification == classification:
            specific_aves.append(i)
    return specific_aves

# Question 09

def find_bird_by_scientific_name_binary_search(sorted_list_of_aves, scientific_name):
    min_index = 0
    max_index = len(sorted_list_of_aves) - 1
    count = 0

    while min_index <= max_index:
        count += 1
        mid_index = math.floor((max_index + min_index)/2)
        if sorted_list_of_aves[mid_index].get_scientific_name() == scientific_name:
            return (sorted_list_of_aves[mid_index], count)

        elif sorted_list_of_aves[mid_index].get_scientific_name() > scientific_name:
            max_index = mid_index - 1
        elif sorted_list_of_aves[mid_index].get_scientific_name() < scientific_name:
            min_index = mid_index + 1

    return (None, 0)

# Below are a number of unit tests which your code has to fulfill. If you are interested in how this works, consider
# looking at the documentation of the Python unittest module. However, you don't have to change anything below here,
# just make sure that when you execute this class through Python command line or an IDE like IDLE, you receive the
# message:
# Ran 2 tests in x.xxx seconds.
# OK

import unittest

class TestBirdsMethods(unittest.TestCase):

    def test_0_read_csvfile(self):
        csv_filename = 'NZOR-BirdsTaxonomicExcerpt_15only.csv'
        reader = BirdDatasetReader(csv_filename)
        all_aves = reader.read_birds_dataset()
        self.assertEqual(repr(all_aves), "[Ave<Callaeas cinerea>, Ave<Hirundapus>, Ave<Leucocarbo colensoi>, Ave<Egretta alba>, Ave<Vanellus miles>, Ave<Thalasseus>, Ave<Anthus novaeseelandiae>, Ave<Callaeas>, Ave<Rallus pectoralis muelleri>, Ave<Procellaria>, Ave<Emeidae>, Ave<Puffinus puffinus puffinus>, Ave<Phalaropus fulicarius>, Ave<Porzana>, Ave<Anas>]")

    def test_1_find_all_birds(self):
        csv_filename = 'NZOR-BirdsTaxonomicExcerpt.csv'
        reader = BirdDatasetReader(csv_filename)
        all_aves = reader.read_birds_dataset()
        all_aves_sorted = sorted(all_aves)
        largest_number_of_search_steps = -1000
        smallest_number_of_search_steps = 1000
        index = 0
        for ave in all_aves:
            bird, nr_search_steps = find_bird_by_scientific_name_binary_search(all_aves_sorted, ave.get_scientific_name())
            index += 1
            if nr_search_steps > largest_number_of_search_steps:
                largest_number_of_search_steps = nr_search_steps
            if nr_search_steps < smallest_number_of_search_steps:
                smallest_number_of_search_steps = nr_search_steps
        self.assertEqual(largest_number_of_search_steps, 11)
        self.assertEqual(smallest_number_of_search_steps, 1)

if __name__ == "__main__":
    unittest.main(verbosity=0)
