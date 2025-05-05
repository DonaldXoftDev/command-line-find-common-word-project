def get_sentence_from_user():
    sentences =[]
    print('Enter each sentence one by one and then type "done" when you are done.')
    getting_sentence = True
    while getting_sentence:
        user_input = input('Enter a sentence: ').lower()
        if user_input.lower() == 'done':
           break
        sentences.append(user_input)
    return sentences

def merge_sentence(sentence_list):
    if sentence_list:
        merged_sentence = ' '.join(sentence_list)
        return merged_sentence
    else:
        print('The list provided is empty.')

def clean_sentence(merge_sent):
        cleaned_word = ''
        current_filtered_list = []

        for char in merge_sent:
           if char.isalpha():
               cleaned_word += char
           elif char.isspace() or not char.isalpha():
               if cleaned_word:
                  current_filtered_list.append(cleaned_word)
                  cleaned_word = ''
        if cleaned_word:
            current_filtered_list.append(cleaned_word)
        return current_filtered_list


def dict_counted_words(filter_lst):
    dict_count_words = {}
    for word in filter_lst:
        count_word = filter_lst.count(word)
        if word not in dict_count_words:
            dict_count_words[word] = count_word

    return dict_count_words


def highest_count_word(dictionary_key_count):
        highest_count = 0
        word_highest_count = []
        for key,value in dictionary_key_count.items():
            if value >= highest_count:
                highest_count = value
                word_highest_count.append(key)
        print(f'{", ".join(word_highest_count)} occurs {highest_count} times.')


def find_common_word(sentence_list):
    merged_sent = merge_sentence(sentence_list)
    filter_list = clean_sentence(merged_sent)
    dictionary = dict_counted_words(filter_list)
    highest_count_word(dictionary)

list_of_sentences = get_sentence_from_user()
find_common_word(list_of_sentences)
