#Radesh Shiwlochan
#CS780 Natural Language Processing
#Project 1

word_summary = {}
bigram_dictionary = {}
dictionary_with_add_tags = {}
brown_test_diction = {}
learner_test_diction = {}
count = 0
count_of_two_words = 0

def get_count_of_single_word(str,input_file):
    word_count = 0
    open_file = open(input_file)
    for word in open_file.read().split():
        if word == str:
            word_count += 1
    open_file.close()
    return word_count

def add_tags(input_file, output_file):
    start_symbol = "<s> "
    stop_symbol = " </s>"
    read_from_file = open(input_file)
    write_to_file = open(output_file, 'w')
    for line in read_from_file:
        result = start_symbol + line[:len(line)-1].lower() + stop_symbol + '\n'
        write_to_file.write(result)
    read_from_file.close()
    write_to_file.close()

def build_unigram(input_file):
    unigram_model = 1.0
    count_of_total = count
    open_file = open(input_file)
    for word in open_file.read().split():
        if word not in word_summary:
            unigram_model *=  float(value_of_unknown)/count_of_total
            print unigram_model
        else:
            count_of_word = word_summary[word]
            unigram_model *= float(count_of_word)/count_of_total
            print unigram_model
    print "this is the unigram model "
    print unigram_model
    open_file.close()

def build_bigram(input_file, unk_count, total_words):
    bigram_model = 1.0
    open_file = open(input_file)
    for a_line in open_file:
        words_in_line = a_line.split()
        size_of_line = len(words_in_line) - 1
        countr = 0
        indx = 1
        prev_indx = 0
        while countr < size_of_line:
            word_A = words_in_line[prev_indx]
            word_B = words_in_line[indx]
            full_word = word_A + word_B
            if full_word in bigram_dictionary:
                count_of_numtr = bigram_dictionary[full_word]
                count_of_denomtr = word_summary[word_A]
                bigram_model *= float(count_of_numtr) / count_of_denomtr
                print "bigram probability "
                print bigram_model

            elif word_A + "<unk>" in bigram_dictionary:
                access_word = word_A + "<unk>"
                the_count = bigram_dictionary[access_word]
                bigram_model *= float(the_count) / unk_count

            elif "<unk> + word_B" in bigram_dictionary:
                access_word = "<unk> + word_B"
                the_count = bigram_dictionary[access_word]
                bigram_model *= float(the_count)/ word_summary[word_B]
            else:
                access_word = "<unk>" + "<unk>"
                the_count = bigram_dictionary[access_word]
                bigram_model *= float(the_count)/ unk_count

    open_file.close()

def build_bigram_with_smoothing(input_file, unk_count, total_words, vocab_size):
    bigram_model = 1.0
    open_file = open(input_file)
    for a_line in open_file:
        words_in_line = a_line.split()
        size_of_line = len(words_in_line) - 1
        countr = 0
        indx = 1
        prev_indx = 0
        while countr < size_of_line:
            word_A = words_in_line[prev_indx]
            word_B = words_in_line[indx]
            full_word = word_A + word_B
            if full_word in bigram_dictionary:
                count_of_numtr = bigram_dictionary[full_word]
                count_of_denomtr = word_summary[word_A]
                bigram_model *= float((count_of_numtr) + 1) / (count_of_denomtr + vocab_size)
                print "bigram probability "
                print bigram_model

            elif word_A + "<unk>" in bigram_dictionary:
                access_word = word_A + "<unk>"
                the_count = bigram_dictionary[access_word]
                bigram_model *= float((the_count) + 1) / (unk_count + vocab_size)

            elif "<unk> + word_B" in bigram_dictionary:
                access_word = "<unk> + word_B"
                the_count = bigram_dictionary[access_word]
                bigram_model *= float((the_count) + 1) / (word_summary[word_B] + vocab_size)
            else:
                access_word = "<unk>" + "<unk>"
                the_count = bigram_dictionary[access_word]
                bigram_model *= float((the_count) + 1 )/ (unk_count + vocab_size)

    open_file.close()

def print_dictionary(dictionary):
    for k, v in dictionary.items():
        print k,v

def count_single_words_in_list(dictionary):
    count_of_1 = 0
    for k, v in dictionary.items():
        if v == 1:
            #print k,v
            count_of_1 += 1

def count_words_in_dictionary(dictionary):
    return len(dictionary)

def create_dictionary(input_file, input_dictionary):
    open_file = open(input_file)
    retrieve_word_count = open(input_file, 'r')
    count_words = 0
    for word in retrieve_word_count.read().split():
        if word not in input_dictionary:
            input_dictionary[word] = 1
            count_words += 1
        else:
            input_dictionary[word] += 1
            count_words += 1
    retrieve_word_count.close()

def count_tokens_in_file(input_file):
    num_of_tokens = 0
    inc = 0
    a_line = open(input_file)
    for line in a_line:
        num_of_tokens += len(line)
        num_of_words = line.split()
        length_of_array = len(num_of_words) - 1
    return num_of_tokens

def count_words_not_training_data(dictionary):
    word_count = 0
    for k,v in word_summary.items():
        if k not in dictionary:
            dictionary[k] = 1
            word_count += 1
    return word_count

add_tags('brown-train.txt','brown-train-with-tags')
add_tags('brown-test.txt', 'brown-test-with-tags')
add_tags('learner-test.txt', 'learner-test-with-tags')

create_dictionary('brown-train-with-tags', word_summary)

read_file_for_bigram = open('final_training_data')
for line in read_file_for_bigram:
    array_of_words = line.split()
    array_length = len(array_of_words) - 1
    counter = 0
    index = 1
    previous_index = index - 1
    while(counter < array_length):
        two_words =  array_of_words[previous_index] + " " + array_of_words[index]
        if two_words not in bigram_dictionary:
            bigram_dictionary[two_words] = 1
            count_of_two_words += 1
        else:
            bigram_dictionary[two_words] += 1
            count_of_two_words += 1
        counter += 1
        index += 1
        previous_index += 1
read_file_for_bigram.close()

read_file = open('brown-train-with-tags','r')
replace_single_words = open('final_training_data','w')
for word in read_file.read().split():
    if word_summary[word] == 1 and word == '</s>':
        replace_single_words.write(' <unk> ' + '\n')
    elif word_summary[word] == 1:
        replace_single_words.write(' <unk> ')
    elif word == "</s>":
        replace_single_words.write(word + ' ' + '\n')
    else:
        replace_single_words.write(word + ' ')
read_file.close()
replace_single_words.close()

#value of unknown words
value_of_unknown = get_count_of_single_word('<unk>','final_training_data')

#create a dictionary from the file with all the tags added
create_dictionary('brown-train-with-tags', dictionary_with_add_tags)

unique_words = count_words_in_dictionary(dictionary_with_add_tags)
print "this is the amount of unique words in the corpus "
print unique_words

#get the count of the tokens in training data including the tags
count = count_tokens_in_file('final_training_data')
print "this is the number of tokens in the training corpus "
print count

#create a dictionary from the data in brown-test-with-tags and learner-test-with-tags
create_dictionary('brown-test-with-tags', brown_test_diction)
create_dictionary('learner-test-with-tags', learner_test_diction)

words_in_brown_test = count_words_not_training_data(brown_test_diction)
words_in_learner_test = count_words_in_dictionary(learner_test_diction)
print_dictionary(brown_test_diction)