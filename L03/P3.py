"""
Dict is natural for counting. Write a function named word_freq
to take a string as its argument, count occurrences of each word,
and return the count as a dict.
"""


def clean_txt(msg):
    msg = msg.replace('.', ' ')
    msg = msg.replace(';', ' ')
    msg = msg.replace('\n', ' ')
    msg = msg.replace('  ', ' ')

    return msg


def word_freq(msg):

    cleaned = clean_txt(msg)

    wfreq = {'dummy': 0} # dummy
    # Write your code here
    for word in cleaned.split():
        if len(word) > 1:  # ไม่เอาคำสั้น <=1
            wfreq[word] = wfreq.get(word, 0) + 1

    return wfreq


if __name__ == '__main__':
    txt = "Evil is done by oneself; " + \
          "by oneself is one defiled. \n " + \
          "Evil is left undone by oneself; " + \
          "by oneself is one cleansed. \n " + \
          "Purity and impurity are one's own doing. \n" + \
          "No one purifies another. \n" + \
          "No other purifies one."
          # excerpt from Attavagga: Self, www.accesstoinsight.org

    print(txt)

    wf = word_freq(txt)


    print('\nCount:')
    print(wf)